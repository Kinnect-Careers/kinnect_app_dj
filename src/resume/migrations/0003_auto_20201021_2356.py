# Generated by Django 2.1.15 on 2020-10-21 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20201021_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='ended_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
