# Generated by Django 2.1.7 on 2019-03-12 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20190312_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='picture',
        ),
    ]