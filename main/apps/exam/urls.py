from django.conf.urls import url
from . import views

urlpatterns=[
    #login/registration
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.validate_login),
    url(r'^logout$', views.logout),
    #links to other pages
    url(r'^success$', views.success),
    url(r'^add$', views.add),
    url(r'handy/(?P<job_id>\d+)/show$', views.show),
    url(r'handy/(?P<job_id>\d+)/edit$', views.edit),
    #processes
    url(r'create_process$', views.create_process),    
    url(r'^handy/(?P<job_id>\d+)/update_process$', views.update),
    
    #targeted actions
    url(r'handy/(?P<job_id>\d+)/cancel$', views.destroy),
    # url(r'^add_job/(?P<job_id>\d+)$', views.users_job),

]