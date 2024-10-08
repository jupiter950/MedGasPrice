# Generated by Django 5.0.3 on 2024-03-22 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socketapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_price', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='gasdata',
            old_name='burnedFees',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='gasdata',
            old_name='cfrom',
            new_name='price_date',
        ),
        migrations.RemoveField(
            model_name='gasdata',
            name='blockNumber',
        ),
        migrations.RemoveField(
            model_name='gasdata',
            name='chainId',
        ),
        migrations.RemoveField(
            model_name='gasdata',
            name='fto',
        ),
        migrations.RemoveField(
            model_name='gasdata',
            name='gasPrice',
        ),
        migrations.RemoveField(
            model_name='gasdata',
            name='index',
        ),
        migrations.RemoveField(
            model_name='gasdata',
            name='status',
        ),
        migrations.RemoveField(
            model_name='gasdata',
            name='tid',
        ),
        migrations.RemoveField(
            model_name='gasdata',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='gasdata',
            name='value',
        ),
    ]
