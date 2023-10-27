from django.db import models

# Create your models here.
class contactParm(models.Model):
    product_contact_whatsapp_phone = models.CharField(max_length=16)
    product_contact_whatsapp_text = models.TextField()

    class Meta:
        verbose_name_plural = 'contactParms'
    
    def __str__(self) -> str:
        return self.product_contact_whatsapp_phone