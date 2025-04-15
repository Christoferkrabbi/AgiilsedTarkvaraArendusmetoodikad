name: Python CI  # See on töövoo (workflow) nimi, mida näed GitHubi Actions vaates

on: [push]  # Töövoog käivitub iga kord, kui tehakse push (koodi üleslaadimine) GitHubi

jobs:
  build:  # Töö nimega "build"
    runs-on: ubuntu-latest  # GitHub loob virtuaalmasina, kus töö käivitatakse (Ubuntu Linux)

    steps:  # Siin on kõik sammud, mida GitHub teeb järjest
      - uses: actions/checkout@v2  # Laeb sinu projekti koodi GitHubi repositooriumist virtuaalmasinasse

      - name: Paigalda Python
        uses: actions/setup-python@v2  # Kasutab ametlikku GitHubi action'it Python'i paigaldamiseks
        with:
          python-version: 3.9  # Määrab, millist Python versiooni kasutatakse (näiteks 3.9)

      - name: Paigalda sõltuvused
        run: pip install pytest  # Käivitab käsu, mis paigaldab testimiseks vajaliku pytest'i

      - name: Käivita testid
        run: pytest  # Käivitab kõik testid failidest, mille nimi algab test_ ja sisaldab testfunktsioone
