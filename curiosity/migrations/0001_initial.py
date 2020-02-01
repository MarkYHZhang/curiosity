# Generated by Django 3.0.2 on 2020-01-31 04:03

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000, verbose_name='title')),
                ('answer', markdownx.models.MarkdownxField()),
                ('pub_date', models.DateField(verbose_name='date')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
