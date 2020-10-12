from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,name):
        cls.objects.filter(name = name).delete()

    def update_category(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)

class Location(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,name):
        cls.objects.filter(name = name).delete()

   
    def update_location(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)   

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()
    image_category = models.ForeignKey(Category,on_delete = models.CASCADE)
    image_location = models.ForeignKey(Location,on_delete = models.CASCADE)


    def save_image(self):
        self.save()

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete() 

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(image_category__name__contains = search_term)
        return images

    
