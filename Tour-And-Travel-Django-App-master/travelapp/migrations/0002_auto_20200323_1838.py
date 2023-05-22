

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
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
