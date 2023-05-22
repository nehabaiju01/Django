

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0025_bookpackage_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookhotel',
            name='room',
            field=models.IntegerField(default=1),
        ),
    ]
