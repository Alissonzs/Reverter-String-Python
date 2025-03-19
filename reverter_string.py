from pilha import Pilha  # Importando a classe Pilha do arquivo pilha.py

def reverter_string(texto):
    pilha = Pilha()

    # Empilhando cada caractere da string
    for char in texto:
        pilha.push(char)

    string_reversa = ""

    # Desempilhando para reverter a string
    while not pilha.esta_vazia():
        string_reversa += pilha.pop()

    return string_reversa

if __name__ == "__main__":
    entrada = input("Digite uma string para reverter: ")
    resultado = reverter_string(entrada)
    print(f"String invertida: {resultado}")
