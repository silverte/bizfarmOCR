# Generated by Django 4.0.4 on 2022-06-23 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentRuleValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value1', models.CharField(blank=True, max_length=100, null=True)),
                ('value2', models.CharField(blank=True, max_length=100, null=True)),
                ('value3', models.CharField(blank=True, max_length=100, null=True)),
                ('value4', models.CharField(blank=True, max_length=100, null=True)),
                ('value5', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_name', models.CharField(error_messages={'unique': '이미 등록된 규칙입니다.'}, max_length=30, unique=True)),
                ('rule_type', models.CharField(choices=[('PERIOD', '기간'), ('CODE', '코드')], default=None, max_length=10)),
                ('rule_type_value', models.CharField(blank=True, max_length=50, null=True)),
                ('rule_class', models.CharField(max_length=30)),
            ],
        ),
    ]
