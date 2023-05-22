

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0014_auto_20200324_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='hotels',
            name='image3',
        ),
    ]
