from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
import orders.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orders.urls')),
    path('docs/', include_docs_urls(title="Order API")),
]
