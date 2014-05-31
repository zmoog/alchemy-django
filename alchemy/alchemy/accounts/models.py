from decimal import Decimal
import logging
import re

from django.conf import settings
from django.db import models
from django.db import transaction
from django.db.models import Q, Sum
from django_extensions.db.fields import UUIDField

from django_extensions.db.models import TimeStampedModel

logger = logging.getLogger(__name__)


class Account(TimeStampedModel):
    id = UUIDField(primary_key=True)
    title = models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.0))

    def related_transfers(self):
        return Transfer.objects.filter(Q(source__id=self.id) | Q(destination__id=self.id)).order_by('-created')

    def __str__(self):
        return self.title


class Transfer(TimeStampedModel):
    id = UUIDField(primary_key=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    source = models.ForeignKey('Account', related_name='source')
    destination = models.ForeignKey('Account', related_name='destination')
    operation_date = models.DateField()
    value_date = models.DateField()
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    shops = models.ManyToManyField('Shop', null=True, blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def save(self, *args, **kwargs):

        with transaction.atomic():

            super(Transfer, self).save(*args, **kwargs)

            self._extract_and_add(self.description, r"(?<=#)\w+", self.tags, Tag)
            self._extract_and_add(self.description, r"(?<=@)\w+", self.shops, Shop)

            self._update_account_balance(self.source)
            self._update_account_balance(self.destination)

    def _extract_and_add(self, text, regex, relationship, Model):

        entities = re.findall(regex, text)

        relationship.clear()

        for name in entities:
            model, created = Model.objects.get_or_create(pk=name)
            relationship.add(model)


    def _update_account_balance(self, account):

        logger.info('starting balance for %s is %s', account.title, account.balance)

        ins = Transfer.objects.filter(Q(destination__id=account.id)).aggregate(Sum('amount'))['amount__sum'] or 0
        outs = Transfer.objects.filter(Q(source__id=account.id)).aggregate(Sum('amount'))['amount__sum'] or 0
        balance = ins - outs
        logger.info("new balance for %s is %s (%s - %s)", account.title, balance, ins, outs)
        account.balance = balance
        account.save()


class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.name
