from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from items.views import CategoryView, ItemCreateView, ItemDeleteView, ItemUpdateView, ItemView, MyItemView, create_category, create_item, get_items, home
from accounts.views import ChangePasswordView, UserCreateAPIView, UserLoginAPIView
from accounts.views import user_register, logout_user, login_user, edit_profile





urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("register/", user_register, name="register"),
    path("profile/", edit_profile, name="profile"),
    path("logout/", logout_user, name="logout"),
    path("login/", login_user, name="login"),
    path("profile/", edit_profile, name="profile"),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path("items/", get_items, name="items-list"),
    path("item/create/", create_item, name="create-item"),
    path("category/create/", create_category, name="create-category"),
    

    path('api/register/', UserCreateAPIView.as_view(), name='register-api'),
    path('api/login/', UserLoginAPIView.as_view(), name='login-api'),
    path('api/category/', CategoryView.as_view(), name='category-list-api'),
    path('api/item/', ItemView.as_view(), name='item-list-api'),
    path('api/item/create/', ItemCreateView.as_view(), name='create-item-api'),
    path('api/myitems/', MyItemView.as_view(), name='my_items_list-api'),
    path('api/item/delete/<int:item_id>/', ItemDeleteView.as_view(), name='delete-item-api'),
    path('api/item/edit/<int:item_id>/', ItemUpdateView.as_view(), name='edit-item-api'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
