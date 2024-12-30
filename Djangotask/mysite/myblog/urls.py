from django.urls import path
from .import views

urlpatternsdict={
    'm1':views.month1,
    'm2':views.month2,
    'm3':views.month3,
    'm4':views.month4,
    'm5':views.month5,
    'm6':views.month6,
    'm7':views.month7,
    'm8':views.month8,
    'm9':views.month9,
    'm10':views.month10,
    'm11':views.month11,
    'm12':views.month12
}
urlpatterns=[
   path(f'{url}/', views,name=url) 
   for url,views in urlpatternsdict.items()
]