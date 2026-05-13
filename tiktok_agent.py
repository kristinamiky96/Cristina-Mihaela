"""
Agent TikTok Copywriting AI
Campanie: Curs Inteligenta Artificiala - De la Zero la Expert
Grup tinta: Femei 25-45 ani, incepátoare cu AI
"""

import anthropic
import json
import os
from datetime import datetime
from dataclasses import dataclass
from typing import Optional


# ---------------------------------------------------------------------------
# Tipuri de continut TikTok
# ---------------------------------------------------------------------------

TIPURI_POST = {
    "educational": "Explica un concept AI pe intelesul tuturor, fara jargon tehnic",
    "motivational": "Inspira femeile sa invete AI acum, inainte sa fie prea tarziu",
    "viral_trend": "Adapteaza un trend viral TikTok la nisa AI si curs",
    "behind_scenes": "Arata cum arata viata dupa ce inveti AI (transformare reala)",
    "testimonial": "Simuleaza o marturie autentica a unei absolvente a cursului",
    "faq": "Raspunde la cea mai frecventa intrebare/obiectie despre invatatul AI",
    "demo": "Prezinta un tool AI gratuit pe care il pot folosi imediat",
    "hooks_pack": "Genereaza 10 hooks virale pentru TikTok despre AI curs",
}

SYSTEM_PROMPT = """Esti un expert in copywriting TikTok pentru piata din Romania.
Creezi continut viral pentru cursul "Inteligenta Artificiala - De la Zero la Expert".

PUBLICUL TINTA:
- Femei 25-45 ani
- Incepátoare cu AI, curioase dar speriante
- Vor sa fie relevante la job si in viata
- Limbaj: prietenos, cald, motivational, fara jargon tehnic

STRUCTURA OBLIGATORIE pentru fiecare post TikTok:

🪝 HOOK (primele 3 secunde - cel mai important):
- Trebuie sa opreasca scroll-ul instantaneu
- Incepe cu o intrebare provocatoare, o statistica socanta sau o afirmatie boldă
- MAX 10 cuvinte

📝 SCRIPT / CAPTION (corpul postarii):
- 150-300 cuvinte pentru video
- Ton conversational, ca o prietena care iti spune un secret
- Structura: problema → agitare → solutie → beneficiu concret
- Foloseste exemple concrete, nu abstractii

📢 CTA (Call-To-Action):
- 1 actiune clara si simpla
- Urgent dar fara presiune artificiala
- Exemple: "Comenteaza VREAU si iti trimit informatiile", "Link in bio"

#️⃣ HASHTAGS (15-20 hashtag-uri):
- Mix: trending + nisa + romani
- Include: #AI #IntelightaArtificiala #CursAI #FemeiInTech #DezvoltarePersonala
- Adaptat pentru algoritmul TikTok Romania

🎬 TIP VIZUAL (optional):
- Sugestie concreta pentru filmare/editare
- Ce sa apara pe ecran

Genereaza in ROMANA. Fii specific, creativ si autentic. Evita cliseele."""


# ---------------------------------------------------------------------------
# Dataclass pentru un post TikTok generat
# ---------------------------------------------------------------------------

@dataclass
class TikTokPost:
    tip: str
    parametri: dict
    continut: str
    generat_la: str


# ---------------------------------------------------------------------------
# Functia principala de generare
# ---------------------------------------------------------------------------

