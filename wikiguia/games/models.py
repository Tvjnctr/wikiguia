from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    def __str__(self):
        return self.name
