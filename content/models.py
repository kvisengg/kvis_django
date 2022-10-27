from django.db import models


class AboutUs(models.Model):
    heading1 = models.CharField(max_length=2000, default=" ")
    description1 = models.CharField(max_length=2000, default=" ")
    heading2 = models.CharField(max_length=2000, default=" ")
    description2 = models.CharField(max_length=2000, default=" ")
    li_item_heading1 = models.CharField(max_length=2000, default=" ")
    li_item_description1 = models.CharField(max_length=2000, default=" ")
    li_item_heading2 = models.CharField(max_length=2000, default=" ")
    li_item_description2 = models.CharField(max_length=2000, default=" ")
    description = models.CharField(max_length=3000, default=" ")
    image_url = models.CharField(max_length=3000, default=" ")
    # def __init__(self, *args, **kwargs):
    #     return self.heading1

    @property
    def has_image(self):
        return True if len(self.image_url) > 2 else False


class ProjectComplete(models.Model):
    happy_clients = models.IntegerField(default=20)
    projects = models.IntegerField(default=20)
    total_hours = models.IntegerField(default=20)
    total_workers = models.IntegerField(default=20)


class Product(models.Model):
    product_name = models.CharField(max_length=1000, default="")
    product_description = models.CharField(max_length=1000, default="")


class Reviews(models.Model):
    user_name = models.CharField(max_length=255)
    user_position = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    image = models.CharField(max_length=255)
