"""
Templateuri Complete de Email - Campanie Curs AI
================================================
Grup tinta: Femei 25-45 ani, incepătoare cu AI
Cele 4 categorii: Urgenta Pura | Curiozitate+Urgenta |
                  Beneficiu+Urgenta | Empowerment+Urgenta
"""

from datetime import datetime, timedelta


def render_urgenta_pura(name: str, deadline_hours: int, discount: int, spots_left: int) -> dict:
    """
    CATEGORIE 1 – URGENTA PURA
    Psihologie: Frica de a pierde. Mesaj direct, fara povestire.
    Ton: Alerta, presant, concis.
    """
    deadline_label = f"{deadline_hours}h" if deadline_hours >= 1 else "cateva minute"
    deadline_date = (datetime.now() + timedelta(hours=deadline_hours)).strftime("%d %B, ora %H:%M")

    subject = f"{name}, mai ai doar {deadline_label} sa te inscrii la cursul AI!"

    body = f"""Salut, {name}!

⏰ MAI AI DOAR {deadline_label.upper()} SA ACTIONEZI.

Inscrierea la cursul nostru „De la Zero la Expert in AI"
se INCHIDE la {deadline_date}.

Nu este o tactica de marketing. Este termenul real.
Dupa aceea, pretul revine la normal si locurile se bloheaza.

Ce obtii daca te inscrii ACUM:
  ✔ {discount}% reducere fata de pretul standard
  ✔ Acces pe viata la toate materialele cursului
  ✔ Certificat de absolvire recunoscut
  ✔ Comunitate privata de femei in tech

Mai sunt doar {spots_left} locuri disponibile.

👉 [INSCRIE-TE ACUM – {deadline_label} RAMASE]

Daca nu actionezi pana la {deadline_date},
vei plati mai mult sau nu vei mai prinde loc.

{name}, decizia iti apartine.

Cu drag,
Echipa Curs AI


P.S. Serios – {deadline_label}. Ceasul ticaie.
"""
    return {"subject": subject, "body": body, "category": "Urgenta Pura"}


def render_curiozitate_urgenta(name: str, deadline_hours: int, discount: int, spots_left: int) -> dict:
    """
    CATEGORIE 2 – CURIOZITATE + URGENTA
    Psihologie: Starneste intrebari, apoi ofera raspunsul DOAR daca actioneaza rapid.
    Ton: Intrigant, conversational, cu urgenta subtila la final.
    """
    deadline_label = f"{deadline_hours}h" if deadline_hours >= 1 else "cateva minute"

    subject = f"Femeile care stiu AI castiga mai mult. Tu poti fi una dintre ele – {deadline_label} mai ai"

    body = f"""Buna, {name}!

Stiai ca femeile care folosesc AI la job castiga in medie
cu 34% mai mult decat colegele lor care nu il folosesc?

Nu pentru ca sunt mai destepte.
Nu pentru ca au un doctorat in informatica.

Ci pentru ca au invatat un singur lucru:
cum sa puna AI-ul sa munceasca pentru ele.

Gestioneaza rapoarte in 10 minute in loc de 3 ore.
Scriu propuneri, emailuri, prezentari in fractiuni de timp.
Iau decizii mai bune, mai repede, cu mai putina energie.

{name}, tu poti fi una dintre ele.

Cursul nostru „De la Zero la Expert in AI" te duce
de la „habar nu am" la „pot face asta singura" in 30 de zile.

FARA experienta anterioara necesara.
FARA matematica sau programare.
DOAR aplicatii practice, pas cu pas.

👉 [VREAU SA FIU SI EU UNA DINTRE ELE]

⚠️  Oferta speciala cu {discount}% reducere expira in {deadline_label}.
    Mai sunt {spots_left} locuri disponibile la pretul acesta.

Curiozitatea ta este primul pas.
Pasul doi il faci tu.

Cu drag,
Echipa Curs AI


P.S. Inca te intrebi „oare e pentru mine?"
     Raspunsul scurt: Da. Mai ales pentru tine.
"""
    return {"subject": subject, "body": body, "category": "Curiozitate + Urgenta"}


def render_beneficiu_urgenta(name: str, deadline_hours: int, discount: int, spots_left: int) -> dict:
    """
    CATEGORIE 3 – BENEFICIU + URGENTA
    Psihologie: Arata valoarea concreta + deadline clar.
    Ton: Practic, orientat spre rezultate, motivant.
    """
    deadline_label = f"{deadline_hours}h" if deadline_hours >= 1 else "cateva minute"
    deadline_date = (datetime.now() + timedelta(hours=deadline_hours)).strftime("%d %B, ora %H:%M")

    subject = f"De la 0 la expert in AI in 30 zile – {discount}% reducere, expira azi"

    body = f"""Salut, {name}!

In exact 30 de zile, poti trece:

  ACUM                        →    DUPA 30 ZILE
  ─────────────────────────────────────────────
  „Nu stiu nimic despre AI"   →    Folosesti AI zilnic la job
  Ore pierdute pe taskuri     →    Automatizezi in minute
  Nesiguranta in cariera      →    Competenta confirmata
  Salariu stagnant            →    Argumente reale pentru avans

Cursul „De la Zero la Expert in AI" este construit
special pentru femei ca tine – fara background tehnic,
cu viata aglomerata, cu dorinta de a avansa.

CE PRIMESTI:
  📚  8 module video (acces pe viata)
  🛠️  30+ exercitii practice cu AI real
  💬  Comunitate privata + sesiuni live lunare
  📜  Certificat de absolvire
  🎁  Bonus: „Top 50 Prompturi AI pentru cariera ta"

PRETUL NORMAL: [pret full]
PRETUL TAU AZI: {discount}% REDUCERE

Aceasta reducere expira la {deadline_date}.
Nu se prelungeste. Nu se repeta.

👉 [VREAU {discount}% REDUCERE – MA INSCRIU ACUM]

{name}, beneficiul este clar.
Acum depinde de tine sa il iei.

Cu respect si incredere in potentialul tau,
Echipa Curs AI


P.S. {spots_left} locuri ramase la pretul redus.
     Dupa aceea, pretul normal se aplica automat.
"""
    return {"subject": subject, "body": body, "category": "Beneficiu + Urgenta"}


