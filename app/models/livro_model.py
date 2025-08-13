class LivroModel:
    def __init__(self, id, titulo, genero, ano_publicacao, autor_id):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__ano_publicacao = ano_publicacao
        self.__autor_id = autor_id

    # Getters
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def get_ano_publicacao(self):
        return self.__ano_publicacao

    def get_autor_id(self):
        return self.__autor_id

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero

    def set_ano_publicacao(self, ano_publicacao):
        self.__ano_publicacao = ano_publicacao

    def set_autor_id(self, autor_id):
        self.__autor_id = autor_id
