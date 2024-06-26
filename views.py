from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestaurantForm, TableFormSet, MenuItemFormSet
from .models import Restaurant
from django.contrib.auth.decorators import login_required
from UserManagement.decorators import role_required, role_and_restaurant_required

@login_required
@role_required(['administrator', 'restaurant_owner'])
def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        table_formset = TableFormSet(request.POST)
        menu_formset = MenuItemFormSet(request.POST)
        if form.is_valid() and table_formset.is_valid() and menu_formset.is_valid():
            restaurant = form.save()
            table_formset.instance = restaurant
            table_formset.save()
            menu_formset.instance = restaurant
            menu_formset.save()

            request.user.restaurants.add(restaurant)
            return redirect('dashboard')
    else:
        form = RestaurantForm()
        table_formset = TableFormSet()
        menu_formset = MenuItemFormSet()

    return render(request, 'restaurant/create_restaurant.html', {
        'form': form,
        'table_formset': table_formset,
        'menu_formset': menu_formset
    })

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant/restaurant_list.html', {'restaurants': restaurants})

@login_required
@role_and_restaurant_required(['administrator', 'restaurant_owner'])
def edit_restaurant(request, pk):
    restaurant = get_object_or_404(Restaurant, id=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
        table_formset = TableFormSet(request.POST, instance=restaurant)
        menu_formset = MenuItemFormSet(request.POST, instance=restaurant)
        if form.is_valid() and table_formset.is_valid() and menu_formset.is_valid():
            form.save()
            table_formset.save()
            menu_formset.save()
            return redirect('dashboard_detail', pk=pk)
    else:
        form = RestaurantForm(instance=restaurant)
        table_formset = TableFormSet(instance=restaurant)
        menu_formset = MenuItemFormSet(instance=restaurant)

    return render(request, 'restaurant/edit_restaurant.html', {
        'form': form,
        'table_formset': table_formset,
        'menu_formset': menu_formset,
        'restaurant': restaurant
    })
