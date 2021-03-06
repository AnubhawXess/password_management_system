# Generated by Django 3.0.4 on 2020-07-31 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a website or application name (e.g. Github, Desktop)', max_length=200)),
                ('link', models.URLField(blank=True, help_text='(optional) Enter a link to the website (e.g. <a href="http://www.example.com">http://www.example.com</a>')),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('account_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
