# 🛒 Bazar Akademicki

Aplikacja webowa typu marketplace umożliwiająca studentom sprzedaż i zakup używanych rzeczy.

## 📋 Opis projektu

Bazar Akademicki to platforma e-commerce dla studentów, gdzie można:

- Przeglądać oferty używanych produktów
- Dodawać własne ogłoszenia
- Wyszukiwać i filtrować produkty
- Kontaktować się ze sprzedającymi

## 🛠️ Technologie

**Backend:**

- Python 3.13
- Django 4.2
- Django REST Framework
- Django Oscar (e-commerce framework)
- SQLite (development)

**Frontend:**

- HTML5
- Tailwind CSS
- JavaScript (vanilla)

## 🚀 Instalacja

### Wymagania

- Python 3.10+
- pip

### Kroki instalacji

1. **Sklonuj repozytorium:**

```bash
git clone https://github.com/Soberek/bazar-akademicki.git
cd bazar-akademicki
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

4. **Wykonaj migracje bazy danych:**

```bash
python manage.py migrate
```

5. **Załaduj kategorie produktów:**

```bash
python manage.py setup_categories
```

6. **Załaduj klasy produktów (typy produktów):**

```bash
python manage.py setup_product_classes
```

7. **Utwórz partnera i zapasy dla produktów:**

```bash
python manage.py setup_stock
```

8. **Utwórz konto administratora (opcjonalnie):**

```bash
python manage.py createsuperuser
```

9. **Uruchom serwer:**

```bash
python manage.py runserver
```

10. **Otwórz przeglądarkę:**

- Aplikacja: http://127.0.0.1:8000
- Panel administracyjny: http://127.0.0.1:8000/admin
- Dashboard: http://127.0.0.1:8000/dashboard

## 📁 Struktura projektu

```
bazar-akademicki/
├── config/              # Ustawienia Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── users/               # Aplikacja użytkowników
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── management/      # Management commands
│   │   └── commands/
│   │       ├── setup_categories.py
│   │       ├── setup_product_classes.py
│   │       └── setup_stock.py
│   └── migrations/
├── templates/           # Szablony HTML (Oscar + custom)
│   ├── oscar/
│   ├── users/
│   └── ...
├── static/              # Pliki statyczne (CSS, JS)
├── media/               # Wgrywane pliki użytkowników
├── docs/                # Dokumentacja projektu
├── manage.py
└── requirements.txt     # Zależności Python
```

## 🔗 API Endpoints

| Endpoint           | Metoda    | Opis                         |
| ------------------ | --------- | ---------------------------- |
| `/`                | GET       | Strona główna                |
| `/users/register`  | GET, POST | Rejestracja użytkownika      |
| `/users/login`     | GET, POST | Logowanie                    |
| `/users/profile`   | GET, POST | Profil użytkownika           |
| `/api/listings/`   | GET       | Lista ofert (Oscar)          |
| `/api/categories/` | GET       | Lista kategorii (Oscar)      |
| `/admin/`          | GET       | Panel administracyjny Django |

## 👥 Autorzy

- **Student A** - Backend (Django, modele, API)
- **Student B** - Frontend (HTML, Tailwind, UI/UX)

## 📄 Licencja

Projekt edukacyjny - Technologie Webowe 2025
