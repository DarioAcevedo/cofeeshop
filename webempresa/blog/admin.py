from django.contrib import admin
from .models import category, post
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')

class postAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')
    list_display= ('author','title', 'published')
    search_fields= ('title','content')

admin.site.register(category, categoryAdmin)
admin.site.register(post, postAdmin)