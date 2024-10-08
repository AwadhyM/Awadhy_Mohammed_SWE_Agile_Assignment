# Generated by Django 5.1.1 on 2024-09-25 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("knowledge_bank", "0004_alter_article_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="category",
            field=models.CharField(
                choices=[
                    ("How To", "How To"),
                    ("Info", "Info"),
                    ("Discussion", "Discussion"),
                    ("Announcement", "Announcement"),
                    ("Social", "Social"),
                    ("Other", "Other"),
                ],
                max_length=12,
            ),
        ),
    ]
