# Generated by Django 5.0.3 on 2024-03-22 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socketapp', '0002_medprice_rename_burnedfees_gasdata_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedGasPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('low', models.CharField(max_length=255)),
                ('high', models.CharField(max_length=255)),
                ('avg', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='medprice',
            old_name='med_price',
            new_name='med',
        ),
    ]
