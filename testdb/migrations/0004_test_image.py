# Generated by Django 4.1.3 on 2022-11-29 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0003_test_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='image',
            field=models.ImageField(default=[], upload_to='images/'),
        ),
    ]