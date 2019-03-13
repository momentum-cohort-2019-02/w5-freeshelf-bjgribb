# Generated by Django 2.1.7 on 2019-03-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20190313_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='topic',
        ),
        migrations.AddField(
            model_name='book',
            name='book_topic',
            field=models.ManyToManyField(to='core.Topic'),
        ),
    ]
