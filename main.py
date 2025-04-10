import json


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers, products, customers):
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    # Omogućite unos kupca
    # Izračunajte sub_total, tax i total
    # Dodajte novu ponudu u listu offers
    print("Dostupni kupci su:")

    for i in range(len(customers)):
        print(i+1, customers[i]['name'])

    broj_kupca = int(input("Unesite broj koji se nalazi ispred zeljenog kupca:")) -1
    kupac = customers[broj_kupca]

    date = input("Unesite datum (GODINA-DAN-MJESEC): ")
    
    print("Dostupni proizvodi:")

    for i in range(len(products)):
        print(f"{i + 1}. {products[i]['name']} ima cijenu: {products[i]['price']}")
    
    proizvodi_za_kupit = []

    while True:
        if input("Jeste li unjeli sve proizvode (Odgovorite s da ili ne)?").lower() =='da':
            break
        dodatni_proizvod_id = int(input("Unesite broj ispred proizvoda kojeg zelite: "))
        kolicina = int(input("Unesite koliko tih proizvoda zelite: "))
        proizvod_total = kolicina * products[dodatni_proizvod_id - 1]["price"]

        proizvod = {
            "product_id": dodatni_proizvod_id,
            "product_name": products[dodatni_proizvod_id - 1]["name"],
            "description": products[dodatni_proizvod_id - 1]["description"],
            "price": products[dodatni_proizvod_id - 1]["price"],
            "quantity": kolicina,
            "item_total": proizvod_total
        }
        proizvodi_za_kupit.append(proizvod)
        
        sub_total = sum(proizvod["item_total"] for proizvod in proizvodi_za_kupit)

        tax = sub_total * 0.1
        total = sub_total + tax
        broj_ponude = max(ponuda["offer_number"] for ponuda in offers) + 1

        nova_ponuda ={
            "offer_number": broj_ponude,
            "customer": kupac,
            "date": date,
            "items": proizvodi_za_kupit,
            "sub_total": sub_total,
            "tax": tax,
            "total": total
        }
        offers.append(nova_ponuda)

    print("Nova ponuda uspjesno dodana")
    

# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products):
    """
    Allows the user to add a new product or modify an existing product.
    """
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
    
    opcija = int(input("Ako zelite dodati novi proizvod upisite 1,\n ako zelite izmijenit neki proizvod upisite 2"))
    if opcija == 1:

        broj_proizvoda = max(proizvod["id"] for proizvod in products) + 1

        ime_proizvoda = input("Unesite ime novog proizvoda ")
        opis_proizvoda = input("Unesite opis novog proizvoda ")
        cijena_proizvoda = int(input("Unesite kolika je cijena tog proizvoda: "))

        novi_proizvod = {
            "id": broj_proizvoda,
            "name": ime_proizvoda,
            "description": opis_proizvoda,
            "price": cijena_proizvoda
        }
        products.append(novi_proizvod)
        print("Novi proizvod uspjesno dodan")
    
    elif opcija == 2:
        
        print("Dostupni proizvodi:")

        for i in range(len(products)):
            print(f"{i + 1}. {products[i]['name']} ima cijenu: {products[i]['price']}")
        
        id_proizvoda_za_izmjenu =int(input("Unesite broj ispred proizvoda kojeg zelite izmijenit: "))

        if input("Zelite li promijeniti ime (Odgovorite s da ili ne)?").lower() =='da':
            novo_ime = input("Unesite novo ime proizvoda")
            products[id_proizvoda_za_izmjenu - 1]["name"] = novo_ime
        if input("Zelite li promijeniti opis (Odgovorite s da ili ne)?").lower() =='da':
            novi_opis = input("Unesite novi opis proizvoda")
            products[id_proizvoda_za_izmjenu - 1]["description"] = novi_opis
        if input("Zelite li promijeniti cijenu (Odgovorite s da ili ne)?").lower() =='da':
            nova_cijena = int(input("Unesite novu cijenu proizvoda"))
            products[id_proizvoda_za_izmjenu - 1]["price"] = nova_cijena
        print("Podaci izmijenjeni")
    else:
        print("To nije ni 1 ni 2")
    



# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers):
    """
    Allows the user to add a new customer or view all customers.
    """
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    # Za pregled: prikaži listu svih kupaca
    opcija = int(input("Ako zelite pregledati sve kupce upisite 1,\n ako zelite dodati novog kupca upisite 2"))
    if opcija == 1:
        for kupac in customers:
            print(f"Ime kupca: {kupac['name']} email: {kupac['email']} vat_id: {kupac['vat_id']}")

    elif opcija == 2:

        ime_kupca = input("Unesite ime novog kupca ")
        email_kupca = ""
        while '@' not in email_kupca:
            email_kupca = input("Unesite email novog kupca ")
        vat_id_kupca = int(input("Unesite vat_id tog kupca: "))

        novi_kupac = {
            "name": ime_kupca,
            "email": email_kupca,
            "vat_id": vat_id_kupca
        }
        customers.append(novi_kupac)
        print("Novi kupac uspjesno dodan")




# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers):
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    opcija = int(input("Ako zelite pregledati sve ponude upisite 1," \
                "\n ako zelite pregledati ponude po mjesecu upisite 2\n"
                "ako zelize pojedinacnu upisite 3"))
    if opcija == 1:
        for ponuda in offers:
            print_offer(ponuda) #a ne radi ("TypeError")
    elif opcija == 2:
        mjesec = int(input("Unesite mjesec:"))
        found = False
        for ponuda in offers:
            parts = ponuda["date"].split("-")
            if len(parts) == 3 and parts[1] == str(mjesec).zfill(2): #zfill pretvara u string sa 2 znak 4->04
                print_offer(ponuda)
                found = True
        if not found:
            print("Nema jos nista za taj mjesec") #joj uvik mi ovo ispisuje
    elif opcija == 3:
        pojedinacan_id = int(input("Unesite broj ponude"))
        for ponuda in offers:
            if ponuda["offer_number"] == pojedinacan_id:
                print_offer(ponuda) #ma ni ova ne radi 
        


#ovo mie promaklo, vidjela sam tek sad kad sam krenila radit ovu zadnju funkciju
# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer):
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']['name']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()
  
