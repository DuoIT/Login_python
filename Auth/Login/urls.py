from django.conf.urls import url
from .views import IndexClass, LoginClass, ViewUser, view_product, AddPost

app_name = 'Login'
urlpatterns = [
    url(r'index/', IndexClass.as_view(), name="index"),
    url(r'login/', LoginClass.as_view(), name="login"),
    url(r'view-user/', ViewUser.as_view(), name="view-user"),
    url(r'view-product/', view_product, name="view-product"),
    url(r'add-post/', AddPost.as_view(), name="add-post"),
]
