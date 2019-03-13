# Generated by Django 2.1.7 on 2019-03-13 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-date_added']},
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='book_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Date Added'),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='book_topic',
            field=models.ManyToManyField(related_name='book_topics', to='core.Topic'),
        ),
    ]
