"""
URL configuration for jmwWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from jmwapp import views
from jmwapp.views import download_application, JobApplicationView

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('jobs/', views.jobs, name='jobs'),
    path('trailers/', views.trailers, name='trailer_types'),
    path('job-application/', JobApplicationView.as_view(), name='job_application'),
    path('application-success/', TemplateView.as_view(template_name="application_success.html"), name='application_success'),
    path('download-application/', download_application, name='download_application'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'jmwapp.views.custom_404'
