

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herbworldapp', '0004_auto_20201029_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='description',
            new_name='address',
        ),
    ]
