

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0007_flights_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='famous',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.city'),
        ),
        migrations.AlterField(
            model_name='flights',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.city'),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.city'),
        ),
    ]