# Generated by Django 2.1.15 on 2020-10-21 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='institution',
            field=models.CharField(max_length=250),
        ),
    ]