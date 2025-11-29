from django.core.management.base import BaseCommand
from marketplace.models import Category


class Command(BaseCommand):
    help = 'Tworzy domyślne kategorie produktów dla marketplace'

    def handle(self, *args, **options):
        categories = [
            {'name': 'Odzież', 'slug': 'odziez', 'icon': 'fa-tshirt', 'description': 'Ubrania, buty, akcesoria'},
            {'name': 'Książki', 'slug': 'ksiazki', 'icon': 'fa-book', 'description': 'Podręczniki, literatura, skrypty'},
            {'name': 'Elektronika', 'slug': 'elektronika', 'icon': 'fa-laptop', 'description': 'Komputery, telefony, sprzęt'},
            {'name': 'Meble', 'slug': 'meble', 'icon': 'fa-couch', 'description': 'Biurka, krzesła, regały'},
            {'name': 'Sport', 'slug': 'sport', 'icon': 'fa-futbol', 'description': 'Sprzęt sportowy, odzież sportowa'},
            {'name': 'Muzyka', 'slug': 'muzyka', 'icon': 'fa-music', 'description': 'Instrumenty, sprzęt audio'},
            {'name': 'Gry', 'slug': 'gry', 'icon': 'fa-gamepad', 'description': 'Gry planszowe, video, konsole'},
            {'name': 'Inne', 'slug': 'inne', 'icon': 'fa-box', 'description': 'Pozostałe przedmioty'},
        ]

        created_count = 0
        for cat_data in categories:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={
                    'name': cat_data['name'],
                    'icon': cat_data['icon'],
                    'description': cat_data['description'],
                }
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Utworzono kategorię: {category.name}'))
            else:
                self.stdout.write(f'Kategoria już istnieje: {category.name}')

        self.stdout.write(self.style.SUCCESS(f'\nUtworzono {created_count} nowych kategorii.'))
