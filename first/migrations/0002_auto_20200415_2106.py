# Generated by Django 3.0.4 on 2020-04-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(choices=[(0, 'Hobbit'), (1, 'Lord of the ring'), (2, 'book title')], default='book title', max_length=36, unique=True),
        ),
    ]