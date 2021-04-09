from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user_profile.forms import UniGroupModelForm


class LogoutView(DjangoLogoutView):
    template_name = 'service/logout.html'


class UniGroupCreateView(CreateView):
    template_name = 'modals/create_group.html'
    form_class = UniGroupModelForm
    success_message = 'Групу успішно створено'
    success_url = reverse_lazy('core:queue_list')

    def form_invalid(self, form):
        return JsonResponse(status=400, data={'errors': form.errors})

    def form_valid(self, form):
        super().form_valid(form)
        return JsonResponse(status=200, data={'next': self.get_success_url()})
