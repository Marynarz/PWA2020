from django import forms


class TaskForm(forms.Form):
    task_name = forms.CharField(label='Task name:', max_length=20)
    description = forms.CharField(label='Description', widget=forms.Textarea)

class BoardForm(forms.Form):
    board_name = forms.CharField(label='Nazwa tablicy:', max_length=20)
    description = forms.CharField(label='Opis', widget=forms.Textarea)


class TabForm(forms.Form):
    tab_name = forms.CharField(label='Tab name:', max_length=20)
