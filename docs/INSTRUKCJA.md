# 📖 Instrukcja - StudentShop

## 🚀 Jak uruchomić projekt

### Szybki start (3 kroki)

```bash
# 1. Aktywuj środowisko wirtualne
source .venv/bin/activate

# 2. Wykonaj migracje (jeśli pierwszy raz)
python manage.py migrate

# 3. Uruchom serwer
python manage.py runserver
```

**Otwórz w przeglądarce:** http://127.0.0.1:8000

---

### Pełna instalacja (od zera)

```bash
# 1. Sklonuj repo
git clone https://github.com/your-username/ecommerce-studia.git
cd ecommerce-studia

# 2. Utwórz środowisko wirtualne
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# 3. Zainstaluj pakiety
pip install -r requirements.txt

# 4. Migracje bazy danych
python manage.py migrate

# 5. Dodaj kategorie produktów
python manage.py setup_categories

# 6. (Opcjonalnie) Utwórz admina
python manage.py createsuperuser

# 7. Uruchom serwer
python manage.py runserver
```

---

## 🔗 Adresy URL

| Adres                                | Opis                 |
| ------------------------------------ | -------------------- |
| http://127.0.0.1:8000                | Strona główna        |
| http://127.0.0.1:8000/admin          | Panel administratora |
| http://127.0.0.1:8000/users/login    | Logowanie            |
| http://127.0.0.1:8000/users/register | Rejestracja          |
| http://127.0.0.1:8000/users/profile  | Profil użytkownika   |
| http://127.0.0.1:8000/listing/create | Dodaj ofertę         |
| http://127.0.0.1:8000/search         | Wyszukiwarka         |
| http://127.0.0.1:8000/api/listings   | API - lista ofert    |

---

## 🛠️ Komendy Django (VS Code Tasks)

W VS Code możesz użyć tasków (`Ctrl+Shift+P` → "Run Task"):

| Task                       | Opis                        |
| -------------------------- | --------------------------- |
| `Django: Run Server`       | Uruchom serwer deweloperski |
| `Django: Make Migrations`  | Utwórz nowe migracje        |
| `Django: Migrate`          | Zastosuj migracje           |
| `Django: Create Superuser` | Utwórz konto admina         |
| `Django: Setup Categories` | Dodaj domyślne kategorie    |

---

## 📁 Struktura folderów

```
ecommerce-studia/
│
├── 📁 config/                 # ⚙️ KONFIGURACJA DJANGO
│   ├── __init__.py
│   ├── settings.py            # Główne ustawienia projektu
│   ├── urls.py                # Główny router URL
│   ├── wsgi.py                # WSGI dla produkcji
│   └── asgi.py                # ASGI dla async
│
├── 📁 users/                  # 👤 APLIKACJA UŻYTKOWNIKÓW
│   ├── models.py              # Model User (rozszerzony)
│   ├── views.py               # Logowanie, rejestracja, profil
│   ├── forms.py               # Formularze użytkownika
│   ├── admin.py               # Panel admin dla User
│   ├── urls.py                # URL-e: /users/...
│   └── migrations/            # Migracje bazy danych
│
├── 📁 marketplace/            # 🛒 GŁÓWNA APLIKACJA (OFERTY)
│   ├── models.py              # Category, Listing, ListingImage
│   ├── views.py               # CRUD ofert, wyszukiwanie
│   ├── forms.py               # Formularze ofert
│   ├── admin.py               # Panel admin dla ofert
│   ├── urls.py                # URL-e: /, /listing/...
│   ├── api_urls.py            # URL-e API: /api/...
│   ├── api_views.py           # Widoki REST API
│   ├── serializers.py         # Serializery DRF
│   ├── migrations/            # Migracje bazy danych
│   └── management/
│       └── commands/
│           └── setup_categories.py  # Komenda dodająca kategorie
│
├── 📁 templates/              # 🎨 SZABLONY HTML
│   ├── base.html              # Bazowy szablon (layout)
│   ├── marketplace/           # Szablony ofert
│   └── users/                 # Szablony użytkowników
│
├── 📁 static/                 # 📦 PLIKI STATYCZNE (CSS, JS)
│
├── 📁 media/                  # 🖼️ PLIKI UŻYTKOWNIKÓW (zdjęcia)
│
├── 📁 docs/                   # 📚 DOKUMENTACJA
│   ├── PROJECT_PLAN.md        # Plan projektu
│   └── INSTRUKCJA.md          # Ta instrukcja
│
├── 📁 .venv/                  # 🐍 Środowisko wirtualne Python
├── 📁 .vscode/                # 💻 Ustawienia VS Code
├── 📁 .github/                # 🔧 Konfiguracja GitHub
│
├── manage.py                  # 🚀 CLI Django
├── requirements.txt           # 📋 Lista pakietów Python
├── db.sqlite3                 # 💾 Baza danych (po migracji)
└── README.md                  # 📖 Opis projektu
```

