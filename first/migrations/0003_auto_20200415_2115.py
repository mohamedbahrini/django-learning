# Generated by Django 3.0.4 on 2020-04-15 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_auto_20200415_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='book title', max_length=36, unique=True),
        ),
    ]