# Generated by Django 4.0.5 on 2022-06-08 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_remove_detailstory_type_remove_detailstory_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DetailStory',
        ),
        migrations.DeleteModel(
            name='TopStories',
        ),
    ]
