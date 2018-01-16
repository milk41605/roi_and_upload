from django import forms

from uploads.core.models import Document
# from uploads.core.models import Document_images

LOCATIONS=[('labels','label'),
        ('images','image')]

class DocumentForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATIONS, widget=forms.RadioSelect())
    class Meta:
        model = Document
        fields = ('description', 'document', 'location', )
#
#
# class DocumentForm_images(forms.ModelForm):
#     class Meta:
#         model = Document_images
#         fields = ('description', 'document', )
