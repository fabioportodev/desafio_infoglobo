# Generated by Django 3.0.2 on 2020-01-13 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200113_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='stream',
            field=models.CharField(max_length=10),
        ),
    ]
