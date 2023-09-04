from django.db import models



class Employees(models.Model):
    name = models.CharField('ФИО сотрудника', max_length=75)
    about = models.CharField('Описание', max_length=150)
    emp_img = models.ImageField('Фото сотрудника', upload_to='images/employees')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'




class Participants(models.Model):
    name = models.CharField('ФИО участника', max_length=65)
    title_univer = models.CharField('Наименование учебного заведения', max_length=65)
    phone = models.IntegerField('Номер телефона')
    email = models.EmailField('Email',max_length=55)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
