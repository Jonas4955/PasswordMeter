from app.requiriments.requirement import Requirements

class Score(Requirements):
    def __init__(self, passwd):
        self.__pass = passwd
        super().__init__(self.__pass)

    def score_por_letras(self):
        score_letra = 100 / self.characters_passwd()
        return score_letra

