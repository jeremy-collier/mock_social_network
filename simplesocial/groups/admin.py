from django.contrib import admin
from . import models
# Register your models here.
#inline tabulation
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
