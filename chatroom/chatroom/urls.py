from django.contrib import admin
from django.urls import path
from chat.views import index, room
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls'))

]
