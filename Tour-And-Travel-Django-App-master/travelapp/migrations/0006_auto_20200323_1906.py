

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0005_famous_flights_hotels'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flights',
            old_name='price',
            new_name='bprice',
        ),
        migrations.AddField(
            model_name='flights',
            name='eprice',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hotels',
            name='amenities',
            field=models.CharField(default=' ', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotels',
            name='distfromap',
            field=models.IntegerField(null=True),
        ),
    ]
