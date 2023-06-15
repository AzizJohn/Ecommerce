# Generated by Django 4.2 on 2023-04-17 04:17

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('first_name', models.CharField(max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last_name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=32, region=None, verbose_name='Phone number')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
