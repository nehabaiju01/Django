

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0024_bookflight_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookpackage',
            name='seat',
            field=models.IntegerField(default=1),
        ),
    ]
