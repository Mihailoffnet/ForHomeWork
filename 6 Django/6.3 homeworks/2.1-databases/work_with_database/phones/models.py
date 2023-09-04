from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, null=False)
    image = models.CharField(max_length=255, null=True)
    price = models.IntegerField(null=True)
    release_date = models.DateField(null=True)
    lte_exist = models.BooleanField(null=True)
    slug = models.CharField(max_length=55, null=False)

