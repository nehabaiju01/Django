

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0027_hotels_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookpackage',
            name='room',
            field=models.IntegerField(default=1),
        ),
    ]
