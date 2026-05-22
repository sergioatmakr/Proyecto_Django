from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Receta

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_message = "¡Tu cuenta ha sido creada con éxito! Ya puedes iniciar sesión."

class RecetaListView(ListView):
    model = Receta
    template_name = 'recetas/receta_list.html'
    context_object_name = 'recetas'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(titulo__icontains=query) | Q(descripcion__icontains=query))
        return queryset

class RecetaDetailView(DetailView):
    model = Receta
    template_name = 'recetas/receta_detail.html'
    context_object_name = 'receta'

class RecetaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Receta
    fields = ['titulo', 'descripcion', 'ingredientes', 'instrucciones']
    template_name = 'recetas/receta_form.html'
    success_url = reverse_lazy('recetas:lista')
    success_message = "¡La receta ha sido publicada correctamente!"

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class RecetaUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Receta
    fields = ['titulo', 'descripcion', 'ingredientes', 'instrucciones']
    template_name = 'recetas/receta_form.html'
    success_url = reverse_lazy('recetas:lista')
    success_message = "¡La receta se ha actualizado con éxito!"

    def test_func(self):
        receta = self.get_object()
        return self.request.user == receta.autor or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, "Acción no autorizada: No tienes permisos para editar esta receta.")
        return redirect('recetas:lista')

class RecetaDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Receta
    template_name = 'recetas/receta_confirm_delete.html'
    success_url = reverse_lazy('recetas:lista')
    success_message = "La receta ha sido eliminada permanentemente."

    def test_func(self):
        receta = self.get_object()
        return self.request.user == receta.autor or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, "Acción no autorizada: No tienes permisos para eliminar este contenido.")
        return redirect('recetas:lista')