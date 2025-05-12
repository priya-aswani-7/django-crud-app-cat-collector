from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name='cat-index'),
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
]


# register a path called conclusion, handled by views.conclusion
# define the conclusion function in views.py and it must return 
# <h1>Conclusion! Thanks </h1>
