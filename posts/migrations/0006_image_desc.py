# Generated by Django 3.0.5 on 2020-04-24 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200422_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]