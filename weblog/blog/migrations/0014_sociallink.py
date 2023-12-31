# Generated by Django 4.0.6 on 2023-07-31 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_newsletter_subscribed_email_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_media', models.CharField(help_text='e.g Instagram', max_length=10)),
                ('link', models.URLField()),
            ],
        ),
    ]
