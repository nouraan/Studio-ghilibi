# Generated by Django 3.2.8 on 2021-10-08 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0005_auto_20211008_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='peaople',
            name='MyMovies',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Movies.mymovies'),
            preserve_default=False,
        ),
    ]