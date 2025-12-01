from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:  # отвечает за модель (на которой базируется) и поля формы
        model = Topic
        fields = ['text']  # поля
        labels = {'text': ''}  # подпись полей

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        
        """(widget) представляет собой элемент формы HTML: 
        однострочное или многострочное текстовое поле, 
        раскрывающийся список и т.д. Включая атрибут widgets, 
        вы можете переопределить виджеты, выбранные Django по умолчанию. 
        Приказывая Django использовать элемент"""

        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        """Приказывая Django использовать элемент forms.
        Textarea, мы настраиваем виджет ввода для поля 'text', 
        чтобы ширина текстовой области составляла 80 столбцов 
        вместо значения по умолчанию 40. 
        У пользователя будет достаточно места для создания 
        содержательных записей."""
        