"""
Django management command to setup stock records for products.
"""

from django.core.management.base import BaseCommand
from oscar.apps.catalogue.models import Product
from oscar.apps.partner.models import Partner, StockRecord


class Command(BaseCommand):
    help = "Create partner and stock records for products"

    def handle(self, *args, **options):
        # Create default partner if doesn't exist
        partner, created = Partner.objects.get_or_create(
            name='Bazar Akademicki',
            defaults={'code': 'bazar-akademicki'}
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"✓ Utworzono partnera: {partner.name}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"⚠ Partner już istnieje: {partner.name}")
            )

        # Create stock records for products without them
        products = Product.objects.filter(stockrecords__isnull=True)
        count = 0
        
        for product in products:
            try:
                # Create stock record with default price and quantity
                stock_record, created = StockRecord.objects.get_or_create(
                    product=product,
                    partner=partner,
                    defaults={
                        'partner_sku': f'{product.id}',
                        'price': 0.00,  # User can update this in dashboard
                        'num_in_stock': 1,
                    }
                )
                
                if created:
                    count += 1
                    self.stdout.write(
                        self.style.SUCCESS(f"✓ Dodano zapas dla: {product.title}")
                    )
                    
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"✗ Błąd przy dodawaniu zapasu dla {product.title}: {e}")
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"\n✓ Gotowe! Dodano {count} zapisów zapasów."
            )
        )
