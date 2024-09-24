# Generated by Django 5.1.1 on 2024-09-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("knowledge_bank", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.CharField(
                choices=[
                    ("How To", "How To"),
                    ("Discussion", "Discussion"),
                    ("Announcement", "Announcement"),
                    ("Social", "Social"),
                    ("Other", "Other"),
                ],
                default="info",
                max_length=12,
            ),
            preserve_default=False,
        ),
    ]
