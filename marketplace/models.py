from django.db import models
from django.conf import settings
from django.urls import reverse


class Category(models.Model):
    """Model kategorii produktów."""
    
    name = models.CharField('Nazwa', max_length=100)
    slug = models.SlugField('Slug', unique=True)
    description = models.TextField('Opis', blank=True)
    icon = models.CharField('Ikona (CSS class)', max_length=50, blank=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Kategoria nadrzędna'
    )
    created_at = models.DateTimeField('Data utworzenia', auto_now_add=True)

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('marketplace:category_detail', kwargs={'slug': self.slug})


class Listing(models.Model):
    """Model oferty/produktu."""
    
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Aktywna'
        SOLD = 'sold', 'Sprzedana'
        RESERVED = 'reserved', 'Zarezerwowana'
        INACTIVE = 'inactive', 'Nieaktywna'

    class Condition(models.TextChoices):
        NEW = 'new', 'Nowy'
        LIKE_NEW = 'like_new', 'Jak nowy'
        GOOD = 'good', 'Dobry'
        FAIR = 'fair', 'Dostateczny'
        POOR = 'poor', 'Do naprawy'

    title = models.CharField('Tytuł', max_length=200)
    slug = models.SlugField('Slug', unique=True, blank=True)
    description = models.TextField('Opis')
    price = models.DecimalField('Cena', max_digits=10, decimal_places=2)
    
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='listings',
        verbose_name='Kategoria'
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='listings',
        verbose_name='Sprzedający'
    )
    
    condition = models.CharField(
        'Stan',
        max_length=20,
        choices=Condition.choices,
        default=Condition.GOOD
    )
    status = models.CharField(
        'Status',
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    
    location = models.CharField('Lokalizacja', max_length=100, blank=True)
    views_count = models.PositiveIntegerField('Liczba wyświetleń', default=0)
    
    created_at = models.DateTimeField('Data dodania', auto_now_add=True)
    updated_at = models.DateTimeField('Ostatnia aktualizacja', auto_now=True)

    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Oferty'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('marketplace:listing_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            import uuid
            self.slug = f"{slugify(self.title)}-{str(uuid.uuid4())[:8]}"
        super().save(*args, **kwargs)

    @property
    def main_image(self):
        """Zwraca główne zdjęcie oferty."""
        first_image = self.images.first()
        return first_image.image if first_image else None


class ListingImage(models.Model):
    """Model zdjęć oferty."""
    
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Oferta'
    )
    image = models.ImageField('Zdjęcie', upload_to='listings/')
    is_main = models.BooleanField('Zdjęcie główne', default=False)
    created_at = models.DateTimeField('Data dodania', auto_now_add=True)

    class Meta:
        verbose_name = 'Zdjęcie oferty'
        verbose_name_plural = 'Zdjęcia ofert'
        ordering = ['-is_main', 'created_at']

    def __str__(self):
        return f"Zdjęcie: {self.listing.title}"
