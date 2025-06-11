from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat')], max_length=50)
    age = models.FloatField()
    breed = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='pet_images/')
    owner_name = models.CharField(max_length=50)
    owner_email = models.EmailField()
    owner_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name