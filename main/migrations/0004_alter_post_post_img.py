# Generated by Django 4.1.3 on 2022-11-27 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_category_category_slug_alter_post_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
