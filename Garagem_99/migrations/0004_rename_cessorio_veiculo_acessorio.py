# Generated by Django 4.2.4 on 2023-09-01 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Garagem_99', '0003_rename_foto_veiculo_capa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veiculo',
            old_name='cessorio',
            new_name='acessorio',
        ),
    ]
