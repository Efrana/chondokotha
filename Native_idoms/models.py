from django.db import models


# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=200)
    bn_name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=200)
    bn_name = models.CharField(max_length=200)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    lat = models.CharField(max_length=200, null=True)
    lon = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    br_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Chondokotha(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def category_name(self):
        return self.category.name

    def district_name(self):
        return self.district.name

    def division_name(self):
        return self.district.division.name

    def __str__(self):
        return self.title
