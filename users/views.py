from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm


def register(request):
    """Rejestracja nowego użytkownika."""
    if request.user.is_authenticated:
        return redirect('marketplace:listing_list')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Rejestracja zakończona pomyślnie!')
            return redirect('marketplace:listing_list')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    """Logowanie użytkownika."""
    if request.user.is_authenticated:
        return redirect('marketplace:listing_list')
    
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Witaj, {user.get_full_name_or_username()}!')
            next_url = request.GET.get('next', 'marketplace:listing_list')
            return redirect(next_url)
    else:
        form = UserLoginForm()
    
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    """Wylogowanie użytkownika."""
    logout(request)
    messages.info(request, 'Zostałeś wylogowany.')
    return redirect('marketplace:listing_list')


@login_required
def profile(request):
    """Widok profilu użytkownika."""
    user_listings = request.user.listings.all().order_by('-created_at')
    return render(request, 'users/profile.html', {
        'user_listings': user_listings,
    })


@login_required
def profile_edit(request):
    """Edycja profilu użytkownika."""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil został zaktualizowany.')
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'users/profile_edit.html', {'form': form})
