# Generated by Django 5.0.6 on 2024-07-01 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clube', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogador',
            name='anos',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
