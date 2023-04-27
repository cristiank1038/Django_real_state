# from django.forms import ModelForm
# from .models import Listing


# class ListingForm(ModelForm):
#     class Meta:
#         model = Listing
#         fields = [
#             "title",
#             "price",
#             "num_bedrooms",
#             "num_bathrooms",
#             "square_footage",
#             "address",
#             "image",
#         ]

from django import forms

from .models import Listing

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'



class NewItemForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'price', 'num_bedrooms', 'num_bathrooms', 'square_footage', 'address', 'image',)
        widgets = {
            
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'num_bedrooms': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'num_bathrooms': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),


            'square_footage': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'address': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'price', 'num_bedrooms', 'num_bathrooms', 'square_footage', 'address', 'image',)
        widgets = {
            
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'num_bedrooms': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'num_bathrooms': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),


            'square_footage': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'address': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }