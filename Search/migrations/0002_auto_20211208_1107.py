# Generated by Django 3.2.9 on 2021-12-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name_cn',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='league',
            name='name_cn',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='familyname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='familyname_cn',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='firstname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='firstname_cn',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='originname',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='shortname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='shortname_cn',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='yearofbirth',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='playertoteam',
            name='num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='fullname_cn',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='fullname_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='shortname_cn',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='shortname_en',
            field=models.CharField(max_length=10, null=True),
        ),
    ]