def genereaza_post_tiktok(
    client: anthropic.Anthropic,
    tip: str,
    parametri: Optional[dict] = None,
) -> TikTokPost:
    """
    Genereaza un post TikTok cu Claude API (streaming).

    Args:
        client: Client Anthropic initializat
        tip: Tipul de continut (cheie din TIPURI_POST)
        parametri: Parametri optionali (discount, deadline, topic etc.)

    Returns:
        TikTokPost cu continutul generat
    """
    if tip not in TIPURI_POST:
        raise ValueError(f"Tip necunoscut: '{tip}'. Alege din: {list(TIPURI_POST.keys())}")

    parametri = parametri or {}
    instructiune = TIPURI_POST[tip]

    # Construieste mesajul utilizatorului cu toti parametrii
    params_text = ""
    if parametri:
        params_text = "\n\nPARAMETRI SPECIFICI:\n"
        for cheie, valoare in parametri.items():
            params_text += f"- {cheie}: {valoare}\n"

    mesaj_user = f"""Genereaza un post TikTok de tip: {tip.upper()}
Instructiune: {instructiune}{params_text}

Respecta EXACT structura cu sectiunile: HOOK, SCRIPT/CAPTION, CTA, HASHTAGS, TIP VIZUAL.
Adapteaza tonul pentru femei 25-45 ani din Romania care vor sa invete AI."""

    print(f"\n{'='*60}")
    print(f"  GENERARE POST: {tip.upper()}")
    print(f"{'='*60}\n")

    continut_complet = ""

    # Streaming cu Claude Opus 4.7 + adaptive thinking
    with client.messages.stream(
        model="claude-opus-4-7",
        max_tokens=2048,
        thinking={"type": "adaptive"},
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": mesaj_user}],
    ) as stream:
        for event in stream:
            if event.type == "content_block_delta":
                if event.delta.type == "text_delta":
                    text = event.delta.text
                    print(text, end="", flush=True)
                    continut_complet += text

    print("\n")

    return TikTokPost(
        tip=tip,
        parametri=parametri,
        continut=continut_complet,
        generat_la=datetime.now().strftime("%d-%m-%Y %H:%M"),
    )


# ---------------------------------------------------------------------------
# Generare batch - mai multe posturi dintr-o data
# ---------------------------------------------------------------------------

def genereaza_campanie_completa(
    client: anthropic.Anthropic,
    tipuri_selectate: list[str],
    parametri_globali: Optional[dict] = None,
) -> list[TikTokPost]:
    """
    Genereaza o campanie completa de posturi TikTok.

    Args:
        client: Client Anthropic
        tipuri_selectate: Lista de tipuri de posturi dorite
        parametri_globali: Parametri comuni tuturor posturilor

    Returns:
        Lista de TikTokPost generate
    """
    posturi = []
    total = len(tipuri_selectate)

    print(f"\n{'*'*60}")
    print(f"  CAMPANIE TIKTOK - CURS AI")
    print(f"  Posturi de generat: {total}")
    print(f"{'*'*60}")

    for i, tip in enumerate(tipuri_selectate, 1):
        print(f"\n[{i}/{total}] Generez post tip: {tip}")
        try:
            post = genereaza_post_tiktok(client, tip, parametri_globali)
            posturi.append(post)
        except Exception as e:
            print(f"  EROARE la generarea postului '{tip}': {e}")

    return posturi


# ---------------------------------------------------------------------------
# Salvare rezultate
# ---------------------------------------------------------------------------

