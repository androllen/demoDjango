# Generated by Django 2.0.6 on 2020-05-06 18:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='经验名称')),
                ('description', models.CharField(default='', max_length=200, verbose_name='经验描述')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('source', models.SmallIntegerField(choices=[(1, '系统'), (2, '手动')], default=1, verbose_name='经验来源')),
            ],
            options={
                'db_table': 'experience',
            },
        ),
    ]
