# Generated by Django 4.1.3 on 2022-11-12 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Category_slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
