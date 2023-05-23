

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=50)),
                ('nursery_id', models.CharField(max_length=50)),
                ('customer_id', models.CharField(max_length=50)),
                ('order_total', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('product_id', models.CharField(max_length=50)),
                ('nursery_id', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('product_image', models.ImageField(default='neuroly/profile_images/default.jpg', null=True, upload_to='herbworldapp/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('profile_image', models.ImageField(default='neuroly/profile_images/default.jpg', null=True, upload_to='herbworldapp/images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('profile_image', models.ImageField(default='neuroly/profile_images/default.jpg', null=True, upload_to='herbworldapp/images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
