# Generated by Django 5.1.4 on 2024-12-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiryform', '0002_alter_enquiryform_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiryform',
            name='mobile',
            field=models.IntegerField(max_length=15),
        ),
    ]
