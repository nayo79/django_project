# Generated by Django 3.0.3 on 2020-03-17 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
