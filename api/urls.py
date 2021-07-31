#django
from django.contrib import admin
from django.urls import path, include
#static files
from django.conf import settings
from django.conf.urls.static import static
#Views
from users.views.login import UserLoginAPIView as login 
from users.views import users as UserViews
from users.views.users import ProfileCompletionViewSet
from posts.views import PostViewSet
#Rest_framework 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts',PostViewSet, basename='posts')
router.register(r'profile', ProfileCompletionViewSet, basename='profile')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserViews.UserListView.as_view(), name="users"),
    path('users/login/', login.as_view(), name="login"),    
    path('users/signup/', UserViews.signup, name="signup"),
    path('users/verified', UserViews.account_verification, name="verify"),
    path('',include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)