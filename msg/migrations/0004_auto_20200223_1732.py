# Generated by Django 3.0.3 on 2020-02-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0003_auto_20200223_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.CharField(max_length=200),
        ),
    ]
