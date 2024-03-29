# Generated by Django 2.2.14 on 2021-02-08 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210205_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Searches',
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear'), ('M', 'Monitor'), ('L', 'Laptop'), ('E', 'Earphone')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
