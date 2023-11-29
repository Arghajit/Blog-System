# Generated by Django 4.0 on 2023-11-29 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertypes', '0002_alter_user_address_alter_user_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(upload_to='blogs')),
                ('category', models.CharField(default='', max_length=30)),
                ('summary', models.CharField(default='', max_length=100)),
                ('content', models.CharField(default='', max_length=100)),
                ('url', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
