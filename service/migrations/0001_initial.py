# Generated by Django 4.0.2 on 2022-03-09 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import service.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.CharField(default=service.models.generate_uuid_hex, max_length=250, primary_key=True, serialize=False)),
                ('type', models.CharField(default='author', max_length=125)),
                ('displayName', models.CharField(max_length=255, unique=True)),
                ('url', models.URLField(max_length=250)),
                ('host', models.URLField(max_length=250)),
                ('github', models.URLField(max_length=250)),
                ('profileImage', models.URLField(blank=True, max_length=250, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadedDate', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(max_length=500, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(default=service.models.generate_uuid_hex, max_length=250, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('type', models.CharField(default='post', max_length=125)),
                ('description', models.CharField(max_length=500)),
                ('source', models.URLField(max_length=250)),
                ('origin', models.CharField(max_length=250)),
                ('contentType', models.CharField(choices=[('text/markdown', 'text/markdown'), ('text/plain', 'text/plain'), ('application/base64', 'application/base64'), ('image/png;base64', 'image/png;base64'), ('image/jpeg;base64', 'image/jpeg;base64')], default='text/plain', max_length=50)),
                ('imageSource', models.URLField(blank=True, max_length=500, null=True)),
                ('publishedDate', models.DateTimeField(auto_now=True, max_length=250)),
                ('visibility', models.CharField(choices=[('PUBLIC', 'Public'), ('FRIENDS', 'Friends-Only'), ('PRIVATE', 'Private'), ('AUTHORIZED', 'Authorized users')], default='PUBLIC', max_length=25)),
                ('unlisted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.author')),
                ('categories', models.ManyToManyField(to='service.Category')),
            ],
        ),
        migrations.CreateModel(
            name='InboxObject',
            fields=[
                ('id', models.CharField(default=service.models.generate_uuid_hex, editable=False, max_length=250, primary_key=True, serialize=False)),
                ('object_id', models.CharField(max_length=250, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.author')),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='FollowRequest',
            fields=[
                ('id', models.CharField(default=service.models.generate_uuid_hex, max_length=250, primary_key=True, serialize=False)),
                ('summary', models.CharField(max_length=500)),
                ('type', models.CharField(default='Follow', max_length=125)),
                ('actor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='actor', to='service.author')),
                ('object', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='obj', to='service.author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('type', models.CharField(default='comment', max_length=100)),
                ('id', models.CharField(default=service.models.generate_uuid_hex, max_length=250, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=500, null=True)),
                ('contentType', models.CharField(default='text/plain', max_length=50)),
                ('publishedDate', models.DateTimeField(auto_now=True, max_length=250)),
                ('url', models.URLField(max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.author')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.post')),
            ],
        ),
    ]
