from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from django.views.generic.edit import CreateView, FormView

from spayce.forms import PedidoForm
from spayce.models import Pedido, Produto


class ValeuParca(TemplateView):
    template_name = 'core/valeu.html'


class PedidoView(FormView):
    template_name = 'core/pedido_form.html'
    form_class = PedidoForm
    success_url = reverse_lazy('obrigado')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)


class Status(TemplateView):
    template_name = 'core/status.html'
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(Status, self).get_context_data()
        context['total_pedidos'] = Pedido.objects.filter(
            consumidor=self.request.user).count()
        return context

pedido = PedidoView.as_view()
valeu = ValeuParca.as_view()
status = Status.as_view()
