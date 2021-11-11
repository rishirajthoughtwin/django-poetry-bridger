# Generated by Django 3.2.8 on 2021-10-27 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('student_details', models.TextField()),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
