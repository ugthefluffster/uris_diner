# Generated by Django 4.1.7 on 2023-04-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_dish_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
