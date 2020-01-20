# Generated by Django 3.0.2 on 2020-01-13 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200113_0606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='musica',
        ),
        migrations.AddField(
            model_name='album',
            name='artista',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.Artista'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musica',
            name='album',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.Album'),
            preserve_default=False,
        ),
    ]
