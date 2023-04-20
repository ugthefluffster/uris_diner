# Generated by Django 4.1.7 on 2023-04-20 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_category_image_category_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image_Url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(limit_choices_to={'is_deleted': False}, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='dish',
            name='image_Url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
