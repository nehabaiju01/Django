

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0012_auto_20200323_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='bestlink',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='weekgetlinks',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
