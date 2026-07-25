# AI Intern Readiness — One-Day Challenge

Bu depo, bir iş günü içinde temel teknik hazırbulunuşluluğu artırmak ve görünür hâle getirmek için hazırlanmış uygulamalı bir görevdir.

Görev; Python, JSON, doğrulama mantığı, test okuma, Git çalışma disiplini, güvenlik farkındalığı ve teknik açıklama becerilerini birlikte çalıştırır. Dış paket kurulumu gerekmez.

## İlk yapılacaklar

1. `START_HERE.md` dosyasını baştan sona oku.
2. Ortam kontrolünü çalıştır:

Windows:
```powershell
py scripts/diagnose.py
```

macOS / Linux:
```bash
python3 scripts/diagnose.py
```

3. Başlangıç testlerini çalıştır. Testlerin bir kısmının başarısız olması beklenir:

Windows:
```powershell
py -m unittest discover -s tests -v
```

macOS / Linux:
```bash
python3 -m unittest discover -s tests -v
```

4. `TASK.md` içindeki sırayla ilerle.

## Görevin özeti

İki ana şeyi düzeltmen gerekiyor:

- `src/envelope_validator.py`: Eksik ve hatalı doğrulama kodu
- `candidate/task_envelope.json`: Kurallara uymayan görev zarfı

Ardından teslim belgelerini doldurup tüm kontrolleri geçireceksin.

## Başarı koşulu

Aşağıdaki komutun sonunda `FINAL RESULT: PASS` görülmelidir:

```bash
python3 scripts/grade.py
```

Windows'ta `python3` yerine `py` kullanabilirsin.

## Yardım almadan takılırsan

Sırasıyla şunları kullan:

1. `docs/01_CONTRACT.md`
2. Test hata mesajları
3. `docs/02_DEBUGGING_GUIDE.md`
4. `docs/03_PROGRESSIVE_HINTS.md`
5. İnternet, dokümantasyon veya AI aracı

AI kullanmak serbesttir; ancak nerede ve nasıl kullandığını `submission/AI_USAGE.md` içinde açıkça yazmalısın.

## Kısıtlar

- `tests/` ve `docs/01_CONTRACT.md` dosyalarını değiştirme.
- Gerçek API anahtarı, parola, kişisel veri veya şirket verisi ekleme.
- Testi susturmak için kod yazma; davranışı gerçekten düzelt.
- Bilmediğin noktayı uydurma. `UNKNOWN` veya `NEEDS_EVIDENCE` yazabilirsin.

## Depoyu alma

Bu görev, ayrı bir çalışma dalında tutuluyor. Şu komutlarla alabilirsin:

```bash
git clone --branch ai-intern-readiness-day-1 --single-branch https://github.com/OFCode-dev/ofcode-dev.github.io.git
cd ofcode-dev.github.io/ai-intern-readiness-day-1
```

Teslim için kendi GitHub hesabında yeni bir repo açıp bu klasörü yükleyebilir veya klasörü ZIP olarak iletebilirsin.