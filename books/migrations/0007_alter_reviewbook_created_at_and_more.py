# Generated by Django 5.1.1 on 2024-09-26 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_author_the_book_alter_book_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewbook',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='reviewbook',
            name='text_review',
            field=models.TextField(db_index=True, null=True),
        ),
    ]
