# Generated by Django 3.0.8 on 2020-07-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('preparation_time', models.IntegerField(default=1, null=True)),
                ('difficulty', models.CharField(choices=[('Hard', 'Hard'), ('Medium', 'Medium'), ('Easy', 'Easy')], max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('published_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
