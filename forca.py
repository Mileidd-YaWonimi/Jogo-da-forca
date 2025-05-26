class Forca:
    def __init__(self, palavra):
        self.palavra = palavra.upper()
        self.letras_certas = []
        self.letras_erradas = []
        self.estado = 'jogando'

    def get_palavra_oculta(self):
        return ' '.join([letra if letra in self.letras_certas else '_' for letra in self.palavra])

    def tentar(self, letra):
        if letra in self.letras_certas or letra in self.letras_erradas:
            return self.estado
        if letra in self.palavra:
            self.letras_certas.append(letra)
            if all(l in self.letras_certas for l in self.palavra):
                self.estado = 'venceu'
        else:
            self.letras_erradas.append(letra)
            if len(self.letras_erradas) >= 6:
                self.estado = 'perdeu'
        return self.estado
