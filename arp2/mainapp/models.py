from django.db import models

# Create your models here.

class Repuesto(models.Model):
    #atributos
    nombre = models.CharField(max_length=50)
    foto = models.ImageField(upload_to = 'pic_folder/', null= True)
    descripcion= models.TextField(max_length=50)
    cantidad= models.IntegerField(default=0)
    def __unicode__(self):
        return  self.nombre
    class Meta:
        verbose_name = "Repuesto"
        verbose_name_plural = "Repuestos"

class Datos(models.Model):
    repuesto= models.ForeignKey(Repuesto)
    descripcion1= models.TextField(max_length=50)
    descripcion2=models.TextField(max_length=50)
    descripcion3= models.TextField(max_length=50)
   
    class Meta:
        verbose_name= "Datos"
        verbose_name_plural= "Datos"

