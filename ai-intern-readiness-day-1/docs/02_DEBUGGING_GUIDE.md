# Debugging Guide

## Python bulunamadı

### Windows

```powershell
py --version
python --version
```

İkisinden çalışanı kullan. Hiçbiri çalışmıyorsa Python 3.10 veya daha yeni bir sürüm kur ve kurulum sırasında “Add Python to PATH” seçeneğini işaretle.

### macOS / Linux

```bash
python3 --version
```

## JSON okunamıyor

Sık nedenler:

- Son alandan sonra fazladan virgül
- Çift tırnak yerine tek tırnak
- Eksik kapanış süslü parantezi
- Boolean değerinin `True`/`False` yazılması; JSON içinde `true`/`false` kullanılmalıdır

Dosyayı tek başına kontrol etmek için:

```bash
python3 -m json.tool candidate/task_envelope.json
```

Windows'ta `python3` yerine `py` kullanabilirsin.

## Tek bir testi çalıştırma

```bash
python3 -m unittest tests.test_validator.ValidatorTests.test_required_fields -v
```

## Hata mesajlarını anlamlandırma

- `AssertionError`: Testin beklediği sonuç ile kodun ürettiği sonuç farklıdır.
- `TypeError`: Kod yanlış veri türü üzerinde işlem yapıyor olabilir.
- `KeyError`: Olmayan bir sözlük alanına doğrudan erişilmiş olabilir.
- `JSONDecodeError`: JSON söz dizimi geçersizdir.

## Güvenli ilerleme yöntemi

Her seferinde tek bir kuralı düzelt. Büyük bir değişiklik yaptıktan sonra hangi düzeltmenin işe yaradığını anlamak zorlaşır.