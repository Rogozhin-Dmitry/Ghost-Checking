import django.shortcuts


def about(request):
    return django.shortcuts.render(request, 'checking/main.html')
