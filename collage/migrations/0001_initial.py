# Generated by Django 3.0.1 on 2020-01-05 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=40)),
                ('msg', models.TextField()),
                ('crDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
