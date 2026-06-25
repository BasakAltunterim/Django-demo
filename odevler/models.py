from django.db import models

# Create your models here.

class Student(models.Model):
    ad=models.CharField(max_length=40)
    soyad=models.CharField(max_length=70)
    email=models.EmailField(unique=True)

    def __str__(self):
        return f"{self.ad} {self.soyad}"
    

class lesson(models.Model):
    ders_adi=models.CharField(max_length=90)

    def __str__(self):
        return self.ders_adi
    

class exam(models.Model):
    baslik=models.CharField(max_length=100)
    aciklama=models.CharField(max_length=200)
    son_tarih=models.DateField()
    ders_adi=models.ForeignKey(lesson,on_delete=models.CASCADE) #kayıt silindiğinde ona bağlı kayıtlarda silinir.

    def __str__(self): #bir nesneyi yazdırdığında ne görüleceğini belirler. exam object(1)==> sınav 30 dk 
        return self.baslik
    

class deadline(models.Model):
    ogrenci=models.ForeignKey(Student,on_delete=models.CASCADE)
    sinav=models.ForeignKey(exam,on_delete=models.CASCADE)
    teslim_tarihi=models.DateTimeField(auto_now_add=True)
    dosya=models.FileField(upload_to='teslimler/')
    puan=models.IntegerField(null=True,blank=True) #blank alan doldurmak zorunlu değil
    

    class Meta:
        indexes = [
            models.Index(fields=['ogrenci'], name='ogrenci_index'),
            models.Index(fields=['sinav'], name='sinav_index'),
        ]
    
    def __str__(self):
      return f"{self.ogrenci} - {self.sinav}"
    


