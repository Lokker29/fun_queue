from django import forms

from core.models import Queue


class QueueModelForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = ('start_date', )

    def __init__(self, creator, *args, **kwargs):
        self._creator = creator
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.creator = self._creator

        return super().save(commit=commit)
