# Generated by Django 4.2.4 on 2023-12-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]