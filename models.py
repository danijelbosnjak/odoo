# -*- coding: utf-8 -*-

from openerp import models, fields, api

# Tablica za klijente. Ime klase nema smisla ako se tablica zove klijenti. Trebalo bi nastimati da bude smisleno
class Rentacar(models.Model):
# Ime tablice u bazi samo sto je u kreirana kao "rentacar_klijenti" sa underscore
# Isto pravilo vrijedi i za druge clase za varijablu _name
	_name = 'rentacar.klijenti'

	name = fields.Char(string="Ime", required=True)
	lastname = fields.Char(string="Prezime", required=True)
	address = fields.Char(string="Adresa", required=True)
	city = fields.Char(string="Grad", required=True)
	country = fields.Char(string="Drzava", required=True)
	birth_date = fields.Date()
	note = fields.Text()

# Tablica za automobile.
class Automobili(models.Model):
	_name = 'rentacar.automobili'
	
	car_brand = fields.Char(string="Marka automobila")
	car_model = fields.Char(string="Model automobila")
	car_plates = fields.Char(string="Reg oznaka")
	car_year = fields.Date()

# Tablica za rezervacije
class Rezervacija(models.Model):
	_name = 'rentacar.rezervacija'

# Relacija izmedju tablice klijent i tablice rezervacija tako da u GUIU dropdown pod sekcijom  "Rezervacije" ponudi odabir mogucih klijenata 	
	korisnik_id = fields.Many2one('rentacar.klijenti', string="Klijent")
# Relacija izmedju tablice automobili i tablice rezervacija isto se ponasa kao korisnik_id tj. dropdown opcija u GUIU
	automobil_id = fields.Many2one('rentacar.automobili', string="Automobil")
# Pocetak najma, GUI izbaci javascript kalendar
	start_date = fields.Date()
# Kraj najma 
	end_date = fields.Date()
# Bool, GUI pokaze kvacicu za oznaciti
	cash_pay = fields.Boolean(string="Gotovina")
	card_pay = fields.Boolean(string="Kartica")
# Ovaj parametar i parametri kao ovaj sluze za moguce kalkulacije upisanih vrijednosti u GUI npr. postotak, snizenje...
# Metoda fields.Float() uzima kao parametar compute koji pak trazi ime funkije koja radi neku radnju "kalkulacije" unesenih vrijednosti!
# Hmmm ovo moram bolje istraziti! Btw. opisi var name ocajan, treba promijeniti.
	opisi = fields.Float(compute="_calculate_price")

# @api.depends je decorator koji za parametre uzima vrijednosti iz klase o kojima ovisi metoda/funkcija ispod njega u ovom slucaju _calculate_price. 
# U ovom slucaju sam stavio opisi ali tu bi npr trebalo ici
# start_date,end_date i npr cijena dnevna auta car_price tako da izracuna razliku dana te npr. pomnozi sa dnevnom cijenom auta i tako se dobije iznos za platit.
# (t1 - t2 ) * dnevna_cijena_auta npr.
	@api.depends('opisi')
	def _calculate_price(self):
# Ovo je samo testna kalkulacija da vidim da li se vidi u GUIU. Nije smislena. Ugl. vidi se u GUIU
		self.opisi = 700.0 * 4.0
#		record.opisi = self.opisi


# Tablica za cijene tj. cjenik!
class Cijene(models.Model):
	_name = 'rentacar.cijene'
# Dnevna cijena	
	car_price = fields.Float(string="Cijena")
# Relacija na tablicu automobil
	automobil_id = fields.Many2one('rentacar.automobili', string="Automobil")	 


# class rentacar(models.Model):
#     _name = 'rentacar.rentacar'

#     name = fields.Char()