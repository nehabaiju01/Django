

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_famous_flights_hotels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='city',
        ),
        migrations.DeleteModel(
            name='Famous',
        ),
        migrations.DeleteModel(
            name='Flights',
        ),
        migrations.DeleteModel(
            name='Hotels',
        ),
    ]
