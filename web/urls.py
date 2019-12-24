from django.urls import re_path, path

from web import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newsite', views.new_page, name='n'),
    re_path(r'preview/(?P<pk>\w{22})/?$', views.log_preview, name='log-preview'),
    re_path(r'preview/(?P<pk>\w{22})/raw/?$', views.log_preview_raw, name='log-preview-raw'),
    re_path(r'preview/(?P<pk>\w{22})/export/?$', views.log_preview_export, name='log-preview-export'),
    re_path(r'preview/(?P<pk>\w{22})/save/?$', views.log_preview_save, name='log-preview-save'),
    re_path(r'(?P<pk>\w{22})/?$', views.log_html, name='log-html'),
    re_path(r'(?P<pk>\w{22})/raw/?$', views.log_raw, name='log-raw'),
    re_path(r'(?P<pk>\w{22})/export/?$', views.log_export, name='log-export'),
    re_path(r'(?P<pk>\w{22})/delete/?$', views.log_delete, name='log-delete'),
    path('new', views.new, name='new')
]
