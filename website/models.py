from django.db import models

# Create your models here.

# Item model
class Item(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    inv = models.IntegerField()
    sale = models.DecimalField(max_digits=2,decimal_places=2)
    desc = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8 ,decimal_places=2)
    food_type = models.CharField(max_length=50)
    food_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return(f"{self.name}")