# Generated by Django 5.0.7 on 2024-07-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatologiaTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100)),
                ('codice', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=120)),
                ('criticita', models.CharField(max_length=20)),
                ('cronica', models.CharField(max_length=1)),
                ('mortale', models.CharField(max_length=1)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
