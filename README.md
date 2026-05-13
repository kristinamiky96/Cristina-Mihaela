# Toolkit Marketing AI – Curs Inteligenta Artificiala

Colectie de unelte Python pentru campania cursului **Inteligenta Artificiala – De la Zero la Expert**.

## Grup tinta
- Femei 25–45 ani, incepátoare cu AI

---

## 1. Agent TikTok Copywriting AI (`tiktok_agent.py`)

Agent AI alimentat de **Claude Opus 4.7** care genereaza posturi TikTok virale pentru promovarea cursului.

### Caracteristici

- **8 tipuri de continut** TikTok generat dinamic:
  - `hooks_pack` – 10 hooks virale stoppers de scroll
  - `educational` – explica AI fara jargon tehnic
  - `motivational` – inspira publicul sa actioneze
  - `viral_trend` – adapteaza trenduri TikTok la nisa AI
  - `behind_scenes` – transformarea reala dupa curs
  - `testimonial` – marturii autentice simulate
  - `faq` – raspunsuri la obiectii frecvente
  - `demo` – tool AI gratuit, demo live
- **Streaming in timp real** – vezi textul generat caracter cu caracter
- **Claude Opus 4.7 + Adaptive Thinking** – calitate maxima a copywriting-ului
- **Structura obligatorie** pentru fiecare post:
  - Hook (3 secunde – opreste scroll-ul)
  - Script/Caption (150-300 cuvinte)
  - CTA (Call-To-Action)
  - Hashtags (15-20, optimizate pentru Romania)
  - Tip vizual (sugestie filmare)
- **Campanie completa** – genereaza toate tipurile dintr-o comanda
- **Export automat** in `tiktok_posts_output.txt`

### Prerequisite

```bash
pip install anthropic
export ANTHROPIC_API_KEY="cheia-ta-api"
```

### Utilizare – Demo (3 posturi automat)

```bash
python3 tiktok_agent.py
```

### Utilizare – Programatica

```python
import anthropic
from tiktok_agent import genereaza_post_tiktok, genereaza_campanie_completa, salveaza_posturi

client = anthropic.Anthropic()

# Un singur post
parametri = {
    "discount": "40%",
    "deadline": "48 ore",
    "locuri_ramase": 12,
    "pret_redus": "597 RON",
    "durata_curs": "30 zile",
}

post = genereaza_post_tiktok(client, "motivational", parametri)

# Campanie completa
posturi = genereaza_campanie_completa(
    client,
    tipuri_selectate=["hooks_pack", "educational", "faq", "testimonial"],
    parametri_globali=parametri,
)
salveaza_posturi(posturi)
```

### Utilizare – Meniu Interactiv

```python
from tiktok_agent import meniu_interactiv
import anthropic

client = anthropic.Anthropic()
meniu_interactiv(client)
```

### Tipuri de posturi disponibile

| Tip | Scop |
|---|---|
| `hooks_pack` | 10 hooks virale pentru oprirea scroll-ului |
| `educational` | Explica un concept AI pe intelesul tuturor |
| `motivational` | Inspira femeile sa invete AI acum |
| `viral_trend` | Adapteaza trenduri TikTok la nisa AI |
| `behind_scenes` | Arata transformarea reala dupa curs |
| `testimonial` | Marturie autentica a unei absolvente |
| `faq` | Raspunde la obiectii frecvente |
| `demo` | Prezinta un tool AI gratuit |

---

## 2. Generator Subiecte Email (`email_subject_generator.py`)

Generator de subiecte de email personalizate cu elemente de urgenta.

### Caracteristici

- **19 subiecte** grupate in 4 categorii:
  - Urgenta Pura
  - Curiozitate + Urgenta
  - Beneficiu + Urgenta
  - Empowerment + Urgenta
- Personalizare cu **prenumele** destinatarei
- Element de **urgenta dinamica** (ore ramase, data expirare, locuri disponibile)
- Export automat in `subjects_output.txt`

### Utilizare

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

---

## 3. Template-uri Email Complete (`email_templates.py`)

Template-uri complete pentru cele 4 categorii de email din campanie.

---

## Output Files

| Fisier | Continut |
|---|---|
| `tiktok_posts_output.txt` | Posturi TikTok generate |
| `subjects_output.txt` | Subiecte de email generate |
