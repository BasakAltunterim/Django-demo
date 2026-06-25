from django.test import TestCase, Client

# Create your tests here.


from django.urls import reverse
from .models import Student, lesson, exam, deadline

#öğrenci oluştuğunda veritabanına kayıt oluyor mu
class StudentModelTest(TestCase):
        def setUp(self):
            self.student = Student.objects.create(ad='Ahmet', soyad='Mehmet', email='ahmet@example.com')

        def test_student_str(self):
              self.assertEqual(str(self.student), 'Ahmet Mehmet')
              self.assertEqual(Student.objects.count(), 1)

#exam oluşturunca __str__ metodu çalışıyor mu ve exam ile lesson ilişkisi doğru mu
class examTestCase(TestCase):
    def setUp(self):
        self.lesson = lesson.objects.create(ders_adi='Matematik')
        self.exam = exam.objects.create(baslik='Sınav 1', aciklama='Açıklama', son_tarih='2023-12-31', ders_adi=self.lesson)

    def test_exam_str(self):
        self.assertEqual(str(self.exam), 'Sınav 1')
        self.assertEqual(exam.objects.count(), 1)
    
    def test_exam_iliskisi(self):
        self.assertEqual(self.exam.ders_adi.ders_adi, 'Matematik')

#/giriş sayfasını açılınca başarılı dönüy mu?, giriş yapmadan adres gidince ne oluyor, doğru kullanıcı adı ve şifre ile giriş yapşınca ne oluyor
class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        from django.contrib.auth.models import User
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

    def test_giris_sayfasi_aciliyor(self):
        response = self.client.get(reverse('giris'))
        self.assertEqual(response.status_code, 200)

    def test_giris_yapilmadan_anasayfa_redirect(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)

    def test_basarili_giris(self):
        response = self.client.post(reverse('giris'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)