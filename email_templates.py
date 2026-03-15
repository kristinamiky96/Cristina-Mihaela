"""
Emailuri Complete Gata de Trimis – Campanie Curs AI
====================================================
Curs: „De la Zero la Expert in AI in 30 de Zile"
Grup tinta: Femei 25-45 ani, incepătoare cu AI
Cele 4 categorii de email:
  1. Urgenta Pura
  2. Curiozitate + Urgenta
  3. Beneficiu + Urgenta
  4. Empowerment + Urgenta
"""

from datetime import datetime, timedelta


# ─────────────────────────────────────────────────────────
# EMAIL 1 – URGENTA PURA
# ─────────────────────────────────────────────────────────

def render_urgenta_pura(name: str, deadline_hours: int, discount: int, spots_left: int) -> dict:
    """
    Psihologie: FOMO (frica de a pierde). Fara poveste, fara introducere lunga.
    Ton: Urgent, direct, alarm-style. Fiecare rand conteaza.
    Structura: Subiect-soc → Countdown vizibil → Ce pierzi → CTA → P.S. presant
    """
    deadline_label = f"{deadline_hours}h" if deadline_hours >= 1 else "cateva minute"
    deadline_date = (datetime.now() + timedelta(hours=deadline_hours)).strftime("%d %B, ora %H:%M")

    subject    = f"{name}, mai ai doar {deadline_label} sa te inscrii la cursul AI!"
    preheader  = f"Dupa {deadline_date} pretul revine la normal. Fara exceptii."

    body = f"""\
De la: Echipa Curs AI <hello@cursai.ro>
Catre: {name}
Subiect: {subject}
Pre-header: {preheader}

──────────────────────────────────────────────────────────────

Salut, {name},

⏰ {deadline_label.upper()} RAMASE. Atat.

La {deadline_date}, inscrierea la cursul
„De la Zero la Expert in AI" se INCHIDE definitiv.

Nu este un artificiu de marketing.
Este termenul real al campaniei noastre.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CE SE INTAMPLA DACA NU ACTIONEZI AZI:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖  Pierzi reducerea de {discount}% – platesti pretul intreg
  ✖  Pierzi accesul la grupul privat de femei in AI
  ✖  Pierzi bonus-ul „Top 50 Prompturi AI" (valoare 197 lei)
  ✖  Pierzi unul dintre cele {spots_left} locuri ramase

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CE SE INTAMPLA DACA TE INSCRII ACUM:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✔  {discount}% reducere aplicata instant la plata
  ✔  Acces imediat la toate cele 8 module video
  ✔  30 de zile de exercitii practice cu AI real
  ✔  Certificat de absolvire recunoscut
  ✔  Comunitate privata + sesiuni live lunare
  ✔  Garantie 14 zile – daca nu esti multumita, iti returnam banii

Locuri ramase: {spots_left} din 50.
Termen limita: {deadline_date}.

──────────────────────────────────────────────────────────────

  👉  [ INSCRIE-TE ACUM CU {discount}% REDUCERE ]
       Link: https://cursai.ro/inscriere

──────────────────────────────────────────────────────────────

{name}, nu am creat acest curs ca sa-l vindem.
L-am creat ca sa schimbam felul in care femeile
se raporteaza la tehnologie.

Dar nu putem pastra pretul redus la nesfarsit.

La {deadline_date} usa se inchide.

Cu drag,
Andreea Ionescu
Fondatoare Curs AI
📞 0720 XXX XXX | hello@cursai.ro
🌐 www.cursai.ro

──────────────────────────────────────────────────────────────

P.S. Daca citesti acest email si inca eziti —
     intreaba-te: cum ma voi simti maine dimineata
     daca nu ma inscriu azi?
     {deadline_label} ramase, {name}. Ceasul ticaie.

P.P.S. Garantie completa 14 zile. Daca nu esti multumita,
       iti returnam 100% din suma platita. Zero risc.

──────────────────────────────────────────────────────────────
Ai primit acest email pentru ca te-ai abonat la lista noastra.
[Dezabonare] | [Modifica preferinte] | cursai.ro
"""
    return {
        "category":   "Urgenta Pura",
        "subject":    subject,
        "preheader":  preheader,
        "body":       body,
    }


