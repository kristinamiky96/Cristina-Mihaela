"""
Generator de Subiecte de Email Personalizate
Campanie: Curs Inteligenta Artificiala - De la Zero la Expert
Grup tinta: Femei 25-45 ani, incepátoare cu AI
Element de personalizare: Urgenta / Limita de timp
"""

from datetime import datetime, timedelta


def generate_subjects(name: str, deadline_hours: int, discount: int, spots_left: int) -> dict:
    """
    Genereaza subiecte de email personalizate cu elemente de urgenta.

    Args:
        name: Prenumele destinatarei
        deadline_hours: Ore ramase pana la expirarea ofertei
        discount: Procentul de reducere (ex: 40 pentru 40%)
        spots_left: Numarul de locuri disponibile

    Returns:
        dict cu subiecte grupate pe categorii
    """
    deadline_label = f"{deadline_hours}h" if deadline_hours >= 1 else "cateva minute"
    deadline_date = (datetime.now() + timedelta(hours=deadline_hours)).strftime("%d %b, ora %H:%M")

    subjects = {
        "Urgenta_Pura": [
            f"{name}, mai ai doar {deadline_label} sa te inscrii la cursul AI!",
            f"Ultimele {spots_left} locuri disponibile – Curs AI De la Zero la Expert",
            f"Oferta expira in {deadline_label} – {discount}% reducere la cursul tau de AI",
            f"ATENTIE: Inscrierea se inchide la {deadline_date}. Locul tau, {name}!",
            f"Countdown: {deadline_label} ramase pentru {discount}% OFF la cursul AI",
        ],
        "Curiozitate_plus_Urgenta": [
            f"{name}, stii deja sa folosesti AI? Afla in 30 zile – oferta valabila {deadline_label}",
            f"Femeile care stiu AI castiga mai mult. Tu poti fi una dintre ele – {deadline_label} mai ai",
            f"Ce ar schimba AI-ul in viata ta? Descopera in 30 zile – oferta expira curand",
            f"{name}, cat de greu e sa inveti AI de la zero? Raspunsul te surprinde – vezi acum",
            f"De ce 1 din 3 femei regreta ca nu a invatat AI mai devreme? Oferta: {deadline_label}",
        ],
        "Beneficiu_plus_Urgenta": [
            f"De la 0 la expert in AI in 30 zile – {discount}% reducere, expira azi",
            f"{name}, locul tau la cursul AI te asteapta – doar pana la {deadline_date}",
            f"Invata AI in 30 zile, fara experienta anterioara – {discount}% OFF, {deadline_label} ramase",
            f"Transforma-ti cariera cu AI: 30 zile, rezultate reale – oferta expira in {deadline_label}",
            f"{name}, {discount}% reducere la cursul AI care iti schimba cariera – expira la {deadline_date}",
        ],
        "Empowerment_plus_Urgenta": [
            f"Viitorul apartine femeilor care stiu AI. Incepe astazi – {deadline_label} ramase",
            f"{name}, nu lasa tehnologia sa te depaseasca – inscrie-te acum, {discount}% OFF",
            f"AI nu e pentru 'altii' – e si pentru tine, {name}. Ultima sansa: {deadline_label}",
            f"30 zile. De la zero. Expert in AI. Oferta speciala expira in {deadline_label}",
        ],
    }

    return subjects


def display_subjects(subjects: dict, name: str, deadline_hours: int, discount: int, spots_left: int):
    """Afiseaza subiectele generate intr-un format lizibil."""
    print("=" * 65)
    print("  GENERATOR SUBIECTE EMAIL PERSONALIZATE")
    print("  Curs: Inteligenta Artificiala - De la Zero la Expert")
    print("  Grup tinta: Femei 25-45 ani, incepátoare cu AI")
    print("=" * 65)
    print(f"\nParametri de personalizare:")
    print(f"  Prenume:          {name}")
    print(f"  Ore ramase:       {deadline_hours}h")
    print(f"  Reducere:         {discount}%")
    print(f"  Locuri ramase:    {spots_left}")
    print()

    total = 0
    for category, subject_list in subjects.items():
        category_label = category.replace("_", " ")
        print(f"--- {category_label} ---")
        for subject in subject_list:
            total += 1
            print(f"  {total:2}. {subject}")
        print()
    print(f"Total subiecte generate: {total}")
    print("=" * 65)


def save_to_file(subjects: dict, filename: str, name: str, deadline_hours: int, discount: int, spots_left: int):
    """Salveaza subiectele intr-un fisier text."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("SUBIECTE DE EMAIL PERSONALIZATE – CURS AI\n")
        f.write("=" * 65 + "\n")
        f.write(f"Campanie: Curs Inteligenta Artificiala – De la Zero la Expert\n")
        f.write(f"Grup tinta: Femei 25-45 ani, incepátoare cu AI\n")
        f.write(f"Generat la: {datetime.now().strftime('%d-%m-%Y %H:%M')}\n")
        f.write("=" * 65 + "\n\n")
        f.write(f"Parametri: Prenume={name}, Urgenta={deadline_hours}h, Reducere={discount}%, Locuri={spots_left}\n\n")

        total = 0
        for category, subject_list in subjects.items():
            category_label = category.replace("_", " ")
            f.write(f"\n[{category_label}]\n")
            for subject in subject_list:
                total += 1
                f.write(f"  {total:2}. {subject}\n")

        f.write(f"\nTotal: {total} subiecte generate\n")


def main():
    # Parametri demo pentru campanie
    name = "Maria"
    deadline_hours = 24
    discount = 40
    spots_left = 7

    subjects = generate_subjects(name, deadline_hours, discount, spots_left)
    display_subjects(subjects, name, deadline_hours, discount, spots_left)
    save_to_file(subjects, "subjects_output.txt", name, deadline_hours, discount, spots_left)
    print(f"\nSubiectele au fost salvate si in: subjects_output.txt")


if __name__ == "__main__":
    main()
