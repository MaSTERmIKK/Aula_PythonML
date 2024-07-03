class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f"L'unità {self.nome} si muove.")

    def attacca(self):
        print(f"L'unità {self.nome} attacca il nemico.")

    def ritira(self):
        print(f"L'unità {self.nome} si ritira strategicamente.")

class Fanteria(UnitaMilitare):
    def costruisci_trincea(self):
        print(f"La fanteria {self.nome} costruisce trincee.")

class Artiglieria(UnitaMilitare):
    def calibra_artiglieria(self):
        print(f"L'artiglieria {self.nome} calibra i cannoni.")

class Cavalleria(UnitaMilitare):
    def esplora_terreno(self):
        print(f"La cavalleria {self.nome} esplora il terreno.")

class SupportoLogistico(UnitaMilitare):
    def rifornisci_unita(self):
        print(f"Supporto Logistico {self.nome} rifornisce le unità.")

class Ricognizione(UnitaMilitare):
    def conduci_ricognizione(self):
        print(f"Ricognizione {self.nome} conduce una missione di sorveglianza.")

class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
    def __init__(self):
        self.unita_registrate = {}

    def registra_unita(self, unita):
        self.unita_registrate[unita.nome] = unita

    def mostra_unita(self):
        for nome in self.unita_registrate:
            print(nome)

    def dettagli_unita(self, nome):
        unita = self.unita_registrate.get(nome)
        if unita:
            print(f"Dettagli di {nome}: {unita.numero_soldati} soldati")
        else:
            print("Unità non trovata.")