# ─────────────────────────────────────────────────────────
# EMAIL 2 – CURIOZITATE + URGENTA
# ─────────────────────────────────────────────────────────

def render_curiozitate_urgenta(name: str, deadline_hours: int, discount: int, spots_left: int) -> dict:
    """
    Psihologie: Deschide cu un fapt socant, construieste curiozitate,
    raspunde treptat, urgenta apare natural la final ca o consecinta logica.
    Ton: Conversational, intrigant, cald — ca o prietena care iti spune un secret.
    Structura: Statistica soc → Poveste → Revelatie → Curs → Urgenta → CTA → P.S.
    """
    deadline_label = f"{deadline_hours}h" if deadline_hours >= 1 else "cateva minute"
    deadline_date  = (datetime.now() + timedelta(hours=deadline_hours)).strftime("%d %B, ora %H:%M")

    subject   = f"Femeile care stiu AI castiga mai mult. Tu poti fi una dintre ele – {deadline_label} mai ai"
    preheader = "Nu e vorba de geniu. E vorba de un singur instrument pe care il poti invata in 30 de zile."

    body = f"""\
De la: Echipa Curs AI <hello@cursai.ro>
Catre: {name}
Subiect: {subject}
Pre-header: {preheader}

──────────────────────────────────────────────────────────────

Buna, {name},

Lasa-ma sa iti spun despre Raluca.

Raluca are 34 de ani, lucreaza in marketing si pana acum
un an credea ca AI este „pentru programatori si oameni
din Silicon Valley."

Azi, Raluca:
  → Genereaza rapoarte lunare in 12 minute (inainte: 4 ore)
  → A primit o marire de salariu de 28% dupa ce a demonstrat
     ca poate livra de 3 ori mai mult in acelasi timp
  → Conduce un curs intern la firma ei despre AI
  → Doarme mai bine noaptea — stie ca nu va ramane in urma

Ce s-a schimbat?

A invatat AI. Nu programare. Nu algoritmi.
Ci cum sa foloseasca instrumentele AI existente
pentru munca ei de zi cu zi.

──────────────────────────────────────────────────────────────

{name}, iti spun sincer:

Conform unui studiu McKinsey (2024), femeile care
integreaza AI in activitatea profesionala castiga
in medie cu 34% mai mult decat colegele lor
care nu folosesc aceste instrumente.

Nu pentru ca sunt mai inteligente.
Nu pentru ca au un background tehnic.

Ci pentru ca au facut un singur lucru:
au ales sa invete.

Acum incerc sa iti dau tie aceeasi sansa.

──────────────────────────────────────────────────────────────

  „De la Zero la Expert in AI in 30 de Zile"
  ─────────────────────────────────────────

  Un curs construit special pentru femei ca tine:
  fara background tehnic, cu viata incarcata,
  cu ambitia de a face mai mult.

  In 30 de zile vei stii sa:
  ✦ Automatizezi taskuri repetitive cu AI
  ✦ Scrii texte, rapoarte si emailuri de 5x mai rapid
  ✦ Analizezi date si iei decizii mai bune
  ✦ Creezi prezentari profesionale in minute
  ✦ Folosesti AI ca asistent personal de cariera

  Fara jargon tehnic. Fara matematica.
  Doar aplicatii practice pe care le folosesti a doua zi.

──────────────────────────────────────────────────────────────

  👉  [ VREAU SA FIU SI EU UNA DINTRE ELE ]
       Link: https://cursai.ro/inscriere

──────────────────────────────────────────────────────────────

⚠️  Un singur lucru inainte sa inchizi emailul:

Oferta speciala cu {discount}% reducere este valabila
doar pana la {deadline_date}.

Mai sunt {spots_left} locuri disponibile la pretul acesta.

Dupa aceea, pretul revine la normal —
si nu stim cand vom mai lansa o alta campanie.

Curiozitatea care te-a facut sa deschizi acest email
este exact ce ai nevoie ca sa faci pasul urmator.

Ascult-o.

Cu drag,
Andreea Ionescu
Fondatoare Curs AI
📞 0720 XXX XXX | hello@cursai.ro
🌐 www.cursai.ro

──────────────────────────────────────────────────────────────

P.S. Inca iti pui intrebarea „oare e pentru mine?"

     Iti raspund eu: daca ai deschis acest email si ai
     citit pana aici — raspunsul este DA.
     Oamenii care nu sunt interesati nu citesc pana la P.S.
     Tu esti interesata. Acum actioneaza.

     {deadline_label} mai ai. [ MA INSCRIU ACUM ]

──────────────────────────────────────────────────────────────
Ai primit acest email pentru ca te-ai abonat la lista noastra.
[Dezabonare] | [Modifica preferinte] | cursai.ro
"""
    return {
        "category":   "Curiozitate + Urgenta",
        "subject":    subject,
        "preheader":  preheader,
        "body":       body,
    }


