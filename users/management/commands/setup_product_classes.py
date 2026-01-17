"""
Django management command to create default product classes for Oscar.
"""

from django.core.management.base import BaseCommand
from oscar.apps.catalogue.models import ProductClass, ProductAttribute


class Command(BaseCommand):
    help = "Create default product classes for the marketplace"

    def handle(self, *args, **options):
        product_classes = [
            {
                "name": "Odzież",
                "attributes": ["Rozmiar", "Kolor", "Materiał", "Stan"]
            },
            {
                "name": "Elektronika",
                "attributes": ["Marka", "Model", "Stan", "Akcesoria"]
            },
            {
                "name": "Książki",
                "attributes": ["Autor", "Wydawnictwo", "Stan", "Edycja"]
            },
            {
                "name": "Meble",
                "attributes": ["Materiał", "Wymiary", "Stan", "Kolor"]
            },
            {
                "name": "Sport",
                "attributes": ["Rozmiar", "Marka", "Stan", "Typ"]
            },
            {
                "name": "Kosmetyka",
                "attributes": ["Marka", "Typ", "Odsetek użycia", "Stan"]
            },
            {
                "name": "Muzyka",
                "attributes": ["Typ", "Marka", "Stan", "Akcesoria"]
            },
            {
                "name": "Gry",
                "attributes": ["Platform", "Gatunek", "Stan", "Wydawca"]
            },
            {
                "name": "Inne",
                "attributes": ["Kategoria", "Stan", "Marka", "Model"]
            },
        ]

        created_count = 0
        updated_count = 0

        for pc_data in product_classes:
            try:
                product_class, created = ProductClass.objects.get_or_create(
                    name=pc_data["name"],
                    defaults={"requires_shipping": True}
                )

                if created:
                    created_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(f"✓ Utworzono klasę produktu: {product_class.name}")
                    )
                else:
                    updated_count += 1
                    self.stdout.write(
                        self.style.WARNING(f"⚠ Klasa już istnieje: {product_class.name}")
                    )

                # Add attributes to product class
                for attr_name in pc_data["attributes"]:
                    attribute, attr_created = ProductAttribute.objects.get_or_create(
                        product_class=product_class,
                        name=attr_name,
                        defaults={
                            "code": attr_name.lower().replace(" ", "_"),
                            "type": "text"  # lowercase!
                        }
                    )
                    if attr_created:
                        self.stdout.write(
                            self.style.SUCCESS(f"  + Dodano atrybut: {attr_name}")
                        )

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"✗ Błąd przy tworzeniu klasy {pc_data['name']}: {e}")
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"\n✓ Gotowe! Utworzono {created_count} klas, zaktualizowano {updated_count}."
            )
        )
