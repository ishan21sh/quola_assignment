# Generated by Django 5.0 on 2023-12-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_id_card_id_card_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='id_card',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='id_card',
            name='date_of_expiry',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='id_card',
            name='date_of_issue',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='id_card',
            name='identification_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='id_card',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='id_card',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]