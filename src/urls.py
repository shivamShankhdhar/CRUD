# from django.contrib import admin
from django.urls import path
from .views import home, post_data,delete_task,task_cross_off, un_cross

app_name = 'src'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('post-data/', post_data, name='post-data'),
    path('delete/<int:id>', delete_task, name='what'),
    path('cross-off/<int:id>', task_cross_off, name='cross-off'),
    path('un-cross/<int:id>', un_cross, name='un-cross'),

]
