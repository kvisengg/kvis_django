# Generated by Django 4.1.2 on 2022-10-23 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_aboutus_description_alter_aboutus_description2'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image_url',
            field=models.CharField(default=' ', max_length=300),
        ),
    ]