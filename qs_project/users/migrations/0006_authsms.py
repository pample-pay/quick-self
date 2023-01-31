# Generated by Django 4.1.5 on 2023-01-10 08:49

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_delete_authsms'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthSMS',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('hp', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='휴대폰번호')),
                ('auth', models.IntegerField(verbose_name='인증번호')),
            ],
            options={
                'db_table': 'AUTH_TB',
            },
        ),
    ]
