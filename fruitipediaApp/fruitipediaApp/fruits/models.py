from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(
        unique=True,
    )


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            RegexValidator(regex='^[a-zA-Z]+$', message="Fruit name should contain only letters!")
        ]
    )
    Image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        to='Fruit',
        on_delete=models.CASCADE,
        null=True
    )