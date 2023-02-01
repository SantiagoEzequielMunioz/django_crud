from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    registration_number = models.IntegerField()
    doctor_image = models.ImageField()

    editado = models.DateTimeField(auto_now=True)
    creado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
    
    def __str__(self) -> str:
        return (f'{(self.surname).upper()}, {(self.name).capitalize()}')

class Patient(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dni = models.IntegerField()
    cellphone = models.CharField(max_length=10)
    SEX_CHOICES = (
        ('male', 'Masculino'),
        ('female', 'Femenino'),
    )
    sex = models.CharField(
        max_length=10,
        choices=SEX_CHOICES
    )
    
    # obra social
    HEALTH_INSURANCE_CHOICES = (
        ('osde', 'Osde'),
        ('swiss', 'Swiss Medical'),
        ('prepaga', 'Prepaga X'),
    )
    health_insurance = models.CharField(
        max_length=10,
        choices=HEALTH_INSURANCE_CHOICES
    )

    # numero de obra social
    num_insurance = models.IntegerField(blank=True, null=True)
    
    patient_image = models.ImageField()

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def __str__(self) -> str:
        return (f'{(self.surname).upper()}, {(self.name).capitalize()}')