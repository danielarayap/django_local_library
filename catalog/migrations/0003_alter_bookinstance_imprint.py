# Generated by Django 4.0.3 on 2022-03-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='imprint',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
