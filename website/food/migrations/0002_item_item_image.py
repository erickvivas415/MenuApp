# Generated by Django 4.2 on 2023-05-04 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='http://www.ukvisitorguide.cn/wp-content/uploads/2015/11/Food-placeholder.jpg', max_length=500),
        ),
    ]
