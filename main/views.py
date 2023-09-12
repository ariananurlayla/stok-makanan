from django.shortcuts import render

# Create your views here.


def show_main(request):
    context = {
        'name': 'Ariana Nurlayla Syabandini',
        'class': 'PBP C',
        'stok': [
            {
                'name': 'Cokelat',
                'amount': 2,
                'description': 'jajan',
            },
            {
                'name': 'Biskuit',
                'amount': 5,
                'description': 'jajan',
            }
        ]
    }

    return render(request, "main.html", context)
