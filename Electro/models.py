from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html

# Create your models here.
class Electro(models.Model):
    elctronic_name = models.CharField(max_length=64)
    elctronic_image = models.ImageField(upload_to='Electro/thumbnail/%Y/%m/%d/', null=True, blank=True)
    description = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.elctronic_name
        
    def get_absolute_url(self):
        return reverse("electro_detail", args=[str(self.pk)])

    # @property
    def thumbnail_preview(self):
        if self.elctronic_image:
            _thumbnail = get_thumbnail(self.elctronic_image,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""