# Generated by Django 3.0.6 on 2020-05-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
