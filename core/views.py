from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from core.forms import QueueModelForm
from core.models import Queue
from user_profile.forms import UniGroupModelForm
from user_profile.models import UniGroup


class QueueListView(ListView):
    model = Queue
    template_name = 'queue_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = UniGroup.objects.all()
        context['create_group_form'] = UniGroupModelForm()
        return context


class QueueCreateView(CreateView):
    template_name = 'modals/create_queue.html'
    form_class = QueueModelForm
    success_message = 'Чергу успішно створено'
    success_url = reverse_lazy('core:queue_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['creator'] = self.request.user
        return kwargs
