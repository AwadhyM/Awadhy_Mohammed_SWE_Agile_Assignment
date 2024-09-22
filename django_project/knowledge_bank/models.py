from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    """Article represents the article table in our database.
    This is the data that users will be able to add, update and read.
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


class Profile(models.Model):
    """
    Profile stores biographical information of a user.

    This model has a one to one relationship with Django's default User model.

    Attributes:
        user (User): A one-to-one relationship with the User model.
        bio: A short description of the user.
        image: Stores the users profile image. If none uploaded then default is used.
        office: The office that the user is based in.
    """

    valid_offices = [
        ("CAM", "Cambridge"),
        ("MANC", "Manchester"),
        ("SHEF", "Sheffield"),
        ("BRIS", "Bristol"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    office = models.CharField(max_length=4, choices=valid_offices)
