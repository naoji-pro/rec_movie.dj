from django.contrib import admin
from django.urls import path
from movie.views import frontpage, view1, view2, view3,view4,view5,view6

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('page1/', view1, name='view1'),
    path('page2/', view2, name='view2'),
    path('page3/', view3, name='view3'),
    path('page4/', view4, name='view4'),
    path('page5/', view5, name='view5'),
    path('page6/', view6, name='view6'),
]