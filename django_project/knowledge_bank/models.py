from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from PIL import Image


class Article(models.Model):
    """

        Article represents knowledge article that is published by a user.

    Attributes:
        title : str
                        Title of article.

        content: str
                        Content of article.

                date_posted: DateTimeField
                        Date and time of creation.

        last_modified: DateTimeField
                        Date and time of article modification.

        author: User
                        The user who published the article.
    """

    choice_categories = [
        ("How To", "How To"),
        ("Discussion", "Discussion"),
        ("Announcement", "Announcement"),
        ("Social", "Social"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # on_delete argument allows post to be deleted if a user is deleted but not vice versa.
    category = models.CharField(max_length=12, choices=choice_categories)

    def __str__(self):
        """Displays model instance attributes in human readable form"""
        return f"{self.title} by {self.author} published on {self.date_posted} and last_modified {self.last_modified}"

    def get_absolute_url(self):
        """Gives us path to ArticleDetail route"""
        return reverse("article-detail", kwargs={"pk": self.pk})
