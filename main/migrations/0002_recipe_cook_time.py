# Generated by Django 3.0.8 on 2020-07-21 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cook_time',
            field=models.IntegerField(default=1, null=True),
        ),
    ]