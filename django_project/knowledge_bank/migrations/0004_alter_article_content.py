# Generated by Django 5.1.1 on 2024-09-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("knowledge_bank", "0003_alter_article_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.TextField(max_length=800),
        ),
    ]
