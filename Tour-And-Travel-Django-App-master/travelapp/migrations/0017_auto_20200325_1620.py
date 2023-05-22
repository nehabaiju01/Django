

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0016_flightuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightuser',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]
