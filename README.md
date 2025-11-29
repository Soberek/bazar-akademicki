# 🛒 StudentShop - Wirtualny Second-Hand dla Studentów

Aplikacja webowa typu marketplace umożliwiająca studentom sprzedaż i zakup używanych rzeczy.

## 📋 Opis projektu

StudentShop to platforma e-commerce dla studentów, gdzie można:

- Przeglądać oferty używanych produktów
- Dodawać własne ogłoszenia
- Wyszukiwać i filtrować produkty
- Kontaktować się ze sprzedającymi

## 🛠️ Technologie

**Backend:**

- Python 3.13
- Django 4.2
- Django REST Framework
- SQLite (development)

**Frontend:**

- HTML5
- Tailwind CSS
- JavaScript

## 🚀 Instalacja

### Wymagania

- Python 3.10+
- pip

### Kroki instalacji

1. **Sklonuj repozytorium:**

```bash
git clone https://github.com/your-username/ecommerce-studia.git
cd ecommerce-studia
```

2. **Utwórz wirtualne środowisko:**

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# lub
.venv\Scripts\activate  # Windows
```

3. **Zainstaluj zależności:**

```bash
pip install -r requirements.txt
```

4. **Wykonaj migracje:**

```bash
python manage.py migrate
```

5. **Utwórz kategorie:**

```bash
python manage.py setup_categories
```

6. **Utwórz superusera (opcjonalnie):**

```bash
python manage.py createsuperuser
```

7. **Uruchom serwer:**

```bash
python manage.py runserver
```

8. **Otwórz przeglądarkę:**
   - Aplikacja: http://127.0.0.1:8000
   - Panel admin: http://127.0.0.1:8000/admin

## 📁 Struktura projektu

```
ecommerce-studia/
├── config/              # Ustawienia Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/               # Aplikacja użytkowników
│   ├── models.py        # Model User
│   ├── views.py         # Logowanie, rejestracja, profil
│   └── forms.py
├── marketplace/         # Główna aplikacja
│   ├── models.py        # Category, Listing, ListingImage
│   ├── views.py         # CRUD ofert, wyszukiwanie
│   ├── forms.py
│   ├── serializers.py   # API serializers
│   └── api_views.py     # REST API
├── templates/           # Szablony HTML
├── static/              # Pliki statyczne
├── media/               # Pliki użytkowników
└── requirements.txt
```

## 🔧 API Endpoints

| Endpoint              | Metoda | Opis             |
| --------------------- | ------ | ---------------- |
| `/api/listings/`      | GET    | Lista ofert      |
| `/api/listings/`      | POST   | Dodaj ofertę     |
| `/api/listings/<id>/` | GET    | Szczegóły oferty |
| `/api/categories/`    | GET    | Lista kategorii  |

## 👥 Autorzy

- **Student A** - Backend (Django, modele, API)
- **Student B** - Frontend (HTML, Tailwind, UI/UX)

## 📄 Licencja

Projekt edukacyjny - Technologie Webowe 2025