# ─────────────────────────────────────────────────────────
# EMAIL 3 – BENEFICIU + URGENTA
# ─────────────────────────────────────────────────────────

def render_beneficiu_urgenta(name: str, deadline_hours: int, discount: int, spots_left: int) -> dict:
    """
    Psihologie: Arata transformarea concreta (inainte/dupa), calculeaza ROI-ul,
    detaliaza tot ce primeste. Urgenta e prezentata ca o oportunitate limitata rational.
    Ton: Practic, clar, orientat spre rezultate. Ca un consultant care iti explica o oferta.
    Structura: Transformare vizuala → Ce primesti detaliat → ROI → Pret → Deadline → CTA → P.S.
    """
    deadline_label = f"{deadline_hours}h" if deadline_hours >= 1 else "cateva minute"
    deadline_date  = (datetime.now() + timedelta(hours=deadline_hours)).strftime("%d %B, ora %H:%M")

    subject   = f"De la 0 la expert in AI in 30 zile – {discount}% reducere, expira azi"
    preheader = f"Iata exact ce primesti, cat valoreza si de ce oferta expira la {deadline_date}."

    body = f"""\
De la: Echipa Curs AI <hello@cursai.ro>
Catre: {name}
Subiect: {subject}
Pre-header: {preheader}

──────────────────────────────────────────────────────────────

Salut, {name},

Iti prezint cei mai importanti 30 de zile
din cariera ta profesionala.

──────────────────────────────────────────────────────────────

  UNDE ESTI AZI          →   UNDE VEI FI DUPA 30 ZILE
  ──────────────────────────────────────────────────────
  „Nu stiu nimic          →   Folosesti AI zilnic,
   despre AI"                 cu incredere deplina

  Taskuri repetitive      →   Automatizate. Tu te ocupi
  iti consuma ore             de ce conteaza cu adevarat

  Prezentari si           →   Gata in 20 de minute,
  rapoarte = cosmar           profesionale, impresionante

  Nesiguranta in          →   Competenta certificata,
  cariera                     recunoscuta de angajatori

  Salariu stagnant        →   Argumente reale si concrete
                              pentru o marire meritate

──────────────────────────────────────────────────────────────

  CE PRIMESTI IN CURSUL „DE LA ZERO LA EXPERT IN AI"
  ───────────────────────────────────────────────────

  📚  8 MODULE VIDEO – ACCES PE VIATA
      De la introducere in AI pana la automatizari avansate.
      Inveti in ritmul tau, ori cand, de pe orice dispozitiv.

  🛠️  30+ EXERCITII PRACTICE CU AI REAL
      Nu teorie. Fiecare lectie are un exercitiu aplicabil
      direct in munca ta de zi cu zi.

  💬  COMUNITATE PRIVATA DE FEMEI IN AI
      Grup exclusiv in care iti poti pune intrebari,
      impartasi progresul si primi feedback de la colege
      si de la instructori.

  📅  4 SESIUNI LIVE LUNARE CU INSTRUCTORII
      Intrebari in timp real, cazuri practice, actualizari
      despre cele mai noi instrumente AI.

  📜  CERTIFICAT DE ABSOLVIRE RECUNOSCUT
      Demonstreaza angajatorului tau ca esti pregatita
      pentru economia digitala.

  🎁  BONUS 1: „Top 50 Prompturi AI pentru Cariera Ta"
      Ghid practic cu promturile exacte pe care sa le
      folosesti in munca ta. Valoare: 197 lei. GRATUIT.

  🎁  BONUS 2: „Planul Tau de 30 de Zile"
      Calendarul zilnic cu ce sa faci, pas cu pas,
      ca sa nu te pierzi si sa avansezi constant.

──────────────────────────────────────────────────────────────

  CALCULUL SIMPLU AL ROI-ULUI
  ─────────────────────────────
  O marire de salariu de 10% (conservator, post-curs)
  inseamna sute de lei in plus in fiecare luna.
  Cursul se „plateste singur" in primele 30-60 de zile.

  Plus: timpul economisit zilnic prin automatizari.
  2 ore/zi × 5 zile/saptamana = 40 ore/luna eliberate.
  Ce ai face tu cu 40 de ore in plus in fiecare luna?

──────────────────────────────────────────────────────────────

  PRETUL TAU AZI:
  ─────────────────
  Pret normal:   [XXX lei]
  Reducere:      -{discount}% (campanie limitata)
  PLATESTI AZI:  [XXX lei cu {discount}% reducere]

  + Garantie 14 zile: daca nu esti multumita,
    iti returnam 100% din bani. Fara intrebari.

  Aceasta reducere expira la {deadline_date}.
  Nu se prelungeste. Nu se repeta pana la urmatoarea
  sesiune a cursului (data necunoscuta).

──────────────────────────────────────────────────────────────

  👉  [ VREAU {discount}% REDUCERE – MA INSCRIU ACUM ]
       Link: https://cursai.ro/inscriere

──────────────────────────────────────────────────────────────

{name}, ai toate informatiile.
Stii ce primesti, stii cat valoreza, stii care e termenul.

Decizia iti apartine.

Cu respect si incredere in potentialul tau,
Andreea Ionescu
Fondatoare Curs AI
📞 0720 XXX XXX | hello@cursai.ro
🌐 www.cursai.ro

──────────────────────────────────────────────────────────────

P.S. {spots_left} locuri ramase la pretul redus.
     Cand se ocupa, se ocupa. Nu exista lista de asteptare
     la pretul redus — urmatoarea sesiune va fi la pret intreg.

P.P.S. Garantia de 14 zile este reala. Am onorat-o
       pentru fiecare cursanta care a cerut-o. Zero risc.
       [ MA INSCRIU ACUM – VREAU {discount}% REDUCERE ]

──────────────────────────────────────────────────────────────
Ai primit acest email pentru ca te-ai abonat la lista noastra.
[Dezabonare] | [Modifica preferinte] | cursai.ro
"""
    return {
        "category":   "Beneficiu + Urgenta",
        "subject":    subject,
        "preheader":  preheader,
        "body":       body,
    }


