

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0021_bookhotel_bookpackage'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='seats',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
