# Generated by Django 5.0.4 on 2024-04-12 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_ordermodel_date_remove_ordermodel_picture_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='warehouse',
            new_name='list_warehouse',
        ),
    ]
