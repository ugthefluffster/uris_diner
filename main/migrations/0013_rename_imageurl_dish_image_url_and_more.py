# Generated by Django 4.1.7 on 2023-04-12 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_dish_image_dish_imageurl_alter_dish_imagefile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='imageUrl',
            new_name='image_Url',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='imagefile',
            new_name='image_file',
        ),
    ]
