# Generated by Django 5.1.4 on 2024-12-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiryform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiryform',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
    ]
