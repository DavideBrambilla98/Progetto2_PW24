# Generated by Django 5.0.7 on 2024-07-21 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OspedaleTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codiceStruttura', models.CharField(max_length=10)),
                ('denominazioneStruttura', models.CharField(max_length=50)),
                ('indirizzo', models.CharField(max_length=50)),
                ('comune', models.CharField(max_length=50)),
                ('descrizioneTipoStruttura', models.CharField(max_length=50)),
                ('direttoreSanitario', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PatologiaTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codice', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=120)),
                ('criticita', models.CharField(max_length=20)),
                ('cronica', models.CharField(max_length=1)),
                ('mortale', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='RicoveroTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codiceOspedale', models.CharField(max_length=10)),
                ('codiceRicovero', models.CharField(max_length=20)),
                ('paziente', models.CharField(max_length=20)),
                ('data', models.DateField()),
                ('durata', models.IntegerField()),
                ('motivo', models.CharField(max_length=50)),
                ('costo', models.IntegerField()),
            ],
        ),
    ]
