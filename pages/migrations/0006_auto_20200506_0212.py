# Generated by Django 3.0.6 on 2020-05-06 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20200505_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_method',
            field=models.CharField(max_length=50),
        ),
    ]