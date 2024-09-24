from django.db import models
from django.contrib.auth.models import AbstractUser
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
    first_name = models.CharField(max_length=25, blank=False, null=False)
    second_name = models.CharField(max_length=25, blank=False, null=False)
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
