

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbworldapp', '0003_auto_20201029_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
