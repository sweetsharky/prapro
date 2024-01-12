# Generated by Django 4.2.7 on 2024-01-07 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('event_type', models.CharField(choices=[('AR', 'Arbeit'), ('FR', 'Freizeit')], default='FR', max_length=2)),
            ],
        ),
    ]
