# Generated by Django 3.2.12 on 2025-02-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon_store', '0002_auto_20250218_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='path/to/upload/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='path/to/upload/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='path/to/upload/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='path/to/upload/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='path/to/upload/'),
        ),
    ]
