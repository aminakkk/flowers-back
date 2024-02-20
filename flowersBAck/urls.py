from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.posts.views import PostAPIViewset

router = routers.DefaultRouter()  # регистрация модель и тд

router.register('post', PostAPIViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # узнать 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG: # если разработка идет, то дебак = тру, свагер работает
    schema_view = get_schema_view(
        openapi.Info(
            title='Notes',
            default_version = 'v1',
            description='test description',
            license=openapi.License(name='BSD License')
        ),
        public=True,
        permission_classes = (AllowAny, )
    )

    urlpatterns += [
        path('swagger(?P<format>.\json|\.yaml)', schema_view.with_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
