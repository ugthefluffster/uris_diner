# Generated by Django 4.1.7 on 2023-04-20 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_category_image_url_alter_dish_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]