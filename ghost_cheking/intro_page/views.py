import django.shortcuts


def intro(request):
    return django.shortcuts.render(request, 'intro_page/intro.html')
