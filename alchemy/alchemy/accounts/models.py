from decimal import Decimal
import logging
import re

from django.db import models

from alchemy.core.models import TimeStampedModel

logger = logging.getLogger(__name__)



class Account(TimeStampedModel):
    title = models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.0))


class Transfer(TimeStampedModel):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    source = models.ForeignKey('Account', related_name='source')
    destination = models.ForeignKey('Account', related_name='destination')
    operation_date = models.DateField()
    value_date = models.DateField()
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    locations = models.ManyToManyField('Location', null=True, blank=True)

    def save(self, *args, **kwargs):

        super(Transfer, self).save(*args, **kwargs)

        #tags = re.findall(r"(?<=#)\w+", self.description)

        #self.tags.clear()

        #for tag_name in tags:
        #    tag, created = Tag.objects.get_or_create(pk=tag_name)
        #    logger.error("adding tag: %s (created: %s)" % (tag, created))
        #    self.tags.add(tag)

        #locations = re.findall(r"(?<=@)\w+", self.description)

        #self.locations.clear()

        #for location_name in locations:
        #    location, created = Location.objects.get_or_create(pk=location_name)
        #    logger.error("adding location: %s (created: %s)" % (location, created))
        #    self.locations.add(location)

        self._extract_and_add(self.description, r"(?<=#)\w+", self.tags, Tag)
        self._extract_and_add(self.description, r"(?<=@)\w+", self.locations, Location)

    def _extract_and_add(self, text, regex, relationship, Model):

        entities = re.findall(regex, text)

        relationship.clear()

        for name in entities:
            model, created = Model.objects.get_or_create(pk=name)
            relationship.add(model)


class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.name
