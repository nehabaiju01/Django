

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbworldapp', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_image',
            field=models.ImageField(default='neuroly/profile_images/default.jpg', null=True, upload_to='media/herbworldapp/images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='herbworldapp/images', null=True, upload_to='herbworldapp/images/'),
        ),
    ]
