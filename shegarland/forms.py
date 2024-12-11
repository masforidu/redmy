from django import forms
from .models import ShegarLandForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First Name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last Name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class ShegarLandFormForm(forms.ModelForm):
    guyya_qophae = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
        })
    )

    class Meta:
        model = ShegarLandForm
        fields = [
            'Kutaamagaalaa', 'Aanaa', 'iddo_adda', 'lakk_adda', 'gosa_tajajila',
            'madda_lafa', 'tajajila_iddo', 'haala_beenya','qamaa_qophaef',
            'tajajila_qophaef', 'balina_lafa', 'kan_qophesse', 'guyya_qophae',
            'shapefile', 'Ragaa_biroo', 'Mallattoo',
            'bal_lafa_bahi_tae', 'bal_lafa_hafe',
            'qaama_bahi_tahef', 'tajajila_bahi_tahef',
            'kan_bahi_taasise', 'ragaittin_bahi_tae', 'guyyaa_bahi_tae',
        ]
       
    def __init__(self, *args, **kwargs):  # Corrected from _init to _init_
        user = kwargs.pop('user', None)  # Extract user from kwargs
        print("Initializing form with user:", user)  # Debug print
        super(ShegarLandFormForm, self).__init__(*args, **kwargs)  # Call the parent constructor

        # Check if user is not admin
        if user and not user.is_staff:
            # Make additional fields read-only
            read_only_fields = [
                'bal_lafa_bahi_tae', 'bal_lafa_hafe', 'qaama_bahi_tahef',
                'tajajila_bahi_tahef', 'kan_bahi_taasise', 'guyyaa_bahi_tae',
            ]
            for field in read_only_fields:
                self.fields[field].widget.attrs['readonly'] = 'readonly'
                self.fields[field].label += " (Only for Admin)"  # Append label indicating admin-only

    def clean_lakk_adda(self):
        lakk_adda = self.cleaned_data.get('lakk_adda')
        if lakk_adda < 0:
            raise forms.ValidationError("Lakk adda must be a positive integer.")
        return lakk_adda

    def clean_Ragaa_biroo(self):
        Ragaa_biroo = self.cleaned_data.get('Ragaa_biroo', None)  # Ensure this matches your model field
        if Ragaa_biroo is None:  # If no file is uploaded
            return None  # Return None instead of raising an error
        return Ragaa_biroo  # Return the uploaded file if it exists