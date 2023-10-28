# Generated by Django 4.2.6 on 2023-10-26 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_remove_item_image_url_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.AddField(
            model_name='item',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]