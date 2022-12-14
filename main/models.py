from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    category_slug = models.SlugField(null=True, blank=True)


    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):  # new
        if not self.category_slug:
            self.category_slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=100)
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_content = RichTextField(blank=True, null=True)
    # post_content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    post_slug = models.SlugField()
    post_img = models.ImageField(null=True, blank=True, upload_to="images/")




    def __str__(self):
        return self.title