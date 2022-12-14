# Generated by Django 4.0.4 on 2022-06-24 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0006_reviewruleresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.review')),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.rule')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewRuleValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value1', models.CharField(blank=True, max_length=100, null=True)),
                ('value2', models.CharField(blank=True, max_length=100, null=True)),
                ('value3', models.CharField(blank=True, max_length=100, null=True)),
                ('value4', models.CharField(blank=True, max_length=100, null=True)),
                ('value5', models.CharField(blank=True, max_length=100, null=True)),
                ('review_rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.reviewrule')),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.rule')),
            ],
        ),
    ]
