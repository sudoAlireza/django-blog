# Generated by Django 3.2.5 on 2021-08-02 17:06

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True),
        ),
    ]
