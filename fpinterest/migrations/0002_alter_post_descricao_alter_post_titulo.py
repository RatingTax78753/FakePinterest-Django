# Generated by Django 5.0.6 on 2024-05-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpinterest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='descricao',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]