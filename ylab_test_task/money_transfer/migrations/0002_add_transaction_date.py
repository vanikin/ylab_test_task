from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('money_transfer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ('-date',)},
        ),
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Transaction time'),
        ),
    ]
