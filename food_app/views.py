from django.shortcuts import render

def food_home(request):
    categories = ["Pizza", "Burgers", "Pasta", "Sandwiches", "Fries & Sides", "Wraps", "Drinks", "Desserts"]

    items = [
        # 🍕 PIZZA
        {
            "name": "Chicken Fajita Pizza", "category": "Pizza", "base_price": 1099,
            "small_price": 799, "medium_price": 1099, "large_price": 1399,
            "description": "Spicy chicken, capsicum, onions and cheese", "has_options": True
        },
        {
            "name": "Chicken Tikka Pizza", "category": "Pizza", "base_price": 1099,
            "small_price": 799, "medium_price": 1099, "large_price": 1399,
            "description": "Chicken tikka, onions, tomatoes and mozzarella", "has_options": True
        },
        {
            "name": "Creamy Garlic Pizza", "category": "Pizza", "base_price": 1199,
            "small_price": 799, "medium_price": 1199, "large_price": 1499,
            "description": "Creamy garlic sauce, chicken and extra cheese", "has_options": True
        },
        {
            "name": "Pepperoni Pizza", "category": "Pizza", "base_price": 1299,
            "small_price": 899, "medium_price": 1299, "large_price": 1599,
            "description": "Pepperoni, mozzarella and tomato sauce", "has_options": True
        },
        {
            "name": "Cheese Lover Pizza", "category": "Pizza", "base_price": 999,
            "small_price": 699, "medium_price": 999, "large_price": 1299,
            "description": "Extra mozzarella and cheddar cheese", "has_options": True
        },
        {
            "name": "BBQ Chicken Pizza", "category": "Pizza", "base_price": 1199,
            "small_price": 799, "medium_price": 1199, "large_price": 1499,
            "description": "BBQ chicken, onions, capsicum and cheese", "has_options": True
        },
        {
            "name": "Mexican Hot Pizza", "category": "Pizza", "base_price": 1249,
            "small_price": 849, "medium_price": 1249, "large_price": 1549,
            "description": "Spicy chicken, jalapeños, onions and peppers", "has_options": True
        },
        {
            "name": "Veggie Supreme Pizza", "category": "Pizza", "base_price": 999,
            "small_price": 699, "medium_price": 999, "large_price": 1299,
            "description": "Capsicum, mushrooms, olives, onions and tomatoes", "has_options": True
        },

        # 🍔 BURGERS
        {"name": "Classic Chicken Burger", "category": "Burgers", "base_price": 399, "description": "Crispy chicken fillet, lettuce and mayo", "has_options": False},
        {"name": "Zinger Burger", "category": "Burgers", "base_price": 449, "description": "Crispy spicy chicken, lettuce and special sauce", "has_options": False},
        {"name": "Cheese Zinger Burger", "category": "Burgers", "base_price": 499, "description": "Zinger chicken, cheese, lettuce and sauce", "has_options": False},
        {"name": "BBQ Chicken Burger", "category": "Burgers", "base_price": 499, "description": "Grilled chicken, BBQ sauce and cheese", "has_options": False},
        {"name": "Double Patty Burger", "category": "Burgers", "base_price": 649, "description": "Two juicy chicken patties with cheese", "has_options": False},
        {"name": "Beef Smash Burger", "category": "Burgers", "base_price": 599, "description": "Beef patty, cheese, onions and special sauce", "has_options": False},
        {"name": "Jalapeño Burger", "category": "Burgers", "base_price": 549, "description": "Crispy chicken, jalapeños, cheese and spicy sauce", "has_options": False},
        {"name": "Mega Tower Burger", "category": "Burgers", "base_price": 699, "description": "Double chicken, cheese, lettuce and special sauce", "has_options": False},

        # 🍝 PASTA
        {
            "name": "Chicken Alfredo Pasta", "category": "Pasta", "base_price": 649,
            "half_price": 449, "full_price": 649, "description": "Creamy white sauce, chicken and parmesan", "has_options": True
        },
        {
            "name": "Creamy Garlic Pasta", "category": "Pasta", "base_price": 599,
            "half_price": 399, "full_price": 599, "description": "Creamy garlic sauce with grilled chicken", "has_options": True
        },
        {
            "name": "Chicken Penne Pasta", "category": "Pasta", "base_price": 649,
            "half_price": 449, "full_price": 649, "description": "Penne pasta, chicken and creamy sauce", "has_options": True
        },
        {
            "name": "Arrabbiata Pasta", "category": "Pasta", "base_price": 549,
            "half_price": 399, "full_price": 549, "description": "Spicy tomato sauce, herbs and parmesan", "has_options": True
        },
        {
            "name": "BBQ Chicken Pasta", "category": "Pasta", "base_price": 699,
            "half_price": 499, "full_price": 699, "description": "BBQ chicken, creamy sauce and cheese", "has_options": True
        },
        {
            "name": "Cheese Macaroni", "category": "Pasta", "base_price": 499,
            "half_price": 349, "full_price": 499, "description": "Creamy macaroni with melted cheese", "has_options": True
        },
        {
            "name": "Spicy Chicken Pasta", "category": "Pasta", "base_price": 649,
            "half_price": 449, "full_price": 649, "description": "Spicy chicken, peppers and creamy sauce", "has_options": True
        },

        # 🥪 SANDWICHES
        {"name": "Grilled Chicken Sandwich", "category": "Sandwiches", "base_price": 449, "description": "Grilled chicken, lettuce, cheese and mayo", "has_options": False},
        {"name": "Club Sandwich", "category": "Sandwiches", "base_price": 549, "description": "Chicken, egg, cheese, lettuce and mayo", "has_options": False},
        {"name": "Crispy Chicken Sandwich", "category": "Sandwiches", "base_price": 499, "description": "Crispy chicken, cheese and special sauce", "has_options": False},
        {"name": "BBQ Chicken Sandwich", "category": "Sandwiches", "base_price": 499, "description": "BBQ chicken, onions and melted cheese", "has_options": False},
        {"name": "Cheese Sandwich", "category": "Sandwiches", "base_price": 349, "description": "Double cheese, vegetables and creamy sauce", "has_options": False},
        {"name": "Chicken Mayo Sandwich", "category": "Sandwiches", "base_price": 399, "description": "Shredded chicken, mayo and fresh vegetables", "has_options": False},

        # 🍟 FRIES & SIDES
        {"name": "Classic Fries", "category": "Fries & Sides", "base_price": 249, "description": "Crispy golden fries with seasoning", "has_options": False},
        {"name": "Masala Fries", "category": "Fries & Sides", "base_price": 299, "description": "Fries with spicy masala seasoning", "has_options": False},
        {"name": "Cheese Fries", "category": "Fries & Sides", "base_price": 399, "description": "Crispy fries topped with cheese sauce", "has_options": False},
        {"name": "Loaded Fries", "category": "Fries & Sides", "base_price": 499, "description": "Fries, chicken, cheese and special sauce", "has_options": False},
        {"name": "Chicken Nuggets", "category": "Fries & Sides", "base_price": 399, "description": "Crispy chicken nuggets", "has_options": False},
        {"name": "Mozzarella Sticks", "category": "Fries & Sides", "base_price": 449, "description": "Crispy mozzarella cheese sticks", "has_options": False},
        {"name": "Chicken Wings", "category": "Fries & Sides", "base_price": 499, "description": "Crispy spicy chicken wings", "has_options": False},

        # 🌯 WRAPS
        {"name": "Chicken Shawarma Wrap", "category": "Wraps", "base_price": 349, "description": "Chicken, garlic sauce, lettuce and pickles", "has_options": False},
        {"name": "Crispy Chicken Wrap", "category": "Wraps", "base_price": 399, "description": "Crispy chicken, lettuce and special sauce", "has_options": False},
        {"name": "BBQ Chicken Wrap", "category": "Wraps", "base_price": 449, "description": "BBQ chicken, cheese and vegetables", "has_options": False},
        {"name": "Spicy Chicken Wrap", "category": "Wraps", "base_price": 399, "description": "Spicy chicken, jalapeños and creamy sauce", "has_options": False},
        {"name": "Cheese Chicken Wrap", "category": "Wraps", "base_price": 449, "description": "Chicken, extra cheese and special sauce", "has_options": False},

        # 🥤 DRINKS
        {"name": "Coca Cola", "category": "Drinks", "base_price": 120, "description": "Chilled soft drink", "has_options": False},
        {"name": "Pepsi", "category": "Drinks", "base_price": 120, "description": "Chilled soft drink", "has_options": False},
        {"name": "7UP", "category": "Drinks", "base_price": 120, "description": "Chilled lemon-lime drink", "has_options": False},
        {"name": "Sprite", "category": "Drinks", "base_price": 120, "description": "Chilled lemon-lime drink", "has_options": False},
        {"name": "Fresh Lemonade", "category": "Drinks", "base_price": 199, "description": "Fresh lemon, water and mint", "has_options": False},
        {"name": "Mint Margarita", "category": "Drinks", "base_price": 299, "description": "Fresh mint, lemon and crushed ice", "has_options": False},
        {"name": "Chocolate Shake", "category": "Drinks", "base_price": 349, "description": "Creamy chocolate milkshake", "has_options": False},
        {"name": "Vanilla Shake", "category": "Drinks", "base_price": 349, "description": "Creamy vanilla milkshake", "has_options": False},
        {"name": "Strawberry Shake", "category": "Drinks", "base_price": 349, "description": "Fresh strawberry milkshake", "has_options": False},
        {"name": "Cold Coffee", "category": "Drinks", "base_price": 349, "description": "Chilled creamy coffee", "has_options": False},

        # 🍰 DESSERTS
        {"name": "Chocolate Lava Cake", "category": "Desserts", "base_price": 399, "description": "Warm chocolate cake with molten center", "has_options": False},
        {"name": "Chocolate Brownie", "category": "Desserts", "base_price": 299, "description": "Soft chocolate brownie", "has_options": False},
        {"name": "Chocolate Cake Slice", "category": "Desserts", "base_price": 349, "description": "Rich chocolate cake with cream", "has_options": False},
        {"name": "Cheesecake", "category": "Desserts", "base_price": 449, "description": "Creamy cheesecake with biscuit base", "has_options": False},
        {"name": "Oreo Cake", "category": "Desserts", "base_price": 399, "description": "Chocolate cake with Oreo cream", "has_options": False},
        {"name": "Ice Cream Sundae", "category": "Desserts", "base_price": 349, "description": "Ice cream, chocolate sauce and toppings", "has_options": False},
        {"name": "Waffles", "category": "Desserts", "base_price": 399, "description": "Crispy waffles with chocolate and cream", "has_options": False},
        {"name": "Chocolate Donut", "category": "Desserts", "base_price": 249, "description": "Soft chocolate donut", "has_options": False},
    ]

    # 🔥 SPECIAL DEALS
    deals = [
        {"title": "Burger Combo", "discount_price": 799, "original_price": 1050, "badge": "Combo Deal", "description": "Zinger Burger + Fries + Drink", "is_deal": True, "deal_type": "combo"},
        {"title": "Pizza Combo", "discount_price": 1499, "original_price": 1850, "badge": "Best Value", "description": "Medium Pizza + Fries + 2 Drinks", "is_deal": True, "deal_type": "combo"},
        {"title": "Pasta Combo", "discount_price": 899, "original_price": 1150, "badge": "Special", "description": "Full Pasta + Garlic Bread + Drink", "is_deal": True, "deal_type": "combo"},
        {"title": "Family Feast", "discount_price": 2499, "original_price": 3200, "badge": "Family Deal", "description": "Large Pizza + 2 Burgers + Large Fries + 4 Drinks", "is_deal": True, "deal_type": "combo"},
        {"title": "Night Deal (30% OFF)", "discount_price": 699, "original_price": 999, "badge": "8 PM – 12 AM", "description": "Special night discount on menu items", "is_deal": True, "deal_type": "time_based", "available_time": "8 PM - 12 AM", "discount": "30%"},
        {"title": "Lunch Deal (25% OFF)", "discount_price": 599, "original_price": 799, "badge": "12 PM – 4 PM", "description": "Flat 25% discount during lunch hours", "is_deal": True, "deal_type": "time_based", "available_time": "12 PM - 4 PM", "discount": "25%"},
        {"title": "Weekend Deal (40% OFF)", "discount_price": 899, "original_price": 1499, "badge": "Sat & Sun", "description": "Weekend special mega discount", "is_deal": True, "deal_type": "time_based", "available_time": "Weekend", "discount": "40%"},
        {"title": "Flash Deal (50% OFF)", "discount_price": 499, "original_price": 999, "badge": "Flash Sale", "description": "Limited time 50% discount on selected items", "is_deal": True, "deal_type": "flash", "discount": "50%"},
    ]

    context = {
        "categories": categories,
        "items": items,
        "deals": deals,
    }
    return render(request, "food_home.html", context)