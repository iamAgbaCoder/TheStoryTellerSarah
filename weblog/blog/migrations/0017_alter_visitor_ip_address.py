# Generated by Django 4.2 on 2023-09-14 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_visitor_blog_post_alter_visitor_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='ip_address',
            field=models.GenericIPAddressField(editable=False),
        ),
    ]
