# Generated by Django 4.1.2 on 2022-11-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_correspondencia_conserje_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='estado',
            field=models.CharField(choices=[('No Recibido', 'No recibido'), ('Recibido', 'Recibido')], default='No Recibido', max_length=15),
        ),
    ]