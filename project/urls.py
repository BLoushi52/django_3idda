from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from items.views import CategoryView, ItemCreateView, ItemDeleteView, ItemUpdateView, ItemView, MyItemView
from user.views import UserCreateAPIView, UserLoginAPIView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('category/', CategoryView.as_view(), name='category-list'),
    path('item/', ItemView.as_view(), name='item-list'),
    path('item/create/', ItemCreateView.as_view(), name='create-item'),
    path('myitems/', MyItemView.as_view(), name='my_items_list'),
    path('item/delete/<int:item_id>/', ItemDeleteView.as_view(), name='delete-item'),
    path('item/edit/<int:item_id>/', ItemUpdateView.as_view(), name='edit-item'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
