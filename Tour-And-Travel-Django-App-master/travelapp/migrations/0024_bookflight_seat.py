

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0023_remove_flights_bprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookflight',
            name='seat',
            field=models.IntegerField(default=1),
        ),
    ]
