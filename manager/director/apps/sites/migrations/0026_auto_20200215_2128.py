# Generated by Django 2.2.10 on 2020-02-16 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0025_auto_20200213_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dockerimageextrapackage',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
