import hashlib


class Usuario:
    def __init__(self, descricao='', nome='', senha=''):
        self.descricao = descricao
        self.nome = nome
        self.senha = self.criptografar_senha(senha)

    def fazer_login(self, senha):
        # verifica se a senga inserido corresponde á senha armazenada
        senha_inserida_criptografada = self.criptografar_senha(senha)
        return senha_inserida_criptografada == self._senha

    def configurar_usuario_padrao(self):
        pass

    def cadastrar_usuario(self):
        self._descricao = input('Digite a descrição do usuário: ').strip()
        self._nome = input('Digite o nome do novo usuário: ').strip().upper()
        senha = input('Digite a senha do novo usuário: ').strip()
        self._senha = self.criptografar_senha(senha)

    def __str__(self):
        return f"Descrição: {self._descricao}, Nome: {self._nome}, Senha: {self.__senha}"

    def apagar_usuario(self):
        pass

    def listar_usuario(self):
        pass

    def criptografar_senha(self, senha):
        # Crie um objeto de hash SHA-256
        sha256 = hashlib.sha256()

        # Converta a senha em bytes, pois o hashlib requer bytes
        senha_bytes = senha.encode('utf-8')

        # Atualize o objeto de hash com os bytes da senha
        sha256.update(senha_bytes)

        # Obtenha o hash criptografado como uma string hexadecimal
        senha_criptografada = sha256.hexdigest()

        return senha_criptografada


if __name__ == "__main__":
    # Cadastra um usuário
    usuario1 = Usuario()
    usuario1.cadastrar_usuario()

    # Faz login
    senha_inserida = input('Digite a senha para fazer login: ').strip()
    if usuario1.fazer_login(senha_inserida):
        print("Login bem-sucedido!")
    else:
        print("Senha incorreta. Login falhou.")