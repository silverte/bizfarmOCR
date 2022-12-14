# Generated by Django 4.0.4 on 2022-06-23 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0002_documentrulevalue_rule'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentrulevalue',
            name='review_document',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='console.reviewdocument'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documentrulevalue',
            name='rule',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='console.rule'),
            preserve_default=False,
        ),
    ]
