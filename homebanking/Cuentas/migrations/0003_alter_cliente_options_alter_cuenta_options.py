# Generated by Django 4.1 on 2022-08-25 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_auditoriacuenta_movimientos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='cuenta',
            options={'managed': True},
        ),
    ]