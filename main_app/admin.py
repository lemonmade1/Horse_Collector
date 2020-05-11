from django.contrib import admin
from .models import Horse, Feeding, Toy, Photo

# Register your models here.
admin.site.register(Horse)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)
