# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0007_user_relationships'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(max_digits=64, decimal_places=2)),
                ('trial_period', models.PositiveIntegerField(null=True, blank=True)),
                ('trial_unit', models.CharField(blank=True, max_length=1, null=True, choices=[(b'D', 'Day'), (b'W', 'Week'), (b'M', 'Month'), (b'Y', 'Year')])),
                ('recurrence_period', models.PositiveIntegerField(null=True, blank=True)),
                ('recurrence_unit', models.CharField(blank=True, max_length=1, null=True, choices=[(b'D', 'Day'), (b'W', 'Week'), (b'M', 'Month'), (b'Y', 'Year')])),
                ('group', models.ForeignKey(to='auth.Group')),
            ],
            options={
                'ordering': ('price', '-recurrence_period'),
            },
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expires', models.DateField(default=datetime.date.today, null=True)),
                ('active', models.BooleanField(default=True)),
                ('cancelled', models.BooleanField(default=True)),
                ('subscription', models.ForeignKey(to='subscription.Subscription')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='usersubscription',
            unique_together=set([('user', 'subscription')]),
        ),
    ]
