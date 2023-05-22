

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0009_auto_20200323_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famous',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.Flights'),
        ),
        migrations.AlterField(
            model_name='flights',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.Flights'),
        ),
        migrations.DeleteModel(
            name='city',
        ),
    ]
