# Generated by Django 3.1.5 on 2021-01-24 10:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=20)),
                ('upper_limit', models.IntegerField()),
            ],
            options={
                'db_table': 'itemcategory',
            },
        ),
        migrations.CreateModel(
            name='AllBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calc_method', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
                ('date_of_use', models.CharField(default='2021-01-24 19:05:54', max_length=19, verbose_name='使用日')),
                ('date_of_regist', models.CharField(default='2021-01-24 19:05:54', max_length=19, verbose_name='登録日')),
                ('item_num', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='moneybook.itemcategory')),
            ],
            options={
                'db_table': 'allbook',
            },
        ),
    ]