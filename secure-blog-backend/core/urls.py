from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('api/auth/register/', include('accounts.urls')),
    path('api/auth/login/', TokenObtainPairView.as_view(), name="login"),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name="refresh"),

    # Blog
    path('api/blog/', include('blog.urls')),
]
