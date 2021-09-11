from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    BaseView,
    ProductDetailView,
    CategoryDetailView,
    CartView,
    AddToCartView,
    DeleteFromCartView,
    ChangeQTYView,
    CheckoutView,
    MakeOrderView,
    LoginView,
    ProfileView,
    AboutView,
    DeliveryView,
    ContactsView,
    FeedbackView,
    RegistrationView, SearchView, GuaranteeView, HowtobuyView
)


urlpatterns = [
    path('', BaseView.as_view(), name='index'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='goods'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('search/', SearchView.as_view(), name='search'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('about/', AboutView.as_view(), name='about'),
    path('delivery/', DeliveryView.as_view(), name='delivery'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('guarantee/', GuaranteeView.as_view(), name='guarantee'),
    path('howtobuy/', HowtobuyView.as_view(), name='howtobuy'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]
