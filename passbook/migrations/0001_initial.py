# Generated by Django 2.1.5 on 2019-01-27 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Passbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txDate', models.DateTimeField(auto_now_add=True)),
                ('txId', models.CharField(max_length=100)),
                ('txtype', models.CharField(max_length=10)),
                ('txAmount', models.DecimalField(decimal_places=3, max_digits=50)),
                ('passbookOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
