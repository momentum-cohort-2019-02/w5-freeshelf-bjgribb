# Generated by Django 2.1.7 on 2019-03-15 22:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190313_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_topic',
        ),
        migrations.AddField(
            model_name='book',
            name='topic',
            field=models.ManyToManyField(to='core.Topic'),
        ),
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]