def render_empowerment_urgenta(name: str, deadline_hours: int, discount: int, spots_left: int) -> dict:
    """
    CATEGORIE 4 – EMPOWERMENT + URGENTA
    Psihologie: Inspira si valideaza femeia, pune AI ca instrument al puterii ei.
    Ton: Inspirational, cald, cu sens de misiune colectiva + deadline ca oportunitate.
    """
    deadline_label = f"{deadline_hours}h" if deadline_hours >= 1 else "cateva minute"
    deadline_date = (datetime.now() + timedelta(hours=deadline_hours)).strftime("%d %B, ora %H:%M")

    subject = f"Viitorul apartine femeilor care stiu AI. Incepe astazi – {deadline_label} ramase"

    body = f"""Buna, {name}!

Trăim un moment unic in istorie.

Tehnologia AI nu este un moft al viitorului.
Este unealta prezentului. Iar femeile care o stapanesc acum
vor fi cele care definesc cum arata urmatorul deceniu.

Nu vorbim despre programare.
Nu vorbim despre robotica sau laboratoare de cercetare.

Vorbim despre puterea de a-ti gestiona mai eficient cariera,
de a produce mai mult in mai putin timp,
de a fi vocea competenta din camera.

{name}, tu esti exact femeia pentru care am construit
cursul „De la Zero la Expert in AI".

Pentru ca tu stii ca vrei mai mult.
Pentru ca tu nu vrei sa ramana in urma.
Pentru ca tu intelegi ca schimbarea incepe cu un singur pas.

Astazi, acel pas costa cu {discount}% mai putin.

✨ Incepe-ti transformarea inainte de {deadline_date}.

👉 [DA – VREAU SA FAC PARTE DIN VIITOR]

Femeile care se alatura astazi nu iti vor fi colege.
Iti vor fi inspiratia.

Cu drag si admiratie,
Echipa Curs AI


P.S. {deadline_label} ramase si {spots_left} locuri disponibile.
     Viitorul nu asteapta – dar nici tu nu trebuie.
"""
    return {"subject": subject, "body": body, "category": "Empowerment + Urgenta"}


def generate_all_emails(name: str = "Maria", deadline_hours: int = 24,
                        discount: int = 40, spots_left: int = 7) -> list:
    """Genereaza toate cele 4 emailuri complete."""
    return [
        render_urgenta_pura(name, deadline_hours, discount, spots_left),
        render_curiozitate_urgenta(name, deadline_hours, discount, spots_left),
        render_beneficiu_urgenta(name, deadline_hours, discount, spots_left),
        render_empowerment_urgenta(name, deadline_hours, discount, spots_left),
    ]


def display_all_emails(emails: list):
    """Afiseaza toate emailurile in consola."""
    separator = "=" * 65
    for i, email in enumerate(emails, 1):
        print(separator)
        print(f"  EMAIL {i}/4 – {email['category'].upper()}")
        print(separator)
        print(f"\nSUBIECT: {email['subject']}\n")
        print("CORP EMAIL:")
        print("-" * 65)
        print(email["body"])

    print(separator)
    print(f"  Total: {len(emails)} emailuri complete generate.")
    print(separator)


def save_emails_to_file(emails: list, filename: str = "emails_complete.txt"):
    """Salveaza emailurile complete intr-un fisier text."""
    separator = "=" * 65
    with open(filename, "w", encoding="utf-8") as f:
        f.write("EMAILURI COMPLETE – CAMPANIE CURS AI\n")
        f.write(f"Generat la: {datetime.now().strftime('%d-%m-%Y %H:%M')}\n")
        f.write(separator + "\n\n")

        for i, email in enumerate(emails, 1):
            f.write(f"\n{'=' * 65}\n")
            f.write(f"  EMAIL {i}/4 – {email['category'].upper()}\n")
            f.write(f"{'=' * 65}\n")
            f.write(f"\nSUBIECT: {email['subject']}\n")
            f.write("\nCORP EMAIL:\n")
            f.write("-" * 65 + "\n")
            f.write(email["body"])

        f.write(f"\n{'=' * 65}\n")
        f.write(f"Total: {len(emails)} emailuri complete generate.\n")


if __name__ == "__main__":
    emails = generate_all_emails(
        name="Maria",
        deadline_hours=24,
        discount=40,
        spots_left=7,
    )
    display_all_emails(emails)
    save_emails_to_file(emails, "emails_complete.txt")
    print("\nEmailurile complete au fost salvate in: emails_complete.txt")
