

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travelapp', '0019_bookflight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookflight',
            name='username',
        ),
        migrations.AddField(
            model_name='bookflight',
            name='username_id',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
