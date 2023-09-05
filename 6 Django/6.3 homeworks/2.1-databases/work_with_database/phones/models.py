from django.db import models


class Phone(models.Model):
    # phone_id = models.CharField('phone_id', max_length=50, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    image = models.CharField(max_length=255, null=True)
    price = models.IntegerField(null=True)
    release_date = models.DateField(null=True)
    lte_exist = models.BooleanField(null=True)
    slug = models.CharField(max_length=55, null=False)

    def __str__(self):
        return f'{self.id}, {self.name}, {self.price}, {self.release_date}, ' \
               f'{self.lte_exist}, {self.slug}'