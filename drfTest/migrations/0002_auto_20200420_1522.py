# Generated by Django 3.0.5 on 2020-04-20 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drfTest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created']},
        ),
    ]