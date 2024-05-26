
from django.contrib import admin
from django.urls import path, include
from adminapp1.admin import blog_admin_site


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadmin/', blog_admin_site.urls),
    path('', include('adminapp1.urls')),
]


# Changing the index title in the admin panel
#admin.site.index_title = "The Bookstore"

# Changing the header of the admin panel/login - instead of django admin
#admin.site.site_header = "Bookstore Admin"

# Changing the title that appears on the tab in the browser
#admin.site.site_title = "The Bookstore"