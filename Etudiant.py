from Devoir import Devoir
# from Horaire import Horaire
class Etudiant:
    """
    Classe Etudiant
    """
    def __init__(self, nom: str, session: int, devoirs: list[Devoir], horaire: str):
        """
        Constructeur de la classe Etudiant
        :param nom: Nom de l'étudiant.
        :param session: # de session.
        :param devoirs: Liste de devoirs à faire.
        :param horaire: Son horaire.
        """
        self.nom = nom
        self.session = session
        self.devoirs = devoirs
        self.horaire = horaire

    def faire_devoir(self, devoir: Devoir):
        print("Voici la liste des devoirs : ")
        for i in self.devoirs:
            print(i)
        choix = input("Veuillez entrer le devoir que vous voulez faire : ")
        for i in self.devoirs:
            if choix == i:
                self.devoirs.remove(i)

    def __str__(self):
        return f"""
Nom : {self.nom}
Session : {self.session}
Devoirs : {self.devoirs}
Horaire : {self.horaire}
"""