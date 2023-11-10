import django.shortcuts


def all_done(request):
    return django.shortcuts.render(request, 'results/all_done.html')


def errors(request):
    return django.shortcuts.render(request, 'results/errors.html')
