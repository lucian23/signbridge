# SignBridge v1.0.0

Simulator educațional de limbaj semnelor românesc (LSR) — proiect InfoEducație 2026, secțiunea Software Educațional.

## Problema identificată

23.000+ români cu deficiențe de auz au dificultăți în comunicarea cu instituțiile publice, școlile și spitalele. Interpreții LSR sunt puțini și costisitori. Nu există aplicații educaționale digitale gratuite pentru învățarea LSR în România.

## Soluția SignBridge

Aplicație desktop (Python + Tkinter/ttkbootstrap) cu:
1. **Dicționar LSR** — 500+ semne organizate pe categorii (saluturi, familie, mâncare, numere, urgențe)
2. **Modul lecții** — Lecții structurate pe dificultate, cu semne grupate tematic
3. **Quiz interactiv** — Joc de tip Duolingo: recunoaștere semn → alegere cuvânt, cu scor și progres
4. **Dicționar invers** — Tastează cuvântul → vezi descrierea semnului
5. **Mod conversație rapidă** — 20 semne esențiale pentru urgențe
6. **Tracker progres** — Statistici personale, rate de reușită per semn

## Arhitectură

```
signbridge/
  core/          — Config singleton, DatabaseManager (SQLite)
  modules/       — SignManager, LessonManager, ProgressTracker
  gui/views/     — Dashboard, Dictionary, Lessons, Quiz, Progress
  gui/widgets/   — GlassCard, NavButton (UI custom Canvas)
  tests/         — pytest (12 teste)
```

## Instalare

```bash
cd signbridge
pip install -r requirements.txt
PYTHONPATH=. python3 -m signbridge.main
```

## Testare

```bash
PYTHONPATH=. pytest signbridge/tests/test_all.py -v
```

## Analiza pieței (comparativ)

| Soluție          | Preț   | LSR    | Offline | Quiz   | Progres |
|------------------|--------|--------|---------|--------|---------|
| Lingvano (web)   | $$$    | ASL    | Nu      | Da     | Da      |
| SignSchool (web) | $$$    | ASL    | Nu      | Da     | Da      |
| SignBridge       | Gratis | Da     | Da      | Da     | Da      |

## Tehnologii

- Python 3.11, ttkbootstrap, SQLite, Pillow, pytest

## Autor

Lucian — elev, InfoEducație 2026
Toate componentele sunt de autor.
