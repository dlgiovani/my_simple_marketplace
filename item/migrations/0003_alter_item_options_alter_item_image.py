# Generated by Django 4.2.3 on 2023-08-09 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name_plural': 'Items'},
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='item_images'),
        ),
    ]
