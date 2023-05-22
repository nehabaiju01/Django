

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('travelapp', '0002_auto_20200323_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('flight_num', models.CharField(max_length=10)),
                ('price', models.IntegerField(null=True)),
                ('dept_time', models.TimeField()),
                ('dest_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=200)),
                ('hotel_address', models.CharField(max_length=500)),
                ('hotel_price', models.IntegerField(null=True)),
                ('hotel_rating', models.IntegerField(null=True)),
                ('image1', models.ImageField(null=True, upload_to='img/')),
                ('image2', models.ImageField(null=True, upload_to='img/')),
                ('image3', models.ImageField(null=True, upload_to='img/')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.Flights')),
            ],
        ),
        migrations.CreateModel(
            name='Famous',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='img/')),
                ('desc', models.CharField(max_length=500)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.Flights')),
            ],
        ),
    ]
