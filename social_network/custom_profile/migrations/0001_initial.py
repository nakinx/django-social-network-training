# Generated by Django 2.0.7 on 2018-07-17 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('birthday_date', models.DateField(verbose_name='YYYY-MM-DD')),
            ],
        ),
    ]