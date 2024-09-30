import random
from django.shortcuts import render, redirect
from datetime import datetime, timedelta

dishes = [
    {"name": "Kung Pao Chicken", "price": 10.00},
    {"name": "Peking Duck", "price": 20.00},
    {"name": "Ma Po Tofu", "price": 8.00},
    {"name": "Dumplings", "price": 5.00},
    {"name": "Sweet and Sour Pork", "price": 12.00},
    {"name": "Chow Mein", "price": 7.00},
    {"name": "Fried Rice", "price": 6.00},
    {"name": "Szechuan Beef", "price": 11.00},
    {"name": "Egg Fried Rice", "price": 6.00},
    {"name": "Hot Pot", "price": 15.00, "extras": ["Beef", "Seafood", "Dumplings"]},
]

special_price = 3.00 

def main(request):
    return render(request, 'restaurant/main.html')

def order(request):
    daily_special = random.choice(dishes)  
    context = {
        'daily_special': daily_special,
        'dishes': dishes  
    }
    return render(request, 'restaurant/order.html', context)

def confirmation(request):
    if request.method == 'POST':
        ordered_items = request.POST.getlist('ordered_items')  
        ordered_extra = request.POST.getlist('ordered_extra', '') 
        comments = request.POST.get('comments', '') 
        name = request.POST.get('name', '')  
        phone = request.POST.get('phone', '')  
        email = request.POST.get('email', '') 
        
        total_price = special_price if request.POST.get('daily_special') else 0

        for item in ordered_items:
            for dish in dishes:
                if dish['name'] == item:
                    total_price += dish['price']
        if ordered_extra:
            total_price += len(ordered_extra)
        
        current_time = datetime.now()
        ready_time = current_time + timedelta(minutes=random.randint(30, 60))
        ready_time_str = ready_time.strftime("%H:%M")
        
        context = {
            'ordered_items': ordered_items,
            'ordered_extra': ordered_extra,
            'total_price': total_price,
            'comments': comments if comments else None,  
            'name': name if name else None,              
            'phone': phone if phone else None,            
            'email': email if email else None, 
            'ready_time': ready_time_str,
        }
        return render(request, 'restaurant/confirmation.html', context)

    return redirect("main")
