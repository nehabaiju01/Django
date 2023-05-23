

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbworldapp', '0005_auto_20201029_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=70)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
