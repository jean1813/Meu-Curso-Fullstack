from django.urls import path
from .views import PostListCreate, PostDetail
from rest_framework_simplejwt.views import (
     TokenObtainPairView,
     TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentação",
        default_version='v1',
        description="Documentação da API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@minhaapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
 path('posts/', PostListCreate.as_view(), name='post-list-create'),
 path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
 path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
 path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
 path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schemaredoc'),

]