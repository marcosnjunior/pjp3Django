# Generated by Django 5.1.2 on 2024-12-01 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fachada', '0009_alter_produto_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens'),
        ),
    ]
