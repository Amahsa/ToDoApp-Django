from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('', home_page, name = 'home_page'),
    path('add_task/',add_task , name='add_task'),
    path('submit',submit,name='submit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('tasks/',list,name='todo_list'),
    path('sortdata/byScheduling/',sortdata_by_scheduling,name='sortdata_by_scheduling'),
    path('sortdata/byId/',sortdata_by_id,name='sortdata_by_id'),
    path('sortdata/byPriority/',sortdata_by_priority,name='sortdata_by_priority'),
    path('searchdata',searchdata,name='searchdata'),
    path('edit/<int:id>',edit,name='edit'),
    path('update/<int:id>',update,name='update'),
    path('todo_detail/<int:id>/',details , name='todo_detail'),
    path('categores/',CategoryList.as_view(),name='category_list'),
    path('categores/<int:id>/',category_tasks,name='category_tasks'),  
    path('categoryDelete/<int:id>/', category_delete,name='category_delete'),
    path('categoryEdit/<int:id>/', category_edit,name='category_edit'),
    path('category_update/<int:id>',category_update,name='category_update'),
   
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)