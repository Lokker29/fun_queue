from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms

from user_profile.models import UniGroup


class UniGroupModelForm(forms.ModelForm):
    class Meta:
        model = UniGroup
        fields = '__all__'
