# Generated by Django 4.2 on 2023-09-19 08:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_visitor_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visitor',
            name='blog_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
