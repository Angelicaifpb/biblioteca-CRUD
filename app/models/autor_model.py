class AutorModel:
    def __init__(self, id, nome, nacionalidade, data_nascimento):
        self.__id = id
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__data_nascimento = data_nascimento

    # Getters
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_nacionalidade(self):
        return self.__nacionalidade

    def get_data_nascimento(self):
        return self.__data_nascimento

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
