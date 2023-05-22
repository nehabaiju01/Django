

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0006_auto_20200323_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='company',
            field=models.CharField(default=' ', max_length=15),
        ),
    ]
