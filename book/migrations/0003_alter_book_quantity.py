# Generated by Django 4.0.4 on 2022-05-14 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
