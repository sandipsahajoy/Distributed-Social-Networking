# Generated by Django 4.0.2 on 2022-02-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_alter_post_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
