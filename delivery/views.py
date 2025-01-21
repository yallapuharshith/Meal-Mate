from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from delivery.models import Customer, Restaurant, MenuItem

# Home Page
def index(request):
    return render(request, 'delivery/index.html')

# Sign In Page
def signin(request):
    return render(request, 'delivery/signin.html')

# Sign Up Page
def signup(request):
    return render(request, 'delivery/signup.html')

# Handle Login
def handle_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Check if the customer exists
            Customer.objects.get(username=username, password=password)
            return render(request, 'delivery/success.html')
        except Customer.DoesNotExist:
            return render(request, 'delivery/fail.html')
    return HttpResponse("Invalid request")

# Handle Sign Up
def handle_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        # Check for duplicate username
        if not Customer.objects.filter(username=username).exists():
            Customer.objects.create(
                username=username,
                password=password,
                email=email,
                mobile=mobile,
                address=address
            )
            return render(request, 'delivery/signin.html')

    return HttpResponse("Invalid request")

# Add Restaurant Page
def restaurant_page(request):
    return render(request, 'delivery/add_restaurant.html')

# Add Restaurant
def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')

        Restaurant.objects.create(name=name, picture=picture, cuisine=cuisine, rating=rating)

        restaurants = Restaurant.objects.all()
        return render(request, 'delivery/show_restaurants.html', {"restaurants": restaurants})

    return HttpResponse("Invalid request")

# Show Restaurants
def show_restaurant_page(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'delivery/show_restaurants.html', {"restaurants": restaurants})

# Restaurant Menu
def restaurant_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        is_veg = request.POST.get('is_veg') == 'on'
        picture = request.POST.get('picture')

        MenuItem.objects.create(
            restaurant=restaurant,
            name=name,
            description=description,
            price=price,
            is_veg=is_veg,
            picture=picture
        )
        return redirect('restaurant_menu', restaurant_id=restaurant.id)

    menu_items = restaurant.menu_items.all()
    return render(request, 'delivery/menu.html', {
        'restaurant': restaurant,
        'menu_items': menu_items,
    })

# Update Restaurant Page
def update_restaurant_page(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    return render(request, 'delivery/update_restaurant_page.html', {"restaurant": restaurant})

# Update Restaurant
def update_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        restaurant.name = request.POST.get('name')
        restaurant.picture = request.POST.get('picture')
        restaurant.cuisine = request.POST.get('cuisine')
        restaurant.rating = request.POST.get('rating')
        restaurant.save()

        restaurants = Restaurant.objects.all()
        return render(request, 'delivery/show_restaurants.html', {"restaurants": restaurants})

# Delete Restaurant
def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    restaurant.delete()

    restaurants = Restaurant.objects.all()
    return render(request, 'delivery/show_restaurants.html', {"restaurants": restaurants})


# Update Menu item Page
def update_menuItem_page(request, menuItem_id):
    menuItem = get_object_or_404(MenuItem, id=menuItem_id)
    return render(request, 'delivery/update_menuItem_page.html', {"item": menuItem})

# Update MenuItem
def update_menuItem(request, menuItem_id):
    menuItem = get_object_or_404(MenuItem, id=menuItem_id)

    if request.method == 'POST':
        menuItem.name = request.POST.get('name')
        menuItem.description = request.POST.get('description')
        menuItem.price = request.POST.get('price')
        menuItem.is_veg = request.POST.get('is_veg') == 'on'
        menuItem.picture = request.POST.get('picture')

        menuItem.save()

        restaurants = Restaurant.objects.all()
        return render(request, 'delivery/show_restaurants.html', {"restaurants": restaurants})

# Delete menuItem
def delete_menuItem(request, menuItem_id):
    menuItem = get_object_or_404(MenuItem, id=menuItem_id)
    menuItem.delete()

    restaurants = Restaurant.objects.all()
    return render(request, 'delivery/show_restaurants.html', {"restaurants": restaurants})
