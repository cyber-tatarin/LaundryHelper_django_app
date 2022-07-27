# Generated by Django 4.0.6 on 2022-07-18 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='title',
            field=models.CharField(default='My thing', max_length=30),
        ),
        migrations.AlterField(
            model_name='thing',
            name='condition',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='thing',
            name='group',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
