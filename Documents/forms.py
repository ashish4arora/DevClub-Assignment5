from django.forms import ModelForm
from Documents.models import Document


class UploadFileForm(ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'course', 'file']