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


class EggsCount(models.Model):
    """Model definition for EggsCount."""

    layed = models.IntegerField(default=0)
    broken = models.IntegerField(default=0)
    pecked = models.IntegerField(default=0)
    date = models.DateField('Date', default=datetime.date.today)
    farm = models.ForeignKey(Farm, unique=True, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for EggsCount."""

        verbose_name = 'EggsCount'

    def __str__(self):
        """Unicode representation of EggsCount."""
        pass

    def save(self):
        """Save method for EggsCount."""
        pass

    def get_absolute_url(self):
        """Return absolute url for EggsCount."""
        return ('')

    # TODO: Define custom methods here


class Sale(models.Model):
    """Model definition for Sale."""

    sold = models.IntegerField(verbose_name='Verkaufter Eier', default=0)
    used = models.IntegerField(verbose_name='Gebrauchter Eier', default=0)
    price = models.FloatField(verbose_name='Eier Preise', default=0.3)
    date = models.DateField('Date', default=datetime.date.today)
    farm = models.ForeignKey(Farm, unique=True, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Sale."""

        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        """Unicode representation of Sale."""
        pass

    def save(self):
        """Save method for Sale."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Sale."""
        return ('')

    def total(self):
        """Return the total price of the sold eggs."""
        pass


class Storage(models.Model):
    """Model definition for Storage."""

    quantity = models.FloatField(verbose_name='Lagerstand', default=0.0)
    date = models.DateField('Date', default=datetime.date.today)
    price = models.FloatField(verbose_name='Eier Preise', default=3.0)
    farm = models.ForeignKey(Farm, unique=False, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Storage."""

        verbose_name = 'Storage'
        verbose_name_plural = 'Storages'

    def __str__(self):
        """Unicode representation of Storage."""
        pass

    def save(self):
        """Save method for Storage."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Storage."""
        return ('')

    # TODO: Define custom methods here


class FoodCount(models.Model):
    """Model definition for FoodCount."""

    used = models.FloatField(verbose_name='Verbrauch', default=0.0)
    date = models.DateField('Date', default=datetime.date.today)
    farm = models.ForeignKey(Farm, unique=True, on_delete=models.CASCADE)
    stroage = models.ForeignKey(Storage, unique=True, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for FoodCount."""

        verbose_name = 'FoodCount'
        verbose_name_plural = 'FoodCounts'

    def __str__(self):
        """Unicode representation of FoodCount."""
        pass

    def save(self):
        """Save method for FoodCount."""
        pass

    def get_absolute_url(self):
        """Return absolute url for FoodCount."""
        return ('')

    # TODO: Define custom methods here
