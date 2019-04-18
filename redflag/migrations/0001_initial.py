# Generated by Django 2.2 on 2019-04-18 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Redflag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redflag_title', models.CharField(max_length=100)),
                ('redflag_comment', models.TextField()),
                ('redflag_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('redflag_status', models.CharField(default='pending', max_length=200)),
                ('redflag_image', models.TextField()),
                ('redflag_video', models.TextField()),
                ('redflag_location', models.CharField(max_length=200)),
                ('redflag_createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='redflag', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
