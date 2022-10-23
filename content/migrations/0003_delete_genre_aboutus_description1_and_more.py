# Generated by Django 4.1.2 on 2022-10-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_genre'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='description1',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='description2',
            field=models.CharField(default=' ', max_length=300),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='heading1',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='heading2',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='li_item_description1',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='li_item_description2',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='li_item_heading1',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='li_item_heading2',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]