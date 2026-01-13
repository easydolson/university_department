from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Department(models.Model):
    """Модель кафедры"""
    name = models.CharField(max_length=200, verbose_name="Название кафедры")
    room = models.CharField(max_length=50, verbose_name="Аудитория кафедры")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"

    def __str__(self):
        return self.name


class Classroom(models.Model):
    """Аудитории для преподавателей"""
    room_number = models.CharField(max_length=20, verbose_name="Номер аудитории")
    capacity = models.IntegerField(verbose_name="Вместимость", default=1)
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"

    def __str__(self):
        return f"Аудитория {self.room_number}"


class Employee(models.Model):
    """Сотрудник кафедры"""
    POSITION_CHOICES = [
        ('prof', 'Профессор'),
        ('docent', 'Доцент'),
        ('senior', 'Старший преподаватель'),
        ('assistant', 'Ассистент'),
        ('other', 'Другое'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100, blank=True, verbose_name="Отчество")
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, verbose_name="Должность")
    rate = models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(1.5)],
        verbose_name="Ставка",
        default=1.0
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    hire_date = models.DateField(verbose_name="Дата приема на работу")
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Рабочее место"
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class Subject(models.Model):
    """Дисциплина"""
    name = models.CharField(max_length=200, verbose_name="Название дисциплины")
    code = models.CharField(max_length=50, verbose_name="Код дисциплины")
    semester = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        verbose_name="Семестр"
    )
    hours_lecture = models.IntegerField(verbose_name="Часы лекций", default=0)
    hours_practice = models.IntegerField(verbose_name="Часы практики", default=0)
    employees = models.ManyToManyField(Employee, through='Teaching', verbose_name="Преподаватели")

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"

    def __str__(self):
        return self.name


class Teaching(models.Model):
    """Связь преподавателя и дисциплины"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Преподаватель")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Дисциплина")
    hours_per_week = models.IntegerField(verbose_name="Часов в неделю", default=2)
    is_responsible = models.BooleanField(default=False, verbose_name="Ответственный преподаватель")

    class Meta:
        verbose_name = "Преподавание"
        verbose_name_plural = "Преподавание"
        unique_together = ['employee', 'subject']


class AdditionalWork(models.Model):
    """Дополнительная работа"""
    WORK_TYPE_CHOICES = [
        ('curator', 'Кураторство'),
        ('practice', 'Проведение практик'),
        ('publications', 'Контроль научных публикаций'),
        ('science', 'Научная работа'),
        ('methodical', 'Методическая работа'),
        ('other', 'Другое'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    work_type = models.CharField(max_length=50, choices=WORK_TYPE_CHOICES, verbose_name="Вид работы")
    description = models.TextField(verbose_name="Описание")
    hours_per_month = models.IntegerField(verbose_name="Часов в месяц", default=0)
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    class Meta:
        verbose_name = "Дополнительная работа"
        verbose_name_plural = "Дополнительная работа"

    def __str__(self):
        return f"{self.employee} - {self.get_work_type_display()}"