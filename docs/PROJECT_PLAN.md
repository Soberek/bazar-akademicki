# Plan projektu: Bazar Akademicki

## Przegląd

Projekt zakłada stworzenie aplikacji webowej typu marketplace dla studentów, opartej na Django (backend) i React/Tailwind (frontend).

**Zespół:** Student A (Backend), Student B (Frontend)  
**Czas realizacji:** 6 laboratoriów

---

## 📋 Backend (Student A) - Django

### Lab 1: Inicjalizacja projektu

- [x] Utworzenie projektu Django
- [x] Konfiguracja bazy danych (SQLite/PostgreSQL)
- [x] Inicjalizacja repozytorium Git
- [x] Struktura katalogów projektu
- [x] Konfiguracja Django REST Framework

### Lab 2: Modele danych

- [x] Model `Category` (kategorie produktów)
- [x] Model `Product/Listing` (oferty)
- [x] Model `User` (rozszerzony o dane studenta)
- [x] Migracje bazy danych
- [x] Panel administracyjny dla modeli

### Lab 3: CRUD ofert

- [x] Endpoint/widok dodawania oferty
- [x] Endpoint/widok edycji oferty
- [x] Endpoint/widok usuwania oferty
- [x] Obsługa zdjęć produktów
- [x] Walidacja danych

### Lab 4: System użytkowników

- [x] Rejestracja użytkowników
- [x] Logowanie/wylogowanie
- [x] Profil użytkownika
- [x] Lista ofert użytkownika
- [x] Autoryzacja (tylko właściciel edytuje ofertę)

### Lab 5: Wyszukiwanie i filtrowanie

- [x] Wyszukiwanie po nazwie/opisie
- [x] Filtrowanie po kategorii
- [x] Filtrowanie po cenie
- [x] Sortowanie wyników
- [ ] (Opcjonalnie) Koszyk/lista obserwowanych

### Lab 6: Dokumentacja

- [x] Dokumentacja README
- [x] Instrukcja instalacji
- [ ] Przygotowanie do prezentacji

---

## 🎨 Frontend (Student B) - HTML/Tailwind

### Lab 1: Layout bazowy

- [x] Struktura HTML (`base.html`)
- [x] Nawigacja główna
- [x] Stopka
- [x] Konfiguracja Tailwind CSS
- [x] Responsywność (mobile-first)

### Lab 2: Widoki produktów

- [x] Lista produktów (karty/siatka)
- [x] Strona szczegółów produktu
- [x] Komponent karty produktu
- [x] Paginacja
- [x] Stany ładowania

### Lab 3: Formularze ofert

- [x] Formularz dodawania oferty
- [x] Formularz edycji oferty
- [x] Upload zdjęć (preview)
- [x] Walidacja po stronie klienta
- [x] Komunikaty błędów/sukcesu

### Lab 4: System użytkowników (UI)

- [x] Strona logowania
- [x] Strona rejestracji
- [x] Profil użytkownika
- [x] Lista moich ofert
- [x] Edycja profilu

### Lab 5: Wyszukiwarka i filtry

- [x] Pasek wyszukiwania
- [x] Panel filtrów (kategoria, cena)
- [x] Widok wyników wyszukiwania
- [x] Sortowanie (UI)
- [ ] (Opcjonalnie) Widok koszyka

### Lab 6: Finalizacja

- [ ] Testy interfejsu (manualne)
- [x] Poprawki responsywności
- [x] Optymalizacja UX
- [ ] Przygotowanie prezentacji demo
- [ ] Nagranie/screenshot'y

---

## 🗂️ Struktura katalogów

```
ecommerce-studia/
├── manage.py                # Django manage
├── config/                  # Ustawienia Django
├── users/                   # Aplikacja użytkowników
├── marketplace/             # Produkty, kategorie, oferty
├── templates/               # Szablony HTML
├── static/                  # Pliki statyczne
├── media/                   # Zdjęcia produktów
├── frontend/                # React frontend (opcjonalnie)
├── docs/                    # Dokumentacja
├── .github/                 # Instrukcje Copilot
└── README.md
```

---

## ✅ Kamienie milowe

| Tydzień | Cel    | Backend         | Frontend           |
| ------- | ------ | --------------- | ------------------ |
| 1       | Setup  | ✅ Projekt + DB | ✅ Layout          |
| 2       | Dane   | ✅ Modele       | ✅ Lista produktów |
| 3       | CRUD   | ✅ Oferty       | ✅ Formularze      |
| 4       | Auth   | ✅ Użytkownicy  | ✅ Login/Profil    |
| 5       | Search | ✅ Filtrowanie  | ✅ UI wyszukiwania |
| 6       | Final  | ⬜ Testy        | ⬜ Prezentacja     |

---

## 🎯 Wymagania funkcjonalne

### Kluczowe (Must Have)

- Rejestracja i logowanie użytkowników
- Dodawanie, edycja i usuwanie ofert
- Przeglądanie ofert według kategorii
- Wyszukiwanie i filtrowanie produktów
- Panel użytkownika z listą ofert

### Opcjonalne (Nice to Have)

- Koszyk zakupowy
- Lista obserwowanych produktów
- System ocen sprzedających
- Integracja płatności

---

## 🚀 Następne kroki

1. **Backend**: Napisać testy jednostkowe dla modeli i widoków
2. **Frontend**: Przetestować wszystkie formularze i flow użytkownika
3. **Obydwaj**: Przygotować prezentację demo (5-10 min)

---

## 📝 Notatki

- Projekt realizowany w ramach zajęć praktycznych z technologii webowych
- Framework: Django (bez Oscar - uproszczona wersja)
- Baza danych: SQLite (dev) / PostgreSQL (prod)
- CSS: Tailwind CSS
- Frontend: React + Vite (SPA) lub Django Templates

---

_Ostatnia aktualizacja: Listopad 2025_
