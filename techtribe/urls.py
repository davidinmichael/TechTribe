from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account import views as register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", register_view.home, name="home"),
    path("profile/", register_view.profile, name="profile"),
    path("editprofile/", register_view.edit_profile, name="edit_profile"),
    path("account/", include("account.urls")),
    path("blog/", include("blog.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
