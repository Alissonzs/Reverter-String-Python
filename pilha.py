class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.esta_vazia():
            return self.itens.pop()

    def peek(self):
        if not self.esta_vazia():
            return self.itens[-1]

    def esta_vazia(self):
        return len(self.itens) == 0

def reverter_string(s):
    pilha = Pilha()
    # Inserir cada caractere na pilha
    for char in s:
        pilha.push(char)
    
    # Recuperar os caracteres em ordem reversa
    string_revertida = ""
    while not pilha.esta_vazia():
        string_revertida += pilha.pop()
    
    return string_revertida

# Teste
entrada = input("Digite uma string para reverter: ")
print(f"String revertida: {reverter_string(entrada)}")
