# Generated by Django 2.0.13 on 2020-09-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
