# Generated by Django 4.0.6 on 2022-07-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0013_alter_colors_owner_alter_thing_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thing',
            name='group',
        ),
        migrations.AddField(
            model_name='thing',
            name='mass',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
