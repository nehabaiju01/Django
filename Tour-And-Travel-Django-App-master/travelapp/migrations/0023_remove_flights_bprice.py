

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0022_flights_seats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flights',
            name='bprice',
        ),
    ]
