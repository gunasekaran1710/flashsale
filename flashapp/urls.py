# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.login_view, name='login'),
#     path('flashsales/', views.flashsales_view, name='flashsales'),
# ]
from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('flashsales/', views.flashsales_view, name='flashsales'),

    # Serve the Firebase service worker from root
    re_path(r'^firebase-messaging-sw.js$', TemplateView.as_view(
        template_name="firebase-messaging-sw.js",  # this must be placed in the templates folder
        content_type='application/javascript',
    )),
]
