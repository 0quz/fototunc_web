from django import forms
from .models import Tracking


class TrackingForm(forms.ModelForm):

    class Meta:
        model = Tracking
        fields = [
            'name',
            'surname',
            'email',
            'phone_number',
            'tracking_number',
            'status',
            'information',
        ]