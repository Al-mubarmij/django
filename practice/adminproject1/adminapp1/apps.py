from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class Adminapp1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adminapp1'

class BlogAdminConfig(AdminConfig):
    default_site = 'adminapp1.admin.BlogAdminArea'