# Generated by Django 2.2.16 on 2022-10-25 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20221025_1042'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_followers',
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='no_self_following',
        ),
    ]