# ─────────────────────────────────────────────────────────
# EMAIL 4 – EMPOWERMENT + URGENTA
# ─────────────────────────────────────────────────────────

def render_empowerment_urgenta(name: str, deadline_hours: int, discount: int, spots_left: int) -> dict:
    """
    Psihologie: Femeia nu cumpara un curs — isi asuma un rol in viitor.
    Urgenta nu e o amenintare, ci o invitatie la o misiune cu termen.
    Ton: Inspirational, cald, cu demnitate. Ca o scrisoare de la o mentora.
    Structura: Viziune → Realitate actuala → Rolul ei → Invitatie → Deadline ca oportunitate → CTA → P.S.
    """
    deadline_label = f"{deadline_hours}h" if deadline_hours >= 1 else "cateva minute"
    deadline_date  = (datetime.now() + timedelta(hours=deadline_hours)).strftime("%d %B, ora %H:%M")

    subject   = f"Viitorul apartine femeilor care stiu AI. Incepe astazi – {deadline_label} ramase"
    preheader = "Nu e vorba despre tehnologie. E vorba despre puterea ta de a defini ce urmeaza."

    body = f"""\
De la: Andreea Ionescu – Curs AI <andreea@cursai.ro>
Catre: {name}
Subiect: {subject}
Pre-header: {preheader}

──────────────────────────────────────────────────────────────

Draga {name},

Iti scriu personal pentru ca vreau sa iti spun ceva
ce cred cu toata convingerea:

Viitorul nu va fi al celor mai inteligenti.
Va fi al celor mai adaptabili.

Si femeile — prin natura lor, prin felul in care
gandesc, prin empatie si creativitate —
sunt cele mai bine pozitionate sa conduca
aceasta tranzitie catre lumea cu AI.

Dar numai daca aleg sa o faca.

──────────────────────────────────────────────────────────────

Traiesc intr-o perioada in care:

  → 65% dintre joburile din urmatorii 10 ani inca nu exista
  → AI va transforma fiecare industrie, fiecare rol profesional
  → Diferenta dintre cei care conduc si cei care raman in urma
    va fi: stiu sau nu stiu sa lucreze cu AI?

{name}, nu iti cer sa devii programatoare.
Nu iti cer sa studiezi ani de zile.

Iti cer sa iti dai 30 de zile sa inveti
un instrument care iti va schimba cariera
si felul in care te raportezi la munca ta.

──────────────────────────────────────────────────────────────

  Am construit cursul „De la Zero la Expert in AI"
  cu un singur gand in minte:

  Sa existe un loc in care femeile ca tine —
  curioase, ambitionase, ocupate, fara background tehnic —
  sa poata invata AI fara sa se simta covisite,
  fara jargon incomprehensibil,
  fara sa li se ceara sa stie matematica sau programare.

  Doar ele, instrumentele AI si rezultate reale
  de la prima saptamana.

──────────────────────────────────────────────────────────────

  CE INSEAMNA SA FAC PARTE DIN ACEASTA MISIUNE:
  ───────────────────────────────────────────────

  🌟  Inveti AI in 30 de zile, pas cu pas
  🌟  Aplici imediat in munca ta — de la ziua 1
  🌟  Faci parte dintr-o comunitate de femei
       care aleg sa conduca, nu sa fie conduse
  🌟  Primesti un certificat care atesta competenta ta
  🌟  Ai acces pe viata la materiale si actualizari

  Si faci toate acestea cu {discount}% reducere fata de
  pretul standard — dar numai pana la {deadline_date}.

──────────────────────────────────────────────────────────────

  {name}, femeile care se alatura astazi nu vor fi
  simpli participanti la un curs.

  Vor fi pionierele generatiei lor.
  Cele despre care colegele lor vor spune, peste 2 ani:
  „Ea a stiut devreme. Ea a facut pasul."

  Vrei sa fii una dintre ele?

──────────────────────────────────────────────────────────────

  👉  [ DA – VREAU SA FAC PARTE DIN VIITOR ]
       Link: https://cursai.ro/inscriere

──────────────────────────────────────────────────────────────

Oferta de {discount}% reducere expira la {deadline_date}.
Nu pentru ca asta e o tactica. Ci pentru ca fiecare
sesiune a cursului are un numar limitat de locuri —
si din {spots_left} locuri ramase, unele vor fi ocupate
inainte sa citesti aceste randuri.

Viitorul nu asteapta.
Dar eu te astept pe tine.

Cu drag si admiratie pentru curajul tau,
Andreea Ionescu
Fondatoare Curs AI
📞 0720 XXX XXX | andreea@cursai.ro
🌐 www.cursai.ro

──────────────────────────────────────────────────────────────

P.S. Stiu ca poate ai impresia ca „nu e momentul potrivit."
     Ca esti prea ocupata. Ca mai ai de rezolvat alte lucruri.

     Dar {name}, momentul potrivit nu vine.
     El se creeaza. Si tu il creezi acum,
     alegand sa investesti in tine.

     {deadline_label} ramase. [ INCEP ASTAZI ]

P.P.S. Garantie completa 14 zile. Daca dupa primele
       2 saptamani simti ca nu e pentru tine, iti returnam
       100% din bani. Fara conditii. Fara intrebari.
       Investitia ta este protejata.

──────────────────────────────────────────────────────────────
Ai primit acest email pentru ca te-ai abonat la lista noastra.
[Dezabonare] | [Modifica preferinte] | cursai.ro
"""
    return {
        "category":   "Empowerment + Urgenta",
        "subject":    subject,
        "preheader":  preheader,
        "body":       body,
    }


