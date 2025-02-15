# Generated by Django 5.1.4 on 2025-01-23 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_add_book', 'Can add a book'), ('can_change_book', 'Can change a book'), ('can_delete_book', 'Can delete a book')]},
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default=1, max_length=13, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=255),
        ),
    ]
