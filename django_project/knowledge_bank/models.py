from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from PIL import Image


class CustomUser(AbstractUser):

    valid_offices = [
        ("CAM", "Cambridge"),
        ("MANC", "Manchester"),
        ("SHEF", "Sheffield"),
        ("BRIS", "Bristol"),
    ]

    valid_roles = [
        ("AP", "Apprentice Software Engineer"),
        ("SWE", "Software Engineer"),
        ("SR", "Senior Software Engineer"),
        ("ST", "Staff Software Engineer"),
    ]
    first_name = models.CharField(max_length=25, blank=True, null=True)
    second_name = models.CharField(max_length=25, blank=True, null=True)
    joining_date = models.DateTimeField(auto_now_add=True)
    bio = models.CharField(max_length=250, default="User hasn't written a bio yet!")
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    office = models.CharField(max_length=4, choices=valid_offices)
    role = models.CharField(max_length=4, choices=valid_roles)

    def __save__(self):
        """Overrides default save method."""
        super().save()

        img = Image.open(self.image.path)
        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)


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

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # on_delete argument allows post to be deleted if a user is deleted but not vice versa.

    def __str__(self):
        """Displays model instance attributes in human readable form"""
        return f"{self.title} by {self.author} published on {self.date_posted} and last_modified {self.last_modified}"

    def get_absolute_url(self):
        """Gives us path to ArticleDetail route"""
        return reverse("article-detail", kwargs={"pk": self.pk})
