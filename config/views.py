from django.views.generic import TemplateView
from oscar.apps.catalogue.models import Product


class HomePageView(TemplateView):
    template_name = 'oscar/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get latest 8 products
        context['products'] = Product.objects.filter(
            is_public=True
        ).order_by('-date_created')[:8]
        return context
