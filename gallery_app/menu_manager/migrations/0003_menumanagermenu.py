# Generated by Django 4.2.16 on 2024-09-09 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_manager', '0002_alter_menu_name_alter_menuitem_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuManagerMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('parent_menu_id', models.IntegerField(default=-1)),
            ],
        ),
    ]
