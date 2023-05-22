

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0010_auto_20200323_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='flights',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.City'),
        ),
    ]
