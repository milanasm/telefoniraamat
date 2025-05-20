import os
import smtplib, ssl
from email.message import EmailMessage

faili_nimi="kontaktid.txt"

def loe_failist():
    kontaktid=[]
    if os.path.exists(faili_nimi):
        with open(faili_nimi, "r") as f:
            for rida in f:
                osad=rida.strip().split(";")
                if len(osad)==3:
                    kontaktid.append({"nimi": osad[0], "telefon": osad[1], "email": osad[2]})
    return kontaktid

def kirjuta_faili(kontaktid):
    with open(faili_nimi, "w") as f:
        for kontakt in kontaktid:
            rida=f"{kontakt['nimi']};{kontakt['telefon']};{kontakt['email']}\n"
            f.write(rida)

def lisa_kontakt(kontaktid):
    nimi=input("Sisesta nimi: ")
    telefon=input("Sisesta telefon: ")
    email=input("Sisesta e-post: ")
    kontaktid.append({"nimi": nimi, "telefon": telefon, "email": email})
    kirjuta_faili(kontaktid)
    print("Kontakt lisatud.")

def kuva_kontaktid(kontaktid):
    for kontakt in kontaktid:
        print(kontakt)

def otsi_kontakti(kontaktid):
    nimi=input("Sisesta nimi otsimiseks: ")
    for kontakt in kontaktid:
        if kontakt["nimi"].lower()==nimi.lower():
            print(kontakt)
            return
    print("Kontakti ei leitud.")

def kustuta_kontakt(kontaktid):
    nimi=input("Sisesta kustutatava kontakti nimi: ")
    for kontakt in kontaktid:
        if kontakt["nimi"].lower()==nimi.lower():
            kontaktid.remove(kontakt)
            kirjuta_faili(kontaktid)
            print("Kontakt kustutatud.")
            return
    print("Kontakti ei leitud.")

def muuda_kontakti(kontaktid):
    nimi=input("Sisesta muudetava kontakti nimi: ")
    for kontakt in kontaktid:
        if kontakt["nimi"].lower()==nimi.lower():
            kontakt["nimi"]=input("Uus nimi: ")
            kontakt["telefon"]=input("Uus telefon: ")
            kontakt["email"]=input("Uus e-post: ")
            kirjuta_faili(kontaktid)
            print("Kontakt muudetud.")
            return
    print("Kontakti ei leitud.")

def sorteeri_kontaktid(kontaktid):
    valik=input("Sorteeri (nimi/telefon/email): ").lower()
    if valik in ["nimi", "telefon", "email"]:
        kontaktid.sort(key=lambda x: x[valik].lower())
        kirjuta_faili(kontaktid)
        print("Kontaktid sorditud.")
    else:
        print("Vale valik.")

def saada_kiri():
    kellele=input("Sisesta saaja e-post: ")
    kiri=input("Sisesta sõnum: ")
    smtp_server="smtp.gmail.com"
    smtp_port=587
    kellelt=input("Sisesta oma Gmaili aadress: ")
    parool=input("Sisesta oma parool: ")
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg["Subject"]="Telefoniraamat"
    msg["From"]=kellelt
    msg["To"]=kellele

    try:
        server=smtplib.SMTP(smtp_server, smtp_port)
        server.starttls(context=context)
        server.login(kellelt, parool)
        server.send_message(msg)
        print("Kiri saadetud!")
    except Exception as e:
        print("Viga:", e)
    finally:
        server.quit()



        #xdas gqun gyez jzwv (oma parool)




# import os
# import smtplib, ssl
# from email.message import EmailMessage
# from twilio.rest import Client

# faili_nimi = "kontaktid.txt"

# def loe_failist():
#     kontaktid = []
#     if os.path.exists(faili_nimi):
#         with open(faili_nimi, "r") as f:
#             for rida in f:
#                 osad = rida.strip().split(";")
#                 if len(osad) == 3:
#                     kontaktid.append({"nimi": osad[0], "telefon": osad[1], "email": osad[2]})
#     return kontaktid

# def kirjuta_faili(kontaktid):
#     with open(faili_nimi, "w") as f:
#         for kontakt in kontaktid:
#             rida = f"{kontakt['nimi']};{kontakt['telefon']};{kontakt['email']}\n"
#             f.write(rida)

# def lisa_kontakt(kontaktid):
#     nimi = input("Sisesta nimi: ")
#     telefon = input("Sisesta telefon: ")
#     email = input("Sisesta e-post: ")
#     kontaktid.append({"nimi": nimi, "telefon": telefon, "email": email})
#     kirjuta_faili(kontaktid)
#     print("Kontakt lisatud.")

# def kuva_kontaktid(kontaktid):
#     for kontakt in kontaktid:
#         print(kontakt)

# def otsi_kontakti(kontaktid):
#     nimi = input("Sisesta nimi otsimiseks: ")
#     for kontakt in kontaktid:
#         if kontakt["nimi"].lower() == nimi.lower():
#             print(kontakt)
#             return
#     print("Kontakti ei leitud.")

# def kustuta_kontakt(kontaktid):
#     nimi = input("Sisesta kustutatava kontakti nimi: ")
#     for kontakt in kontaktid:
#         if kontakt["nimi"].lower() == nimi.lower():
#             kontaktid.remove(kontakt)
#             kirjuta_faili(kontaktid)
#             print("Kontakt kustutatud.")
#             return
#     print("Kontakti ei leitud.")

# def muuda_kontakti(kontaktid):
#     nimi = input("Sisesta muudetava kontakti nimi: ")
#     for kontakt in kontaktid:
#         if kontakt["nimi"].lower() == nimi.lower():
#             kontakt["nimi"] = input("Uus nimi: ")
#             kontakt["telefon"] = input("Uus telefon: ")
#             kontakt["email"] = input("Uus e-post: ")
#             kirjuta_faili(kontaktid)
#             print("Kontakt muudetud.")
#             return
#     print("Kontakti ei leitud.")

# def sorteeri_kontaktid(kontaktid):
#     valik = input("Sorteeri (nimi/telefon/email): ").lower()
#     if valik in ["nimi", "telefon", "email"]:
#         kontaktid.sort(key=lambda x: x[valik].lower())
