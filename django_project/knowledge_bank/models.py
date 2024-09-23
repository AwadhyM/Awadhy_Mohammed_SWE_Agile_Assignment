from django.db import models
from django.contrib.auth.models import User
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

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # on_delete argument allows post to be deleted if a user is deleted but not vice versa.

    def __str__(self):
        """Displays model instance attributes in human readable form"""
        return f"{self.title} by {self.author} published on {self.date_posted} and last_modified {self.last_modified}"

    def get_absolute_url(self):
        """Gives us path to ArticleDetail route"""
        return reverse("article-detail", kwargs={"pk": self.pk})


class Profile(models.Model):
    """
    Profile stores biographical information of a user.

    This model has a one to one relationship with Django's default User model.

    Attributes:
        user : User
                        A one-to-one relationship with the User model.

        first_name: str
                        The users first name.

                second_name: str
                        The usrs second name.

        bio: str
                        A short description of the user.

        role: (str,str)
                        The users job role

        image: str
                        Stores path to user's profile image. If none uploaded then default is used.

        office: (str,str)
                        The office that the user is based in.
    """

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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, null=True, blank=True, default=None)
    second_name = models.CharField(max_length=25, null=True, blank=True, default=None)
    bio = models.CharField(max_length=250)
    role = models.CharField(max_length=4, choices=valid_roles, default="SWE")
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    office = models.CharField(max_length=4, choices=valid_offices)

    def __save__(self):
        """Overrides default save method."""
        super().save()

        img = Image.open(self.image.path)
        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)
