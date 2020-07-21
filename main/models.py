from django.db import models

# Create your models here.


DIFFICULTY = (
    ('Hard','Hard'),
    ('Medium','Medium'),
    ('Easy','Easy'),
)
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    preparation_time = models.IntegerField(null=True, default=1) 
    cook_time = models.IntegerField(null=True, default=1) 
    difficulty = models.CharField(null=True, choices=DIFFICULTY, max_length=100)
    image = models.ImageField(upload_to='recipes_img/', null=True, blank=True, )
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.recipe_name


