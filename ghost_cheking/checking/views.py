import django.shortcuts
from django.views.generic import TemplateView

from .forms import UploadFileForm, handle_uploaded_file

a = False


class UploadFile(TemplateView):
    TEMPLATE = "checking/add_file.html"

    def get(self, request, *args, **kwargs):
        form = UploadFileForm()
        context = {'form': form}
        return django.shortcuts.render(request, self.TEMPLATE, context)

    def post(self, request):
        global a
        form = UploadFileForm(request.POST, request.FILES)
        context = {'form': form}
        if form and form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            if a:
                a = False
                return django.shortcuts.redirect("loading:progres-bar", 1)
            else:
                a = True
                return django.shortcuts.redirect("loading:progres-bar", 0)
        return django.shortcuts.render(request, self.TEMPLATE, context)
