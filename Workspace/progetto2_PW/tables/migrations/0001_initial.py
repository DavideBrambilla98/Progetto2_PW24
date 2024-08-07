# Generated by Django 5.0.7 on 2024-07-27 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CittadinoTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cognome', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=20)),
                ('nasLuogo', models.CharField(max_length=20)),
                ('nasRegione', models.CharField(max_length=20)),
                ('nasProv', models.CharField(max_length=4)),
                ('nasCap', models.CharField(max_length=7)),
                ('dataNascita', models.DateField()),
                ('codFiscale', models.CharField(max_length=50)),
                ('resLuogo', models.CharField(max_length=50)),
                ('resRegione', models.CharField(max_length=50)),
                ('resProv', models.CharField(max_length=4)),
                ('resCap', models.CharField(max_length=7)),
                ('indirizzo', models.CharField(max_length=60)),
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
            name='OspedaleTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codiceStruttura', models.CharField(max_length=10)),
                ('denominazioneStruttura', models.CharField(max_length=50)),
                ('indirizzo', models.CharField(max_length=50)),
                ('comune', models.CharField(max_length=50)),
                ('descrizioneTipoStruttura', models.CharField(max_length=50)),
                ('direttoreSanitario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.cittadinotable')),
            ],
        ),
        migrations.CreateModel(
            name='RicoveroTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codiceRicovero', models.CharField(max_length=20, unique=True)),
                ('data', models.DateField()),
                ('durata', models.IntegerField()),
                ('motivo', models.CharField(max_length=50)),
                ('costo', models.IntegerField()),
                ('codiceOspedale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.ospedaletable')),
                ('paziente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.cittadinotable')),
            ],
        ),
        migrations.CreateModel(
            name='PatologiaRicoveroTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codOspedale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.ospedaletable')),
                ('codPatologia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.patologiatable')),
                ('codRicovero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.ricoverotable')),
            ],
        ),
    ]
