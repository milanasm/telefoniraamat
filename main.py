import funktsioonid as f

def main():
    kontaktid = f.loe_failist()

    while True:
        print("""
1. Lisa kontakt
2. Kuva kõik kontaktid
3. Otsi kontakti
4. Kustuta kontakt
5. Muuda kontakti
6. Sorteeri kontaktid
7. Saada e-kiri
8. Saada masskiri
9. Välju
        """)
        valik = input("Vali tegevus: ")

        if valik=="1":
            f.lisa_kontakt(kontaktid)
        elif valik=="2":
            f.kuva_kontaktid(kontaktid)
        elif valik=="3":
            f.otsi_kontakti(kontaktid)
        elif valik=="4":
            f.kustuta_kontakt(kontaktid)
        elif valik=="5":
            f.muuda_kontakti(kontaktid)
        elif valik=="6":
            f.sorteeri_kontaktid(kontaktid)
        elif valik=="7":
            f.saada_kiri()
        elif valik=="8":
            f.saada_masskiri(kontaktid)
        elif valik=="9":
            print("Head aega!")
            break
        else:
            print("Vale valik, proovi uuesti.")

if __name__=="__main__":
    main()


# import funktsioonid as f

# def main():
#     kontaktid = f.loe_failist()

#     while True:
#         print("""
# 1. Lisa kontakt
# 2. Kuva kõik kontaktid
# 3. Otsi kontakti
# 4. Kustuta kontakt
# 5. Muuda kontakti
# 6. Sorteeri kontaktid
# 7. Saada e-kiri
# 8. Spämmida numbri järgi
# 9. Välju
#         """)
#         valik = input("Vali tegevus: ")

#         if valik == "1":
#             f.lisa_kontakt(kontaktid)
#         elif valik == "2":
#             f.kuva_kontaktid(kontaktid)
#         elif valik == "3":
#             f.otsi_kontakti(kontaktid)
#         elif valik == "4":
#             f.kustuta_kontakt(kontaktid)
#         elif valik == "5":
#             f.muuda_kontakti(kontaktid)
#         elif valik == "6":
#             f.sorteeri_kontaktid(kontaktid)
#         elif valik == "7":
#             f.saada_kiri()
#         elif valik == "8":
#             f.spamma_numbrile()
#         elif valik == "9":
#             print("Head aega!")
#             break
#         else:
#             print("Vale valik, proovi uuesti.")

# if __name__ == "__main__":
#     main()

