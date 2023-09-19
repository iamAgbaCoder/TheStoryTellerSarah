# Generated by Django 4.2 on 2023-09-14 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_visitor_delete_peoplewhovistedyoursite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='blog_post',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='city',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='country',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
    ]