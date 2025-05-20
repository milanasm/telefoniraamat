import os
import smtplib, ssl
from email.message import EmailMessage
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont

faili_nimi="kontaktid.txt"
teema="valgus"

def vaheta_teemat():
    global teema
    if teema=="valgus":
        aken.configure(bg="#2E2E2E")
        for widget in aken.winfo_children():
            if isinstance(widget, (Label, Button)):
                widget.configure(bg="#3E3E3E", fg="white")
            elif isinstance(widget, Entry):
                widget.configure(bg="#5A5A5A", fg="white", insertbackground="white")
            elif isinstance(widget, Listbox):
                widget.configure(bg="#5A5A5A", fg="white")
            elif isinstance(widget, Text):
                widget.configure(bg="#5A5A5A", fg="white", insertbackground="white")
        teema="tume"
    else:
        aken.configure(bg="#FFDDE7")
        for widget in aken.winfo_children():
            if isinstance(widget, (Label, Button)):
                widget.configure(bg="#FFDDE7", fg="black")
            elif isinstance(widget, Entry):
                widget.configure(bg="white", fg="black", insertbackground="black")
            elif isinstance(widget, Listbox):
                widget.configure(bg="white", fg="black")
            elif isinstance(widget, Text):
                widget.configure(bg="white", fg="black", insertbackground="black")
        teema="valgus"

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

def uuenda_loendit():
    kontaktid=loe_failist()
    listbox.delete(0, END)
    for kontakt in kontaktid:
        listbox.insert(END, f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}")

def kontrolli_andmed(nimi, telefon, email):
    if nimi == "" or telefon == "" or email == "":
        messagebox.showwarning("Viga", "Kõik väljad peavad olema täidetud!")
        return False
    if telefon.isdigit() == False:
        messagebox.showwarning("Viga", "Telefoninumber peab sisaldama ainult numbreid!")
        return False
    if email.count("@") != 1 or "." in email.split("@")[-1] == False:
        messagebox.showwarning("Viga", "E-posti aadress peab sisaldama ühte '@' ja domeenis punkti ('.')!")
        return False
    return True

def lisa_kontakt():
    nimi=entry_nimi.get()
    telefon=entry_telefon.get()
    email=entry_email.get()

    if kontrolli_andmed(nimi, telefon, email) == False:
        return

    kontaktid=loe_failist()
    kontaktid.append({"nimi": nimi, "telefon": telefon, "email": email})
    kirjuta_faili(kontaktid)
    uuenda_loendit()
    messagebox.showinfo("Teade", "Kontakt lisatud!")

def muuda_kontakt():
    kontaktid=loe_failist()
    nimi=entry_nimi.get()
    telefon=entry_telefon.get()
    email=entry_email.get()

    if kontrolli_andmed(nimi, telefon, email)==False:
        return

    leitud=False
    for kontakt in kontaktid:
        if kontakt["nimi"].lower()==nimi.lower():
            kontakt["telefon"]=telefon
            kontakt["email"]=email
            leitud=True
            break
    if leitud:
        kirjuta_faili(kontaktid)
        uuenda_loendit()
        messagebox.showinfo("Teade", "Kontakt muudetud!")
    else:
        messagebox.showwarning("Hoiatus", "Kontakti ei leitud!")

def kustuta_kontakt():
    kontaktid=loe_failist()
    nimi=entry_nimi.get().strip()
    telefon=entry_telefon.get().strip()
    email=entry_email.get().strip()

    if nimi == "" and telefon == "" and email == "":
        messagebox.showwarning("Hoiatus", "Palun sisesta vähemalt üks väli (nimi, telefon või email)!")
        return

    uuendatud_kontaktid=[]
    kontakt_leitud=False

    for kontakt in kontaktid:
        nimi_sobib=(nimi != "" and kontakt["nimi"].lower() == nimi.lower())
        telefon_sobib=(telefon != "" and kontakt["telefon"] == telefon)
        email_sobib=(email != "" and kontakt["email"].lower() == email.lower())

        if nimi_sobib or telefon_sobib or email_sobib:
            kontakt_leitud=True
        else:
            uuendatud_kontaktid.append(kontakt)

    if kontakt_leitud:
        kirjuta_faili(uuendatud_kontaktid)
        uuenda_loendit()
        messagebox.showinfo("Teade", "Kontakt kustutatud!")
    else:
        messagebox.showwarning("Hoiatus", "Kontakti ei leitud!")

def otsi_kontakt():
    kontaktid=loe_failist()
    nimi=entry_nimi.get().lower()
    telefon=entry_telefon.get().lower()
    email=entry_email.get().lower()

    leitud=False

    for kontakt in kontaktid:
        kontakt_nimi=kontakt["nimi"].lower()
        kontakt_telefon=kontakt["telefon"].lower()
        kontakt_email=kontakt["email"].lower()
        if ((nimi and kontakt_nimi == nimi)
            or (telefon and kontakt_telefon == telefon)
            or (email and kontakt_email == email)):

            entry_nimi.delete(0,END)
            entry_telefon.delete(0,END)
            entry_email.delete(0,END)

            entry_nimi.insert(0,kontakt["nimi"])
            entry_telefon.insert(0,kontakt["telefon"])
            entry_email.insert(0,kontakt["email"])

            leitud=True
            break
    if leitud==True:
        pass
    else:
        messagebox.showwarning("Hoiatus", "Kontakti ei leitud!")

def naita_koguarv():
    kontaktid=loe_failist()
    messagebox.showinfo("Koguarv", f"Kokku on {len(kontaktid)} kontakti.")

