# Generated by Django 4.2.4 on 2024-07-09 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pachamodel', '0004_usuario_diasriego_usuario_horariego'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='DiasRiego',
            new_name='diasRiego',
        ),
    ]