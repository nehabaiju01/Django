

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbworldapp', '0002_auto_20201029_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='nursery_name',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='manager',
            name='profile_image',
            field=models.ImageField(default='herbworldapp/images/', null=True, upload_to='herbworldapp/images/'),
        ),
    ]
