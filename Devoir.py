class Devoir:
    """
    Classe Devoir
    """
    def __init__(self, nom, type, matiere):
        """
        Constructeur de la classe Devoir
        :param nom: str
        :param type: str
        :param matiere: str
        """
        self.nom = nom
        self.type = type
        self.matiere = matiere


    def __str__(self):
        return f"""
        nom = {self.nom}
        type = {self.type}
        matiere = {self.matiere}   
        """