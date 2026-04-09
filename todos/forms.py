from django import forms
from datetime import date
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "deadline"]

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if deadline and deadline < date.today():
            raise forms.ValidationError("Informe uma data de entrega válida")
        return deadline
