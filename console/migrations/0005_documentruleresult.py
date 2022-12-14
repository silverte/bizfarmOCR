# Generated by Django 4.0.4 on 2022-06-23 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0004_rule_rule_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentRuleResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('SUCCESS', '성공'), ('FAILURE', '실패')], default='FAILURE', max_length=10)),
                ('message', models.TextField(null=True)),
                ('contract_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.contractdocument')),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.rule')),
            ],
        ),
    ]
