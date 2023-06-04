from django.urls import path
from . import views
from .views import ProjectPageView, ProjectInfoView
app_name = 'blog'

urlpatterns = [
    path('', views.home_page,
         name='home-page'),
    path('videos/', views.videos_page, name='videos-page'),
    # path('projects/', views.projects_page, name='projects-page'),
    path('projects/', ProjectPageView.as_view(), name='projects-page'),
    # path('projects/details/', views.project_details_page, name='project-info'),
    path('projects/details/<int:pk>', ProjectInfoView.as_view(), name='project-info'),
    path('about-me/', views.about_me_page, name='about-me')
]
