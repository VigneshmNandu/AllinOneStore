# Generated by Django 2.2.14 on 2021-02-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210208_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='search',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]