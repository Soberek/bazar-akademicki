"""
Django management command to create default product categories using Oscar.
"""

from django.core.management.base import BaseCommand
from oscar.apps.catalogue.models import Category


class Command(BaseCommand):
    help = "Create default product categories for the marketplace"

    def handle(self, *args, **options):
        categories_data = [
            "Odzież",
            "Elektronika", 
            "Książki",
            "Meble",
            "Sport",
            "Kosmetyka",
            "Muzyka",
            "Gry",
            "Inne",
        ]

        created_count = 0
        
        for cat_name in categories_data:
            try:
                slug = cat_name.lower().replace(" ", "-")
                # Check if category exists
                category = Category.objects.filter(name=cat_name).first()
                
                if not category:
                    # Use add_root from treebeard
                    category = Category.add_root(
                        name=cat_name,
                        slug=slug
                    )
                    created_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(f"✓ Utworzono kategorię: {category.name}")
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"⚠ Kategoria już istnieje: {category.name}")
                    )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"✗ Błąd przy tworzeniu {cat_name}: {e}")
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"\n✓ Gotowe! Utworzono {created_count} nowych kategorii."
            )
        )
