# Generated by Django 5.0 on 2023-12-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_id_image_id_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='ID_CARD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('date_of_issue', models.DateField()),
                ('date_of_expiry', models.DateField()),
                ('id_card_img', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
