# Görev Tebliği

## Görev adı

**Bozuk Görev Zarfını Kurtarma ve Doğrulama**

## Süre

Bir iş günü.

## Amaç

Bir AI ajanına veya otomasyon sistemine iş aktarılırken kullanılan görev zarfının belirlenmiş kurallara uygun, güvenli ve makine tarafından doğrulanabilir hâle getirilmesi.

## Senaryo

Bir sistem, görevleri JSON biçiminde alıyor. Mevcut doğrulayıcı bazı kuralları kontrol etmiyor ve örnek görev zarfı da birden fazla hata içeriyor. Bu durum hatalı veri işlenmesine, yetkisiz eylemlere ve güvensiz dosya yollarına yol açabilir.

Senden beklenen, mevcut kodu ve veriyi inceleyerek sistemi belirtilen sözleşmeye uygun hâle getirmendir.

## Yapılacak işler

1. Depoyu bilgisayarına al.
2. Testleri çalıştır ve başlangıçta başarısız olan testleri `submission/FINDINGS.md` içine yaz.
3. `docs/01_CONTRACT.md` dosyasını oku. Bu belge tek yetkili teknik kaynaktır.
4. `src/envelope_validator.py` içindeki `TODO` işaretlerini ve hatalı kontrolleri düzelt.
5. `candidate/task_envelope.json` dosyasını sözleşmeye uygun hâle getir.
6. Tüm testleri geçir.
7. Teslim belgelerini doldur.
8. `scripts/grade.py` komutunu çalıştır ve `FINAL RESULT: PASS` çıktısını al.

## Doğrulayıcıdan beklenenler

- Zorunlu alanları kontrol etme
- Alan tiplerini kontrol etme
- Boş metinleri reddetme
- Durum değerlerini kontrol etme
- İnsan onayı gerektiren eylemleri kontrol etme
- Güvensiz dosya yollarını reddetme
- Anlaşılır hata mesajları üretme
- İlk hatada durmak yerine tüm hataları birlikte döndürme

## Aday görev zarfının amacı

Dosyanın amacı değişmemelidir: örnek müşteri geri bildirimlerini sınıflandıran, yalnızca rapor üreten ve dış sisteme işlem yapmayan bir görev olarak kalmalıdır.

## Değiştirilebilecek dosyalar

- `src/envelope_validator.py`
- `candidate/task_envelope.json`
- `submission/FINDINGS.md`
- `submission/AI_USAGE.md`
- `submission/LEARNING_NOTE.md`

## Değiştirilmemesi gereken dosyalar

- `tests/**`
- `docs/01_CONTRACT.md`
- `scripts/grade.py`

## Kabul kriterleri

- Tüm otomatik testler geçiyor.
- `scripts/grade.py` PASS veriyor.
- Görev zarfında gerçek sır veya kişisel veri yok.
- Güvenlik kuralları kod içinde uygulanıyor.
- Bulgular belgesi gerçek hata nedenlerini açıklıyor.
- AI kullanımı dürüstçe beyan ediliyor.
- Çalışma beş dakika içinde açıklanabiliyor.

## Sunumda anlatılacaklar

1. Başlangıçta hangi hatalar vardı?
2. En kritik güvenlik problemi neydi?
3. Doğrulayıcıyı nasıl düzelttin?
4. Hangi test seni en çok zorladı?
5. AI veya başka kaynaklardan nasıl yararlandın?
6. Bu sistemi gerçek ortamda kullanmadan önce başka ne eklerdin?