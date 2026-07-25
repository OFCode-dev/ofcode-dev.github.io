# Git Mini Guide

## Depoyu alma

```bash
git clone --branch ai-intern-readiness-day-1 --single-branch https://github.com/OFCode-dev/ofcode-dev.github.io.git
cd ofcode-dev.github.io/ai-intern-readiness-day-1
```

## Kendi teslim reponu oluşturma

GitHub hesabında boş bir repo oluştur. Ardından bu klasörde:

```bash
rm -rf ../.git
git init
git add .
git commit -m "complete AI intern readiness challenge"
git branch -M main
git remote add origin KENDI_REPO_URLIN
git push -u origin main
```

Windows PowerShell'da `rm -rf` yerine üst klasördeki `.git` klasörünü Dosya Gezgini ile sil veya şu komutu kullan:

```powershell
Remove-Item -Recurse -Force ..\.git
```

## Durumu görme

```bash
git status
git diff
```

## Önerilen commitler

```bash
git add src/envelope_validator.py candidate/task_envelope.json
git commit -m "implement envelope validation rules"

git add submission/
git commit -m "complete readiness challenge notes"
```

Git kullanamıyorsan görevi yine tamamla ve klasörü ZIP olarak teslim et; bunu öğrenme notunda belirt.