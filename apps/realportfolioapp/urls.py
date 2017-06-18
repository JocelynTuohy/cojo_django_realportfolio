from django.conf.urls import url
from . import views
app_name = 'realportfolioapp'
print 'wtf'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about', views.about, name='about'),
    url(r'projects', views.projects, name='projects'),
    url(r'testimonials', views.testimonials, name='testimonials'),
]