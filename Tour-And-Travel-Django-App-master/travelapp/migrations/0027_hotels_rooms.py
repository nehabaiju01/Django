

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0026_bookhotel_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='rooms',
            field=models.IntegerField(default=0),
        ),
    ]
