# Generator Subiecte Email Personalizate

Generator Python pentru subiecte de email targetate pe campania cursului **Inteligenta Artificiala – De la Zero la Expert**.

## Grup tinta
- Femei 25–45 ani, incepátoare cu AI

## Caracteristici

- **19 subiecte** grupate in 4 categorii:
  - Urgenta Pura
  - Curiozitate + Urgenta
  - Beneficiu + Urgenta
  - Empowerment + Urgenta
- Personalizare cu **prenumele** destinatarei
- Element de **urgenta dinamica** (ore ramase, data expirare, locuri disponibile)
- Export automat in `subjects_output.txt`

## Utilizare

```bash
python3 email_subject_generator.py
```

### Personalizare parametri

Modifica valorile din functia `main()`:

```python
name = "Maria"          # Prenumele destinatarei
deadline_hours = 24     # Ore ramase pana la expirare
discount = 40           # Procentul de reducere
spots_left = 7          # Locuri ramase disponibile
```

### Utilizare programatica

```python
from email_subject_generator import generate_subjects

subjects = generate_subjects(
    name="Ana",
    deadline_hours=48,
    discount=30,
    spots_left=10
)

for category, lines in subjects.items():
    for subject in lines:
        print(subject)
```

## Output

Subiectele sunt afisate in terminal si salvate automat in `subjects_output.txt`.
