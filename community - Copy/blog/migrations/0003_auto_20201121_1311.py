# Generated by Django 3.1.3 on 2020-11-21 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201119_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dlike',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=34),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=77),
        ),
    ]
