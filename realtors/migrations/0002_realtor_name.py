# Generated by Django 2.1.1 on 2019-08-28 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='name',
            field=models.CharField(default=312, max_length=200),
            preserve_default=False,
        ),
    ]
