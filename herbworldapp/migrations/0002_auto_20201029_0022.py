

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbworldapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='herbworldapp/images/', null=True, upload_to='herbworldapp/images/'),
        ),
    ]
