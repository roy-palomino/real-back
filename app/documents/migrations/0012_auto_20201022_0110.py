# Generated by Django 3.1.2 on 2020-10-22 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0011_auto_20201022_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='author',
            field=models.ManyToManyField(default='Unknown', to='documents.Author'),
        ),
    ]