from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()
    file.widget.attrs["style"] = '''position: absolute;	z-index: -1; 	opacity: 0; 	display: block; 	
        width: 0;	height: 0;'''


def handle_uploaded_file(f):
    with open("media/upload/name.docx", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
