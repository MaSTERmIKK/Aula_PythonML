class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0):
        self._titolare = titolare
        self._saldo = saldo_iniziale

    def deposita(self, importo):
        if importo > 0:
            self._saldo += importo
            print(f"Depositati {importo}€. Saldo attuale: {self._saldo}€.")
        else:
            print("L'importo del deposito deve essere positivo.")

    def preleva(self, importo):
        if importo > 0 and self._saldo >= importo:
            self._saldo -= importo
            print(f"Prelievo di {importo}€ effettuato. Saldo attuale: {self._saldo}€.")
        else:
            print("Importo non valido o saldo insufficiente.")

    def visualizza_saldo(self):
        return self._saldo

    # Getter e Setter per _titolare
    @property
    def titolare(self):
        return self._titolare

    @titolare.setter
    def titolare(self, nuovo_titolare):
        if isinstance(nuovo_titolare, str) and nuovo_titolare:
            self._titolare = nuovo_titolare
        else:
            print("Il nome del titolare deve essere una stringa valida.")

# Esempio di utilizzo
conto = ContoBancario("Mario Rossi", 1000)
conto.deposita(500)
conto.preleva(200)
print(f"Saldo finale: {conto.visualizza_saldo()}€")
conto.titolare = "Giulia Bianchi"
