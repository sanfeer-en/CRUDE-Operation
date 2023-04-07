from  django.urls import path
from .views import name , index , demo , create, retrieve ,delete, editDetails, update

urlpatterns = [
    path("enter" , name),
    path("secondhead", demo),
    path("form", create),
    path("retrieve",retrieve),
    path("delete/<int:id>", delete , name="delete"),
    path("edit/<int:id>", editDetails,name='edit'),
    path("update/<int:id>", update ,name="update"), 
    
    
]