def salveaza_posturi(posturi: list[TikTokPost], filename: str = "tiktok_posts_output.txt"):
    """Salveaza posturile generate intr-un fisier text formatat."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("POSTURI TIKTOK - CURS AI DE LA ZERO LA EXPERT\n")
        f.write("=" * 65 + "\n")
        f.write(f"Campanie: Inteligenta Artificiala – De la Zero la Expert\n")
        f.write(f"Grup tinta: Femei 25-45 ani, incepátoare cu AI\n")
        f.write(f"Generat la: {datetime.now().strftime('%d-%m-%Y %H:%M')}\n")
        f.write("=" * 65 + "\n\n")

        for i, post in enumerate(posturi, 1):
            f.write(f"\n{'─'*60}\n")
            f.write(f"POST #{i} – TIP: {post.tip.upper()}\n")
            if post.parametri:
                f.write(f"Parametri: {json.dumps(post.parametri, ensure_ascii=False)}\n")
            f.write(f"Generat la: {post.generat_la}\n")
            f.write(f"{'─'*60}\n\n")
            f.write(post.continut)
            f.write("\n\n")

        f.write(f"\n{'='*65}\n")
        f.write(f"Total posturi generate: {len(posturi)}\n")

    print(f"\n✓ Posturi salvate in: {filename}")


def afiseaza_rezumat(posturi: list[TikTokPost]):
    """Afiseaza un rezumat al posturilor generate."""
    print(f"\n{'='*60}")
    print(f"  REZUMAT CAMPANIE")
    print(f"{'='*60}")
    print(f"Total posturi generate: {len(posturi)}")
    print("\nPosturi create:")
    for i, post in enumerate(posturi, 1):
        preview = post.continut[:80].replace("\n", " ").strip()
        print(f"  {i:2}. [{post.tip.upper()}] {preview}...")
    print(f"{'='*60}\n")


# ---------------------------------------------------------------------------
# Interfata interactiva simpla
# ---------------------------------------------------------------------------

def meniu_interactiv(client: anthropic.Anthropic):
    """Meniu interactiv pentru selectia tipului de post."""
    print("\n" + "="*60)
    print("  AGENT TIKTOK COPYWRITING AI")
    print("  Curs: Inteligenta Artificiala - De la Zero la Expert")
    print("="*60)
    print("\nTipuri de posturi disponibile:\n")
    for i, (tip, descriere) in enumerate(TIPURI_POST.items(), 1):
        print(f"  {i:2}. {tip.upper():20} - {descriere[:45]}...")

    print(f"\n  {len(TIPURI_POST)+1:2}. CAMPANIE COMPLETA     - Genereaza toate tipurile")
    print(f"  {len(TIPURI_POST)+2:2}. IESIRE")

    print("\n" + "-"*60)
    alegere = input("Alege optiunea (1-10): ").strip()

    try:
        optiune = int(alegere)
    except ValueError:
        print("Optiune invalida.")
        return

    tipuri_lista = list(TIPURI_POST.keys())

    # Parametri comuni pentru campanie
    parametri = {
        "discount": "40%",
        "deadline": "48 ore",
        "locuri_ramase": 12,
        "pret_normal": "997 RON",
        "pret_redus": "597 RON",
        "durata_curs": "30 zile",
        "nivel": "de la zero, fara experienta anterioara",
    }

    if 1 <= optiune <= len(tipuri_lista):
        tip_ales = tipuri_lista[optiune - 1]
        post = genereaza_post_tiktok(client, tip_ales, parametri)
        salveaza_posturi([post])

    elif optiune == len(tipuri_lista) + 1:
        posturi = genereaza_campanie_completa(client, tipuri_lista, parametri)
        afiseaza_rezumat(posturi)
        salveaza_posturi(posturi)

    elif optiune == len(tipuri_lista) + 2:
        print("La revedere!")

    else:
        print("Optiune invalida.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("EROARE: Variabila de mediu ANTHROPIC_API_KEY nu este setata.")
        print("Seteaza-o cu: export ANTHROPIC_API_KEY='cheia-ta'")
        return

    client = anthropic.Anthropic(api_key=api_key)

    # Demo implicit: genereaza 3 posturi reprezentative
    print("\n" + "="*60)
    print("  AGENT TIKTOK COPYWRITING AI – DEMO")
    print("  Curs: Inteligenta Artificiala - De la Zero la Expert")
    print("="*60)
    print("\nMod demo: generez 3 posturi reprezentative...")
    print("(Pentru mod interactiv, apeleaza: meniu_interactiv(client))\n")

    parametri_demo = {
        "discount": "40%",
        "deadline": "48 ore",
        "locuri_ramase": 12,
        "pret_redus": "597 RON",
        "durata_curs": "30 zile",
        "nivel": "de la zero, fara experienta anterioara",
    }

    tipuri_demo = ["hooks_pack", "motivational", "faq"]
    posturi = genereaza_campanie_completa(client, tipuri_demo, parametri_demo)
    afiseaza_rezumat(posturi)
    salveaza_posturi(posturi)


if __name__ == "__main__":
    main()
