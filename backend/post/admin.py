from django.contrib import admin
from post.models import ModelPost

# Register your models here.
@admin.register(ModelPost)
class AdminModelPost(admin.ModelAdmin):
     list_display = ('title',)
     list_filter = ('title',)




