from django.db import models

# Create your models here.
class Repuesto(models.Model):
    #atributos
    nombre = models.CharField(max_length=50, blank=True)
    foto = models.ImageField(upload_to = 'pic_folder/', blank=True)
    descripcion1= models.TextField(max_length=50, blank=True)
    descripcion2= models.TextField(max_length=50, blank=True)
    descripcion3= models.TextField(max_length=50, blank=True)
    cantidad= models.IntegerField(default=0)
    
    def __unicode__(self):
        return  unicode(self.nombre)
    class Meta:
        verbose_name = "Repuesto"
        verbose_name_plural = "Repuestos"