---

## 🗂️ Opis plików

### Config (Konfiguracja)

| Plik                 | Opis                                                               |
| -------------------- | ------------------------------------------------------------------ |
| `config/settings.py` | Wszystkie ustawienia: baza danych, aplikacje, middleware, szablony |
| `config/urls.py`     | Główny router - łączy URL-e z aplikacjami                          |

### Users (Użytkownicy)

| Plik              | Opis                                                                       |
| ----------------- | -------------------------------------------------------------------------- |
| `users/models.py` | Model `User` - rozszerzony o: telefon, uczelnia, bio, avatar               |
| `users/views.py`  | Widoki: `register`, `user_login`, `user_logout`, `profile`, `profile_edit` |
| `users/forms.py`  | Formularze: rejestracja, logowanie, edycja profilu                         |

### Marketplace (Oferty)

| Plik                         | Opis                                                                      |
| ---------------------------- | ------------------------------------------------------------------------- |
| `marketplace/models.py`      | Modele: `Category`, `Listing`, `ListingImage`                             |
| `marketplace/views.py`       | Widoki: lista ofert, szczegóły, dodawanie, edycja, usuwanie, wyszukiwanie |
| `marketplace/forms.py`       | Formularze: dodawanie/edycja oferty                                       |
| `marketplace/serializers.py` | Serializery dla REST API                                                  |
| `marketplace/api_views.py`   | Endpointy API                                                             |

---

## 🔑 Modele danych

### User (Użytkownik)

```
- username        # Nazwa użytkownika
- email           # Email
- first_name      # Imię
- last_name       # Nazwisko
- phone           # Telefon
- university      # Uczelnia
- bio             # O mnie
- avatar          # Zdjęcie profilowe
```

### Category (Kategoria)

```
- name            # Nazwa (np. "Odzież")
- slug            # URL-friendly (np. "odziez")
- description     # Opis
- icon            # Ikona CSS (FontAwesome)
- parent          # Kategoria nadrzędna (opcjonalnie)
```

### Listing (Oferta)

```
- title           # Tytuł
- description     # Opis
- price           # Cena (PLN)
- category        # Kategoria (FK)
- seller          # Sprzedający (FK → User)
- condition       # Stan: new, like_new, good, fair, poor
- status          # Status: active, sold, reserved, inactive
- location        # Lokalizacja
- views_count     # Liczba wyświetleń
- created_at      # Data dodania
```

### ListingImage (Zdjęcie oferty)

```
- listing         # Oferta (FK)
- image           # Plik zdjęcia
- is_main         # Czy główne zdjęcie
```

---

## 🎯 Funkcjonalności

### ✅ Zaimplementowane

- [x] Rejestracja i logowanie użytkowników
- [x] Profil użytkownika z edycją
- [x] Dodawanie ofert ze zdjęciami
- [x] Edycja i usuwanie własnych ofert
- [x] Przeglądanie ofert (lista, szczegóły)
- [x] Wyszukiwanie po tytule i opisie
- [x] Filtrowanie po kategorii, cenie, stanie
- [x] Sortowanie (najnowsze, cena)
- [x] Paginacja wyników
- [x] REST API dla ofert
- [x] Panel administracyjny

### ⬜ Do zrobienia (opcjonalnie)

- [ ] Koszyk zakupowy
- [ ] Lista obserwowanych
- [ ] System wiadomości
- [ ] Oceny sprzedających

---

## ❓ FAQ

**P: Jak zresetować bazę danych?**

```bash
rm db.sqlite3
python manage.py migrate
python manage.py setup_categories
python manage.py createsuperuser
```

**P: Jak dodać nową kategorię?**

- Panel admin → Kategorie → Dodaj
- Lub edytuj `marketplace/management/commands/setup_categories.py`

**P: Gdzie są zdjęcia produktów?**

- Folder `media/listings/`

**P: Jak zmienić port serwera?**

```bash
python manage.py runserver 8080
```
