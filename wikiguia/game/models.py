from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length= 255)
    description = models.TextField(blank=True, null=True)
    description_short = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='game_images', blank=True, null=True)
    carousel_image = models.ImageField(upload_to='game_images/carousel', blank=True, null=True)

    def __str__(self):
        return self.name