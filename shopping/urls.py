from django.urls import path
from shopping.views import *

urlpatterns = [

    path('admin_dashboard/', admin_dashboard),
    path('category_index/',category_index),
    path('add_category/', create_category),
    path('edit_category/',edit_category),
    #path('delete_category/',delete_category),
    path('Product_index/',Product_index),
    path('add_product/', create_product),
    path('edit_product/',edit_product),
    path('delete_product/',delete_product),
    



]
