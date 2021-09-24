from app.views import make_abba, close_far, not_string
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warmup-1/not_string/<str>', not_string),
    path('string-1/make_abba/<a>/<b>', make_abba),
    path('logic-2/close_far/<int:a>/<int:b>/<int:c>', close_far),
]
