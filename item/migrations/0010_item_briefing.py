# Generated by Django 4.2.6 on 2023-10-28 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_item_price_currency_alter_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='briefing',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
