from django.urls import path
from . import views

app_name = 'recetas'

urlpatterns = [
    path('', views.RecetaListView.as_view(), name='lista'),
    path('receta/<int:pk>/', views.RecetaDetailView.as_view(), name='detalle'),
    path('receta/nueva/', views.RecetaCreateView.as_view(), name='crear'),
    path('receta/<int:pk>/editar/', views.RecetaUpdateView.as_view(), name='editar'),
    path('receta/<int:pk>/eliminar/', views.RecetaDeleteView.as_view(), name='eliminar'),
    path('registrarse/', views.SignUpView.as_view(), name='signup'),
]