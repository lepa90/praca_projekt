# Generated by Django 3.2.10 on 2022-09-19 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('category', models.PositiveSmallIntegerField(choices=[(1, 'normal'), (2, 'ulgowy'), (3, 'premium'), (4, 'premiumplus')])),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('places', models.ManyToManyField(to='ideass.Place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]