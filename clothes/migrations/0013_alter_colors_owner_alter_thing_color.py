# Generated by Django 4.0.6 on 2022-07-22 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clothes', '0012_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colors',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thing',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.colors'),
        ),
    ]
