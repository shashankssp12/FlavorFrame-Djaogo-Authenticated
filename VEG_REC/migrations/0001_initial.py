from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rname', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('Rimage', models.ImageField(upload_to='ReceipeImages')),
            ],
        ),
    ]