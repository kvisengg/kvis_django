from django.db import models


class AboutUs(models.Model):
    heading1 = models.CharField(max_length=200, default=" ")
    description1 = models.CharField(max_length=200, default=" ")
    heading2 = models.CharField(max_length=200, default=" ")
    description2 = models.CharField(max_length=200, default=" ")
    li_item_heading1 = models.CharField(max_length=200, default=" ")
    li_item_description1 = models.CharField(max_length=200, default=" ")
    li_item_heading2 = models.CharField(max_length=200, default=" ")
    li_item_description2 = models.CharField(max_length=200, default=" ")
    description = models.CharField(max_length=300, default=" ")
    image_url = models.CharField(max_length=300, default=" ")
    # def __init__(self, *args, **kwargs):
    #     return self.heading1

    @property
    def has_image(self):
        return True if len(self.image_url) >2 else False
