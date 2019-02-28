# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from rest_framework import generics, permissions

from spayce.forms import PedidoForm
from spayce.models import Product, Order
from spayce.permissions import IsAdmin
from spayce.serializers import ProductSerializer, OrderSerializer


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
        context['total_pedidos'] = Order.objects.filter(
            consumidor=self.request.user).count()
        context['lista_pedidos'] = Order.objects.all()
        return context


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsAdmin,
    )

    def perform_create(self, serializer):
        """Save the post data when creating a new product.
        Check if product already exists"""
        duplicated = False
        for q in self.get_queryset():
            if q.name == serializer.validated_data['name']:
                duplicated = True
        if not duplicated:
            serializer.save()


class ProductView(generics.ListAPIView):
    """List of Product saved, to show to authenticated users"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProductRetrieve(generics.RetrieveAPIView):
    """Retrieve a single object, search by name. To authenticated users
    only."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'name'
    permission_classes = (permissions.IsAuthenticated,)


class ProductDetail(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdmin)


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsAdmin,
    )

    def perform_create(self, serializer):
        """Save the post data when creating a new product.
        Check if product already exists"""
        duplicated = False
        for q in self.get_queryset():
            if q.name == serializer.validated_data['name']:
                duplicated = True
        if not duplicated:
            serializer.save()


class OrderDetail(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdmin)


pedido = PedidoView.as_view()
valeu = ValeuParca.as_view()
status = Status.as_view()
productlist = ProductList.as_view()
productview = ProductView.as_view()
productdetail = ProductDetail.as_view()
productretrieve = ProductRetrieve.as_view()
orderlist = OrderList.as_view()
orderdetail = OrderDetail.as_view()
