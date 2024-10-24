from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),

    path('menu-item/', views.menu_item, name='menu-item'),
    path('menu-item/<int:id>/', views.view_menu_item, name='view-menu-item'),
    path('menu-item-add/', views.add_menu_item, name='menu-item-add'),
    path('menu-item-edit/<int:id>/', views.edit_menu_item, name="menu-item-edit"),
    path('menu-item-delete/<int:id>/', views.delete_menu_item, name="menu-item-delete"),

    path('category/', views.category, name='category'),
    path('category/<int:id>/', views.view_category, name='view-category'),
    path('category-add/', views.add_category, name='category-add'),
    path('category-edit/<int:id>/', views.edit_category, name="category-edit"),
    path('category-delete/<int:id>/', views.delete_category, name="category-delete"),

    path('customer/', views.customer, name='customer'),
    path('customer/<int:id>/', views.view_customer, name='view-customer'),
    path('customer-add/', views.add_customer, name='customer-add'),
    path('customer-edit/<int:id>/', views.edit_customer, name="customer-edit"),
    path('customer-delete/<int:id>/', views.delete_customer, name="customer-delete"),

    path('order/', views.order, name='order'),
    path('order/<int:id>/', views.view_order, name='view-order'),
    path('order-add/', views.add_order, name='order-add'),
    path('order-edit/<int:id>/', views.edit_order, name="order-edit"),
    path('order-delete/<int:id>/', views.delete_order, name="order-delete"),

    path('order-item/', views.order_item, name='order-item'),
    path('order-item/<int:id>/', views.view_order_item, name='view-order-item'),
    path('order-item-add/', views.add_order_item, name='order-item-add'),
    path('order-item-edit/<int:id>/', views.edit_order_item, name="order-item-edit"),
    path('order-item-delete/<int:id>/', views.delete_order_item, name="order-item-delete"),

    path('shipping-address/', views.shipping_address, name='shipping-address'),
    path('shipping-address/<int:id>/', views.view_shipping_address, name='view-shipping-address'),
    path('shipping-address-add/', views.add_shipping_address, name='shipping-address-add'),
    path('shipping-address-edit/<int:id>/', views.edit_shipping_address, name="shipping-address-edit"),
    path('shipping-address-delete/<int:id>/', views.delete_shipping_address, name="shipping-address-delete"),

    path('query-first/', views.query_first, name='query-first'),
    path('query-second/', views.query_second, name='query-second'),
    path('query-third/', views.query_third, name='query-third'),
    path('query-fourth/', views.query_fourth, name='query-fourth'),
    path('query-fifth/', views.query_fifth, name='query-fifth'),
    path('query-sixth/', views.query_sixth, name='query-sixth'),
    path('query-seventh/', views.query_seventh, name='query-seventh'),
    path('query-eighth/', views.query_eighth, name='query-eighth'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)