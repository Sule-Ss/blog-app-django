# Generated by Django 4.0.4 on 2022-05-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_blog_options_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('status', 'status')], max_length=200),
        ),
    ]
