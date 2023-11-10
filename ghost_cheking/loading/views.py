import django.shortcuts


def progres(request, a):
    if a == 1:
        s = '/result/all_done'
    else:
        s = '/result/errors'
    return django.shortcuts.render(request, 'loading/loading.html', context={'link': s})
