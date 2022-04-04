# Generated by Django 4.0.2 on 2022-04-02 20:10

from django.db import migrations, models
import service.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_likepost_likecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likecomment',
            name='id',
            field=models.CharField(default=service.models.generate_uuid_hex, max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='likepost',
            name='id',
            field=models.CharField(default=service.models.generate_uuid_hex, max_length=250, primary_key=True, serialize=False),
        ),
    ]
