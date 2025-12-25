from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, UserUpdateForm
from .models import UserPreference
from bookmarks.models import Bookmark


def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('news:home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user preferences
            UserPreference.objects.create(user=user)
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('news:home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                next_url = request.GET.get('next', 'news:home')
                return redirect(next_url)
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    """User logout view"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('news:home')


@login_required
def profile(request):
    """User profile view"""
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
    else:
        form = UserUpdateForm(instance=request.user)
    
    # Get user statistics
    bookmark_count = Bookmark.objects.filter(user=request.user).count()
    
    # Get or create preferences
    preferences, created = UserPreference.objects.get_or_create(user=request.user)
    
    context = {
        'form': form,
        'bookmark_count': bookmark_count,
        'preferences': preferences,
    }
    return render(request, 'accounts/profile.html', context)
