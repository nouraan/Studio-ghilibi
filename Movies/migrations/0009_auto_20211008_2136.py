# Generated by Django 3.2.8 on 2021-10-08 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0008_peaople_mymovies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymovies',
            old_name='Film1',
            new_name='Film',
        ),
        migrations.RemoveField(
            model_name='mymovies',
            name='Film2',
        ),
        migrations.RemoveField(
            model_name='mymovies',
            name='Film3',
        ),
        migrations.DeleteModel(
            name='Peaople',
        ),
    ]