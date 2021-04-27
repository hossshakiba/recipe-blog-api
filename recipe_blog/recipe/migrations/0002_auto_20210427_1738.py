# Generated by Django 3.1.7 on 2021-04-27 17:38

from django.db import migrations, models
import django.utils.timezone
import recipe_blog.recipe.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, default=django.utils.timezone.now, upload_to=recipe_blog.recipe.models.recipe_image_file_path),
            preserve_default=False,
        ),
    ]