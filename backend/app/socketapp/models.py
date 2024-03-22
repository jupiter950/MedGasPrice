from django.db import models

# Create your models here.
class GasData(models.Model):
    tid = models.CharField(max_length=255)
    chainId = models.CharField(max_length=20)
    timestamp = models.CharField(max_length=255)
    blockNumber = models.BigIntegerField()
    gasPrice = models.CharField(max_length=255)
    status = models.BooleanField()
    burnedFees = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    index = models.DecimalField(max_digits=6, decimal_places=2)
    cfrom = models.CharField(max_length=255)
    fto = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add = True)
    date_updated = models.DateField(auto_now = True)
