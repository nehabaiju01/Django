

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0017_auto_20200325_1620'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FlightUser',
        ),
    ]
