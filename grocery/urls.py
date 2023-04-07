from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views
from .forms import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('',views.ProductView.as_view(), name='home'),

    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),

    path('cart/', views.show_cart, name='showcart'),

    path('pluscart/', views.plus_cart),

    path('minuscart/', views.minus_cart),

    path('removecart/', views.remove_cart),

    path('buy/', views.buy_now, name='buynow'),

    #path('profile/', views.profile, name='profile'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('address/', views.address, name='address'),

    path('update-address/<int:id>', views.update_address, name='updateaddress'),

    path('delete-address/<int:id>', views.delete_address, name='deleteaddress'),

    path('orders/', views.orders, name='orders'),

    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
    
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='changepassword.html',
    form_class=ChangePasswordForm, success_url='/passwordchangedone/'), name='changepassword'),
    
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html'),
    name='passwordchangedone'),
    
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html', 
    form_class=MyPasswordResetForm),name='password-reset'),

    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'
    ),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view
    (template_name='password_reset_confirm.html', form_class=MySetPasswordResetForm),name='password_reset_confirm'),

    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view
    (template_name='password_reset_complete.html'),name='password_reset_complete'),

    path('mobile/', views.mobile, name='mobile'),

    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    # path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', 
    # authentication_form=LoginForm), name='login'),
    path('atta/', views.atta, name='atta'),

    path('chhola/',views.chhola, name='chhola'),

    path('oil/',views.CookingOil, name='oil'),

    path('kitchen/',views.Kitchen, name='kitchen'),

    path('rice/',views.Rice, name='rice'),

    path('dal/',views.Dal, name='dal'),

    path('accounts/login/',views.loginUser,name='login'),
    # path('login/', views.LoginPage, name='login'),

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),

    path('logout/',auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('checkout/', views.checkout, name='checkout'),

    path('chooseaddress/', views.chooseaddress, name='chooseaddress'),

    path('success/' , views.success , name='success'),

    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('SearchView/', views.SearchView, name='SearchView'),

    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)