# ─────────────────────────────────────────────────────────
# GENERATOR & AFISARE
# ─────────────────────────────────────────────────────────

def generate_all_emails(name: str = "Maria", deadline_hours: int = 24,
                        discount: int = 40, spots_left: int = 7) -> list:
    """Genereaza toate cele 4 emailuri complete gata de trimis."""
    return [
        render_urgenta_pura(name, deadline_hours, discount, spots_left),
        render_curiozitate_urgenta(name, deadline_hours, discount, spots_left),
        render_beneficiu_urgenta(name, deadline_hours, discount, spots_left),
        render_empowerment_urgenta(name, deadline_hours, discount, spots_left),
    ]


def display_all_emails(emails: list):
    """Afiseaza toate emailurile in consola."""
    sep = "=" * 66
    for i, email in enumerate(emails, 1):
        print(f"\n{sep}")
        print(f"  EMAIL {i}/4 – {email['category'].upper()}")
        print(sep)
        print(email["body"])
    print(f"\n{sep}")
    print(f"  ✅  {len(emails)} emailuri complete generate si gata de trimis.")
    print(sep)


def save_emails_to_file(emails: list, filename: str = "emails_complete.txt"):
    """Salveaza toate emailurile intr-un singur fisier text."""
    sep = "=" * 66
    with open(filename, "w", encoding="utf-8") as f:
        f.write("EMAILURI COMPLETE GATA DE TRIMIS – CAMPANIE CURS AI\n")
        f.write(f"Generat la: {datetime.now().strftime('%d-%m-%Y %H:%M')}\n")
        f.write(sep + "\n")
        for i, email in enumerate(emails, 1):
            f.write(f"\n{sep}\n")
            f.write(f"  EMAIL {i}/4 – {email['category'].upper()}\n")
            f.write(f"{sep}\n")
            f.write(email["body"])
            f.write("\n")
        f.write(f"\n{sep}\n")
        f.write(f"Total: {len(emails)} emailuri complete generate.\n")
        f.write(sep + "\n")


# ─────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Parametri campaniei — modifica dupa nevoie
    emails = generate_all_emails(
        name           = "Maria",
        deadline_hours = 24,
        discount       = 40,
        spots_left     = 7,
    )

    display_all_emails(emails)
    save_emails_to_file(emails, "emails_complete.txt")
    print(f"\n📄 Emailurile au fost salvate in: emails_complete.txt")
