# Generated by Django 3.1.7 on 2021-03-21 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import recipe_blog.recipe.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredients', '0002_auto_20210321_1337'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0002_auto_20210316_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('instruction', models.TextField()),
                ('time_minutes', models.PositiveIntegerField()),
                ('image', models.ImageField(null=True, upload_to=recipe_blog.recipe.models.recipe_image_file_path)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(to='categories.Category')),
                ('ingredients', models.ManyToManyField(to='ingredients.Ingredient')),
            ],
        ),
    ]