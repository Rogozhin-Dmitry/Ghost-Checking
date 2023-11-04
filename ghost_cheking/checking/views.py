import django.shortcuts
from django import forms
from django.views.generic import TemplateView


def upload_file(request):
    return django.shortcuts.render(request, 'checking/main.html')


class UploadForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)


class UploadFile(TemplateView):
    TEMPLATE = "checking/main.html"

    def get(self, request, *args, **kwargs):
        form = UploadForm(request.POST or None)
        context = {'form': form}
        return django.shortcuts.render(request, self.TEMPLATE, context)

    def post(self, request):
        form = UploadForm(request.POST or None)
        if request.method == 'POST':
            if form and form.is_valid():
                print('lol, wtf')
            #     return redirect('item_detail', item_num=context['item'].pk)
            # return render(request, self.TEMPLATE, context)
