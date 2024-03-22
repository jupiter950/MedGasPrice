from django.db import models

# Create your models here.
class GasData(models.Model):
    price_date = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add = True)
    date_updated = models.DateField(auto_now = True)
class MedGasPrice(models.Model):
    low = models.CharField(max_length=255)
    high = models.CharField(max_length=255)
    avg = models.CharField(max_length=255)

class MedPrice(models.Model):
    med = models.CharField(max_length=255)