def sorteeri_nimi_jargi():
    kontaktid=loe_failist()
    kontaktid.sort(key=lambda x: x["nimi"].lower())
    kirjuta_faili(kontaktid)
    uuenda_loendit()
    messagebox.showinfo("Teade", "Kontaktid sorteeritud nime järgi.")

def saada_kiri():
    kellele=entry_email.get()
    kiri=text_sonum.get("1.0", END).strip()
    kellelt=entry_kellelt.get()
    parool=entry_parool.get()

    smtp_server="smtp.gmail.com"
    smtp_port=587
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
        messagebox.showinfo("Teade", "Kiri saadetud!")
    except Exception as e:
        messagebox.showerror("Viga", f"Kiri saatmata: {e}")
    finally:
        if "server" in locals():
                server.quit()

def saada_mass_kiri():
    kontaktid=loe_failist()
    kiri=text_sonum.get("1.0", END).strip()
    kellelt=entry_kellelt.get()
    parool=entry_parool.get()

    if len(kontaktid)==0:
        messagebox.showwarning("Hoiatus", "Kontakte pole.")
        return

    if kiri != "" and kellelt != "" and parool != "":
        smtp_server="smtp.gmail.com"
        smtp_port=587
        context=ssl.create_default_context()

        try:
            server=smtplib.SMTP(smtp_server, smtp_port)
            server.starttls(context=context)
            server.login(kellelt, parool)

            for kontakt in kontaktid:
                msg=EmailMessage()
                msg.set_content(kiri)
                msg["Subject"]="Telefoniraamat"
                msg["From"]=kellelt
                msg["To"]=kontakt["email"]
                server.send_message(msg)
            messagebox.showinfo("Teade", "Masskiri saadetud!")

        except Exception as e:
            messagebox.showerror("Viga", f"Kiri saatmata: {e}")
        finally:
            if "server" in locals():
                server.quit()
    else:
        messagebox.showwarning("Hoiatus", "Täida kõik e-kirja väljad.")
        return

#GUI
aken=Tk()
aken.title("Telefoniraamat")
aken.geometry("800x380")
aken.configure(bg="#FFDDE7")

#shrifty
font_label=tkFont.Font(family="Arial", size=10)
font_entry=tkFont.Font(family="Arial", size=10)
font_button=tkFont.Font(family="Arial", size=11, weight="bold")
font_title=tkFont.Font(family="Arial", size=12, weight="bold")
font_list=tkFont.Font(family="Arial", size=10)
font_text=tkFont.Font(family="Arial", size=10)

#graf metki knigi
Label(aken, text="Nimi:", font=font_label, bg="#FFDDE7").place(x=20, y=20)
entry_nimi=Entry(aken, width=30, font=font_entry)
entry_nimi.place(x=100, y=20)

Label(aken, text="Telefon:", font=font_label, bg="#FFDDE7").place(x=20, y=60)
entry_telefon=Entry(aken, width=30, font=font_entry)
entry_telefon.place(x=100, y=60)

Label(aken, text="E-post:", font=font_label, bg="#FFDDE7").place(x=20, y=100)
entry_email=Entry(aken, width=30, font=font_entry)
entry_email.place(x=100, y=100)

#knopki
Button(aken, text="Lisa\nkontakt", command=lisa_kontakt, font=font_button,
       bg="#FDA3BE", fg="white", width=7, height=2).place(x=20, y=140)
Button(aken, text="Otsi\nkontakt", command=otsi_kontakt, font=font_button,
       bg="#FDA3BE", fg="white", width=7, height=2).place(x=20, y=195)
Button(aken, text="Kustuta\nkontakt", command=kustuta_kontakt, font=font_button,
       bg="#FDA3BE", fg="white", width=7, height=2).place(x=20, y=250)
Button(aken, text="Muuda\nkontakt", command=muuda_kontakt, font=font_button,
       bg="#FDA3BE", fg="white", width=7, height=2).place(x=20, y=305)

#box kontaktov
listbox=Listbox(aken, height=12, width=50, font=font_list)
listbox.place(x=100, y=140)
uuenda_loendit()

#e-kiri
Label(aken, text="Sinu Gmail:", font=font_label, bg="#FFDDE7").place(x=480, y=140)
entry_kellelt=Entry(aken, width=30, font=font_entry)
entry_kellelt.place(x=570, y=140)

Label(aken, text="Parool:", font=font_label, bg="#FFDDE7").place(x=480, y=175)
entry_parool=Entry(aken, show="*", width=30, font=font_entry)
entry_parool.place(x=570, y=175)

Label(aken, text="Sõnum:", font=font_label, bg="#FFDDE7").place(x=480, y=215)
text_sonum=Text(aken, width=30, height=3, font=font_text)
text_sonum.place(x=570, y=215)

Button(aken, text="Saada e-kiri", command=saada_kiri, font=font_button,
       bg="#FDA3BE", fg="white").place(x=570, y=275)
Button(aken, text="Masskiri", command=saada_mass_kiri, font=font_button,
       bg="#FDA3BE", fg="white", width=10).place(x=680, y=275)

#dop funkts
Button(aken, text="Vaheta\nteemat", command=vaheta_teemat, font=font_button,
       bg="#FDA3BE", fg="white", width=10).place(x=680, y=20)

Button(aken, text="Kokku\nkontakte", command=naita_koguarv, font=font_button,
       bg="#FDA3BE", fg="white", width=10, height=2).place(x=430, y=20)

Button(aken, text="Sorteeri\nnime järgi", command=sorteeri_nimi_jargi, font=font_button,
       bg="#FDA3BE", fg="white", width=12, height=2).place(x=550, y=20)

aken.mainloop()






