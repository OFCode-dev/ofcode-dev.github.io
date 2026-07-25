# Progressive Hints

İpuçlarını sırayla kullan. Bir ipucu yeterliyse daha aşağıya geçme.

## İpucu 1 — Zorunlu alanlar

Bir listedeki her alanın sözlükte bulunup bulunmadığını `for` döngüsüyle kontrol edebilirsin.

## İpucu 2 — Tür kontrolü

Python'da:

- string: `isinstance(value, str)`
- list: `isinstance(value, list)`
- boolean: `isinstance(value, bool)`

## İpucu 3 — Boş metin

Bir string yalnızca boşluklardan oluşuyorsa `value.strip()` boş string döndürür.

## İpucu 4 — Güvenli eylem

`actions` listesini bir kümeyle kesiştirerek riskli eylem olup olmadığını bulabilirsin:

```python
set(actions) & HUMAN_APPROVAL_ACTIONS
```

## İpucu 5 — Yol güvenliği

`pathlib.PurePosixPath` kullanabilirsin. Yol parçaları içinde `..` olmamalıdır. Ayrıca yol `/` ile başlamamalıdır.

## İpucu 6 — Tüm hataları toplama

Her doğrulama fonksiyonu `list[str]` döndürsün. Ana fonksiyon bu listeleri `extend` ile birleştirsin.

## İpucu 7 — Aday dosya

Aday görevin amacı müşteri geri bildirimlerini sınıflandırmak ve rapor üretmek olarak kalmalı. Dış sisteme e-posta gönderme veya kayıt değiştirme eylemine gerek yoktur.