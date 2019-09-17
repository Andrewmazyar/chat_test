from .models import Chat
from django import forms


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = (
            'description',
        )

