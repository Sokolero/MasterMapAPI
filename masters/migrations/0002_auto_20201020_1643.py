# Generated by Django 3.1.2 on 2020-10-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='master',
            name='categorys',
            field=models.ManyToManyField(to='masters.Category'),
        ),
    ]
