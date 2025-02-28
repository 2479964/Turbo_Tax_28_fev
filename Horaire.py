class Horaire:
    """
    Classe Horaire
    """
    def __init__(self, temps_ecole: int = 10):
        """
        Constructeur de la classe Horaire
        :param temps_ecole: nombre de temps à l'école
        """
        self._temps_ecole = temps_ecole
        self.pauses: list = []


    def get_temps_ecole(self):
        return self._temps_ecole

    def set_temps_ecole(self, temps_ecole: int):
        if isinstance(temps_ecole, int) and 0 <= temps_ecole <= 10:
            self._temps_ecole = temps_ecole

    def planifier_pause(self):
        heure = 1
        pauses = input("Ajouter les heures de pause séparées par une virgule: ").split(",")
        for p in pauses:
            self.pauses.append(int(p))
            print(self.pauses)
        while heure <= self._temps_ecole:
            print(f"Heure numéro {heure} d'école: ")
            for p in self.pauses:
                if p == heure:
                    print("L'étudiant est en pause.")
                else:
                    print(L'étudiant est en cours.')
            heure += 1