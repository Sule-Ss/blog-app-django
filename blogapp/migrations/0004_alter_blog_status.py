# Generated by Django 4.0.4 on 2022-06-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[(None, 'status'), ('published', 'published'), ('draft', 'draft')], max_length=200),
        ),
    ]