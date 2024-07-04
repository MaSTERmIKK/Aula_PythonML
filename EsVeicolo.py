class Veicolo:
    def __init__(self, marca, modello, anno):
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione = False

    def accendi(self):
        self._accensione = True
        print(f"{self._marca} {self._modello} accesa.")

    def spegni(self):
        self._accensione = False
        print(f"{self._marca} {self._modello} spenta.")

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self._numero_porte = numero_porte

    def suona_clacson(self):
        print("Beep beep!")

class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, capacità_carico):
        super().__init__(marca, modello, anno)
        self._capacità_carico = capacità_carico

    def carica(self):
        print(f"Carico {self._capacità_carico}kg nel furgone.")

    def scarica(self):
        print("Scarico il furgone.")

class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self._tipo = tipo

    def esegui_wheelie(self):
        if self._tipo == 'sportiva':
            print("Wheelie eseguito!")
        else:
            print("Questa motocicletta non è adatta per wheelies.")

class GestoreParcoVeicoli:
    def __init__(self):
        self._veicoli = []

    def aggiungi_veicolo(self, veicolo):
        self._veicoli.append(veicolo)
        print(f"Aggiunto: {veicolo._marca} {veicolo._modello}")

    def rimuovi_veicolo(self, marca, modello):
        self._veicoli = [v for v in self._veicoli if not (v._marca == marca and v._modello == modello)]
        print(f"Rimosso: {marca} {modello}")

    def lista_veicoli(self):
        for v in self._veicoli:
            print(f"{v._marca} {v._modello}, anno {v._anno}")

# Esempio di utilizzo
parco = GestoreParcoVeicoli()
parco.aggiungi_veicolo(Auto("Fiat", "500", 2020, 4))
parco.aggiungi_veicolo(Furgone("Mercedes", "Sprinter", 2018, 1000))
parco.aggiungi_veicolo(Motocicletta("Yamaha", "R1", 2021, "sportiva"))
parco.lista_veicoli()
