from django.db import models

from django.utils import timezone


class FeedBack(models.Model):
    new = 'new_feed_back'
    progress = 'in_progress'
    ready = 'answered'
    problems = 'some_problems'
    FEED_BACK_STATUS = [
        (new, 'Новый вопрос'),
        (progress, 'В обработке'),
        (ready, 'Отвечен'),
        (problems, 'Возникли проблемы'),
    ]
    name = models.CharField('Название модели', max_length=120, null=True)
    email = models.EmailField('Email', max_length=120, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=20)
    description = models.TextField('Описание', max_length=300, blank=True, null=True)
    status = models.CharField(
        max_length=100,
        verbose_name='Статус вопроса',
        choices=FEED_BACK_STATUS,
        default=new
    )
    feedback_date = models.DateField(verbose_name='Дата вопроса', default=timezone.now)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'
