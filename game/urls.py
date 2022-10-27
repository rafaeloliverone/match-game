from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg import openapi, views

schema_view = views.get_schema_view(
    openapi.Info(
        title="Players API",
        default_version='v1',
        description="Players Application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="players@local.com"),
        license=openapi.License(name="BSD License"),
        x_logo={
            "url": "https://inclusio.io/wp-content/uploads/2022/02/Logo-09.svg",
            "backgroundColor": "#FFFFFF"
        }
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('match.urls')),
    path(
        'documentation-api/',
        schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'
    ),
]
