from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('createinvoice', views.createinvoice, name='createinvoice'),
	path('properties', views.properties, name='properties'),
	path('agent', views.agent, name='agent'),
	

	# path('invoice/', views.ViewPDF.as_view(), name="invoice"),
  # path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
]