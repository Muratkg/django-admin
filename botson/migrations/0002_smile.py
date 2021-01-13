# Generated by Django 3.1.5 on 2021-01-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botson', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(blank=True, max_length=100, null=True)),
                ('user_name', models.CharField(blank=True, max_length=100, null=True)),
                ('before', models.TextField(default='')),
                ('after', models.TextField(default='')),
                ('publication', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
