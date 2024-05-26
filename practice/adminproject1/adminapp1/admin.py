from django.contrib import admin
from . import models 


class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Stuff'

blog_admin_site = BlogAdminArea(name = 'BlogAdmin')
blog_admin_site.register(models.Blog)
admin.site.register(models.Blog)