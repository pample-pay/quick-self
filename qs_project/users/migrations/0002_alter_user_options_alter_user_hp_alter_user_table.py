# Generated by Django 4.1.5 on 2023-01-10 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'user'},
        ),
        migrations.AlterField(
            model_name='user',
            name='hp',
            field=models.CharField(max_length=15, null=True, unique=True, verbose_name='휴대폰번호'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='USER_TB',
        ),
    ]
