# Generated by Django 5.0.4 on 2024-04-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_ordermodel_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='number',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]