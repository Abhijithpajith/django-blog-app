
from django.contrib import admin
from .models import Blogs,Category
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug_field': ('title',)}

class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Blogs,BlogAdmin)
admin.site.register(Category,AdminCategory)
