from django.db import models
from django.contrib.auth.models import User, Group
import datetime


class Farm(models.Model):
    """Model definition for Farm."""

    group = models.ForeignKey(Group, unique=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    chickens = models.IntegerField(default=0)
    rooster = models.IntegerField(default=0)

    class Meta:
        """Meta definition for Farm."""

        verbose_name = 'Farm'
        verbose_name_plural = 'Farms'

    def __str__(self):
        """Unicode representation of Farm."""
        return f'{self.name}'

    def save(self):
        """Save method for Farm."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Farm."""
        return ('')

    # TODO: Define custom methods here


class Eggs(models.Model):
    """Model definition for Eggs."""

    layed = models.IntegerField(default=0)
    broken = models.IntegerField(default=0)
    pecked = models.IntegerField(default=0)
    date = models.DateField('Date', default=datetime.date.today)

    class Meta:
        """Meta definition for Eggs."""

        verbose_name = 'Eggs'

    def __str__(self):
        """Unicode representation of Eggs."""
        pass

    def save(self):
        """Save method for Eggs."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Eggs."""
        return ('')

    # TODO: Define custom methods here


class Sale(models.Model):
    """Model definition for Sale."""

    sold = models.IntegerField(verbose_name='Verkaufter Eier', default=0)
    used = models.IntegerField(verbose_name='Gebrauchter Eier', default=0)
    price = models.FloatField(verbose_name='Eier Preise', default=0.3)
    date = models.DateField('Date', default=datetime.date.today)

    class Meta:
        """Meta definition for Sale."""

        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        """Unicode representation of Sale."""
        date = self.date.strftime('%Y-%m-%d')
        return f'{date}: {self.total}'

    def save(self):
        """Save method for Sale."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Sale."""
        return ('')

    def total(self):
        """Return the total price of the sold eggs."""
        pass
