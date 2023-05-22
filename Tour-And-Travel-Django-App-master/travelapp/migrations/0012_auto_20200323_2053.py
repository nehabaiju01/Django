

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0011_auto_20200323_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famous',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.City'),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.City'),
        ),
    ]
