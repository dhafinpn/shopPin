from django.shortcuts import render

def show_main(request):
    context = {
        'product' : 'Manchester United 2024/2025 Official Jersey',
        'price': '2000000',
        'description': 'The Official Jersey of Manchester United for 2024/2025 season'
    }

    return render(request, "main.html", context)
