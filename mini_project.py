import json

def adaugare_angajat(employees):
    
    while True:
        cnp = input("CNP: ")
        if not (cnp.isdigit() and len(cnp) == 13):
            print("CNP invalid. Trebuie să conțină exact 13 cifre.")
        elif any(emp["cnp"] == cnp for emp in employees):
            print("Există deja un angajat cu acest CNP.")
        else:
            break

    nume = input("Nume: ")
    prenume = input("Prenume: ")
    while True:
        try:
            varsta = int(input("Varsta: "))
            if varsta < 18:
                print("Vârsta trebuie să fie mai mare decât 18 ani.")
            else:
                break
        except ValueError:
            print("Introduceți un număr valid pentru vârstă.")

    while True:
        try:
            salariu = int(input("Salariu: "))
            if salariu < 4050:
                salariu = int(input("Salariu: "))
            else:
                break
        except ValueError:
             print("Introduceți un număr valid pentru salariu.")      
    
    departament = input("Departament: ").lower()
    senioritate = input("Senioritate: ").lower()

    while senioritate not in ["junior", "mid", "senior"]:
        senioritate = input("Senioritate invalidă. Introdu din nou: ")
   
    angajat = {
        "cnp": cnp,
        "nume": nume,
        "prenume": prenume,
        "varsta": varsta,
        "salariu": salariu,
        "departament": departament,
        "senioritate": senioritate
    }
    employees.append(angajat)

def cautare_angajat(employees):
    while True:
        cnp_search = input("CNP: ")
        if not (cnp_search.isdigit() and len(cnp_search) == 13):
            print("CNP invalid. Trebuie să conțină exact 13 cifre.")
        else:
            break
    found = False
    for emp in employees:
        if emp["cnp"] == cnp_search:
            print(emp)
            found = True
            break
    if not found:
        print("Angajatul nu există")

def modificare_angajat(employees):
    while True:
        cnp_change = input("CNP: ")
        if not (cnp_change.isdigit() and len(cnp_change) == 13):
            print("CNP invalid. Trebuie să conțină exact 13 cifre.")
        else:
            break
    emp_gasit = None
    for emp in employees:
        if emp["cnp"] == cnp_change:
            emp_gasit = emp
            break
    if emp_gasit:
        update = input("Ce doriți să modificați?").lower()
        if update == "nume":
            emp_gasit["nume"] = input("Nume nou: ")
        elif update == "prenume":
            emp_gasit["prenume"] = input("Prenume nou: ")
        elif update == "varsta":
            while True:
                try:
                    varsta_noua = int(input("Varsta noua: "))

                    if varsta_noua < 18:
                        print("Invalid, vârsta trebuie să fie mcel puțin 18 ani. Încearcă din nou.")
                    else:
                        emp_gasit["varsta"] = varsta_noua
                        break
                except ValueError:
                    print("Introduceți un număr vă rog.")
        elif update == "salariu":
            while True:
                try:
                    salariu_nou = int(input("Salariu nou: "))
                    if salariu_nou < 4050:
                        print("Invalid, salariul trebuie să fie cel puțin 4050. Încearcă din nou.")
                    else:
                        emp_gasit["salariu"] = salariu_nou
                        break
                except ValueError:
                    print("Introduceți un număr vă rog.")
        elif update == "departament":
            emp_gasit["departament"] = input("Noul departament: ").lower()
        elif update == "senioritate":
            senioritate_noua = input("Noua senioritate: ").lower()
            while senioritate_noua not in ["junior", "mid", "senior"]:
                senioritate_noua = input("Senioritate nerecunoscută. Încercați din nou.").lower()
            emp_gasit["senioritate"] = senioritate_noua
        else:
            print("Eroare")
    else:
        print("Angajatul nu există.")

def stergere_angajat(employees):
    while True:
        cnp_delete = input("CNP: ")
        if not (cnp_delete.isdigit() and len(cnp_delete) == 13):
            print("CNP invalid. Trebuie să conțină exact 13 cifre.")
        else:
            break
    found = False
    for i, emp in enumerate(employees):
        if emp["cnp"] == cnp_delete:
            del employees[i]
            found = True
            print("Angajat șters")
            break
    if not found:
        print("Angajatul nu a fost găsit")

