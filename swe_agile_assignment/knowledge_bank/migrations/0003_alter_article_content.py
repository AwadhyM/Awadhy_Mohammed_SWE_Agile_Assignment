# Generated by Django 5.1.1 on 2024-09-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("knowledge_bank", "0002_article_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.TextField(max_length=300),
        ),
    ]
