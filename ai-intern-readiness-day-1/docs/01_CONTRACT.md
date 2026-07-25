# Task Envelope Contract v1

Bu belge görev zarfı için tek yetkili teknik kaynaktır.

## Zorunlu alanlar

Aşağıdaki alanların tamamı bulunmalıdır:

- `task_id`
- `owner`
- `objective`
- `inputs`
- `actions`
- `artifacts`
- `status`
- `requires_human_approval`

## Alan kuralları

### `task_id`

- Tür: string
- Boş olamaz
- Yalnızca küçük İngilizce harf, sayı ve tire içerebilir
- Örnek: `classify-feedback-001`

### `owner`

- Tür: string
- Boş olamaz
- Bir kişi adı yerine sorumlu rol yazılabilir

### `objective`

- Tür: string
- En az 15 karakter olmalıdır
- Görevin çıktısını açıkça ifade etmelidir

### `inputs`

- Tür: array/list
- En az bir öğe içermelidir
- Her öğe boş olmayan string olmalıdır

### `actions`

- Tür: array/list
- En az bir öğe içermelidir
- Her öğe boş olmayan string olmalıdır

İnsan onayı gerektiren eylemler:

- `send_email`
- `delete_file`
- `publish_content`
- `modify_customer_record`
- `execute_payment`

Bu eylemlerden herhangi biri varsa `requires_human_approval` değeri `true` olmalıdır.

### `artifacts`

- Tür: array/list
- En az bir öğe içermelidir
- Her öğe göreli, güvenli bir dosya yolu olmalıdır
- Mutlak yol kullanılamaz
- `..` yol parçası kullanılamaz
- Yol `output/` ile başlamalıdır
- İzin verilen uzantılar: `.json`, `.md`, `.csv`

### `status`

Yalnızca şu değerlerden biri olabilir:

- `planned`
- `in_progress`
- `blocked`

`done` başlangıç görev zarfında kullanılamaz.

### `requires_human_approval`

- Tür: boolean
- Güvenli, yalnızca analiz ve raporlama yapan görevlerde `false` olabilir
- İnsan onayı gerektiren bir eylem varsa `true` olmalıdır

## Hata mesajı ilkeleri

- Hata mesajı alan adını içermelidir.
- Mesaj, sorunu tek cümlede açıklamalıdır.
- Aynı hata birden fazla kez üretilmemelidir.
- Doğrulama tüm hataları birlikte döndürmelidir; ilk hatada durmamalıdır.

## Örnek güvenli görev

```json
{
  "task_id": "summarize-notes-001",
  "owner": "ai-intern",
  "objective": "Toplantı notlarını kısa bir Markdown özetine dönüştür.",
  "inputs": ["data/meeting-notes.txt"],
  "actions": ["read_text", "summarize"],
  "artifacts": ["output/summary.md"],
  "status": "planned",
  "requires_human_approval": false
}
```