def afisare_angajati(employees):
    for emp in employees:
        print(emp)

def cost_salariu_total(employees):
    total = sum(emp["salariu"] for emp in employees)
    print("Costul total pentru salariu este:", total)            

def cost_salariu_dep(employees):
    departament = input("Specificați departamentul: ").lower()
    cost = 0
    found = False
    for emp in employees:
        if emp["departament"] == departament:
            found = True
            cost += emp["salariu"]
    if not found:
        print("Departament inexistent")
    else:
        print(f"Costul salariilor pe departamentul {departament} este {cost}")

    
def calcul_fluturas(employees):
    while True:
        cnp_fluturas = input("CNP: ")
        if not (cnp_fluturas.isdigit() and len(cnp_fluturas) == 13):
            print("CNP invalid. Trebuie să conțină exact 13 cifre.")
        else:
            break

    for emp in employees:
        if emp["cnp"] == cnp_fluturas:
            salariu = emp["salariu"]

            cas = salariu * 0.10
            cass = salariu * 0.25
            ramas = salariu - cas - cass
            impozit = ramas * 0.10
            net = ramas - impozit

            print(f"Fluturaș salariu pentru {emp['nume']} {emp['prenume']}:")
            print(f"Brut: {salariu}")
            print(f"CAS: {cas}")
            print(f"CASS: {cass}")
            print(f"Impozit: {impozit}")
            print(f"Net: {net}")

            return

    print("Angajatul nu există")

def dupa_senioritate(employees):
    senioritate = input("Introduceți senioritatea: ").lower()
    match = False
    while senioritate not in ["mid", "junior", "senior"]:
        senioritate = input("Invalid. Încercați din nou: : ").lower()
    for emp in employees:
        if emp["senioritate"] == senioritate:
            print(emp)
            match = True
    if not match:
        print("Nu există angajați pentru această senioritate")

def dupa_departament(employees):
    departament = input("Introduceți departament:").lower()
    match = False
    for emp in employees:
        if emp["departament"] == departament:
            print(emp)
            match = True
    if not match:
       print("Nu există angajați pentru aceast departament")

def load_employees():
    try:
        with open("employees.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_employees(employees):
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=4) 


def main():
    employees = load_employees()
    while True:  
        print("\n WELCOME \n")
        print("Alegeți o opțiune:")
        print("1. Adăugare angajat")
        print("2. Căutare angajat")
        print("3. Modificarea datelor unui angajat")
        print("4. Ștergere angajat")
        print("5. Afișarea tuturor angajaților")
        print("6. Calcul cost total salarii companie")
        print("7. Calcul cost total salarii departament")
        print("8. Calcul fluturaș salariu angajat")
        print("9. Afișarea angajaților unei senioritate")
        print("10. Afișarea angajaților unui departament")
        print("11.Ieșire")
        try:
            optiune = int(input("Opțiune: "))
        except ValueError:
            print("Introduceți un număr valid!")
            continue
        if optiune == 1:
            adaugare_angajat(employees)
            save_employees(employees)
        elif optiune == 2:
            cautare_angajat(employees)
        elif optiune == 3:
            modificare_angajat(employees)
            save_employees(employees)
        elif optiune == 4:
            stergere_angajat(employees)
            save_employees(employees)
        elif optiune == 5:
            afisare_angajati(employees)
        elif optiune == 6:
            cost_salariu_total(employees)
        elif optiune == 7:
            cost_salariu_dep(employees)
        elif optiune == 8:
            calcul_fluturas(employees)
        elif optiune == 9:
            dupa_senioritate(employees)
        elif optiune == 10:
            dupa_departament(employees)
        elif optiune == 11:
            print("GOODBYE")
            break
        else:
            print("Opțiune invalidă, încercați din nou.")

main()