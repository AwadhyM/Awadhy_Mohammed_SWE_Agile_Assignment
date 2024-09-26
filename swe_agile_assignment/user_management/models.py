from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class CustomUser(AbstractUser):
    """
    CustomUser represents each individual user of the application. The class is named
    CustomUser because it is an extension of Django's built in User class.

    This class inherits from AbstractUser class and thus contains all of Django's
    built in User class attributes such as Username.

    """

    valid_offices = [
        ("CAM", "Cambridge"),
        ("MANC", "Manchester"),
        ("SHEF", "Sheffield"),
        ("BRIS", "Bristol"),
    ]

    valid_roles = [
        ("Apprentice Software Engineer", "AP"),
        ("Software Engineer", "SWE"),
        ("Senior Software Engineer", "SR"),
        ("Staff Software Engineer", "ST"),
    ]
    first_name = models.CharField(max_length=25, blank=False, null=False)
    second_name = models.CharField(max_length=25, blank=False, null=False)
    joining_date = models.DateTimeField(auto_now_add=True)
    bio = models.CharField(max_length=250, default="User hasn't written a bio yet!")
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    office = models.CharField(max_length=4, choices=valid_offices)
    role = models.CharField(max_length=50, choices=valid_roles)

    def __save__(self):
        """Overrides default save method."""
        super().save()

        img = Image.open(self.image.path)
        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)
