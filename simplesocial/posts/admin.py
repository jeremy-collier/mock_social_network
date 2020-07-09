from django.contrib import admin
from . import models
# Register your models here.

#this class defines the order in which Post is orderd on the Admin page
class PostAdmin(admin.ModelAdmin):
    fields = ['group','user','message']

    search_fields = ['message']

    list_filter = ['group','user']

    list_display = ['message','user','group']

    # list_editable = ['message']
    #
    # list_display_links = ['user']

admin.site.register(models.Post,PostAdmin)
