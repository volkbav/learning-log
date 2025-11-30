from django.db import models

# Create your models here.
class Topic(models.Model):
    # Тема, которую изучает пользователь
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        # Возвращает строковое представление модели.
        return self.text
    
class Entry(models.Model):
    # """Информация, изученная пользователем по теме"""
    # внешний ключ
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    # используется для создания доп. атрибута,
    # который приказывает Django использовать форму множественного числа Entries
    #  при обращении более чем к одной записи. 
    # (Без этого Django будет использовать неправильную форму Entrys.)
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        # """Возвращает строковое представление модели."""
        return f"{self.text[:50]}..."