from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Multicubing API",
      default_version='v1',
      description="Multicubing API documentation",
      contact=openapi.Contact(email="ukasz.klimkiewicz@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

app_name = 'docs'

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='swagger-without-ui'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
]
