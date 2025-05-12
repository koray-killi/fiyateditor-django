# Fiyat Editor Django

Tarım ürünleri fiyat takip ve görselleştirme sistemi.

## Proje Hakkında

Fiyat Editor, tarım ürünlerinin (sebze) günlük fiyatlarını izlemek, kaydetmek ve görseller aracılığıyla görselleştirmek için tasarlanmış bir Django web uygulamasıdır. Uygulama, fiyat değişimlerini (artış, azalış, sabit) takip eder ve bu değişimleri görsel olarak gösterir.

Bu proje, başlangıçta Flask framework'ü kullanılarak geliştirilmiş bir uygulamanın Django'ya port edilmiş versiyonudur.

## Özellikler

- Farklı sebze türlerini (biber, domates, salatalık, patlıcan, kabak) kategorize etme
- Önceki ve güncel fiyatları karşılaştırma
- Fiyat değişimlerini görsel olarak izleme (artış, azalış, sabit)
- Fiyat bilgilerini otomatik olarak görsel formatta oluşturma
- Ürün fiyatlarını veritabanında saklama

## Proje Yapısı

```
fiyateditor-django/
├── FiyatEditor/
│   ├── FiyatEditor/           # Django proje ana dizini
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py        # Django yapılandırma dosyası
│   │   ├── urls.py            # Ana URL yönlendirmeleri
│   │   └── wsgi.py
│   ├── Main/                  # Ana uygulama dizini
│   │   ├── __init__.py
│   │   ├── admin.py           # Admin panel yapılandırması
│   │   ├── apps.py
│   │   ├── models.py          # Veri modelleri
│   │   ├── static/            # Statik dosyalar (CSS, JS, resimler)
│   │   │   └── pillow/        # Resim şablonları ve fontları
│   │   ├── templates/         # HTML şablonları
│   │   ├── tests.py           # Test dosyası
│   │   ├── urls.py            # Uygulama URL yönlendirmeleri
│   │   ├── utils.py           # Yardımcı fonksiyonlar ve görselleştirme
│   │   └── views.py           # Görünüm fonksiyonları
│   ├── db.sqlite3             # SQLite veritabanı
│   ├── manage.py              # Django yönetim betikleri
│   └── test.py                # İlave test dosyası
├── venv/                      # Sanal ortam klasörü
└── requirements.txt           # Bağımlılıklar listesi
```

## Kurulum

1. Repo'yu klonlayın:
```bash
git clone https://github.com/kullaniciadi/fiyateditor-django.git
cd fiyateditor-django
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python -m venv venv
source venv/bin/activate
```

3. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

4. Veritabanı migrasyonlarını uygulayın:
```bash
cd FiyatEditor
python manage.py migrate
```

5. Uygulamayı başlatın:
```bash
python manage.py runserver
```

6. Tarayıcınızda `http://127.0.0.1:8000/` adresine giderek uygulamayı görüntüleyin.

## Kullanım

1. Ana sayfada, her sebze türü için önceki ve güncel fiyatları girebilirsiniz.
2. Tarih bilgisini girin ve formu gönderin.
3. Sistem, girilen fiyatlara göre otomatik olarak bir görsel oluşturacaktır.
4. Oluşturulan görsel, başarı sayfasında görüntülenecektir.

## Gereksinimler

- Python 3.8+
- Django 4.0+
- Pillow 9.0+ (Görsel işleme için)
- Diğer bağımlılıklar `requirements.txt` dosyasında listelenmiştir.

## Katkıda Bulunma

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

## İletişim

Proje sahibi: [Adınız](https://github.com/kullaniciadi)

Proje linki: [https://github.com/kullaniciadi/fiyateditor-django](https://github.com/kullaniciadi/fiyateditor-django)
