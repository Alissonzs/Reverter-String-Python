# Reversão de String com Pilha

Este projeto implementa um programa Python que reverte uma string utilizando uma estrutura de dados chamada pilha. A pilha segue a característica LIFO (Last In, First Out), que é aplicada para inverter a ordem dos caracteres de uma string de maneira eficiente.

## Funcionalidade
- O programa recebe uma string como entrada.
- Cada caractere da string é empilhado usando o método `push`.
- Os caracteres são retirados da pilha usando `pop` e concatenados para formar a string invertida.

## Testes Realizados
- **Entrada:** "abcdef" → **Saída Esperada:** "fedcba"
- **Entrada:** "hello world" → **Saída Esperada:** "dlrow olleh"
- **Entrada:** "a!b@c#" → **Saída Esperada:** "#c@b!a"
- **Entrada:** "12345" → **Saída Esperada:** "54321"

## Conclusões
- A pilha é uma estrutura de dados simples, mas eficiente, para resolver problemas que exigem operações na ordem reversa.
- A solução foi eficaz na inversão de strings e pode ser aplicada em áreas como criptografia e processamento de linguagem natural.
- O uso da pilha facilitou a implementação de uma solução intuitiva e de fácil entendimento.

## Como Executar
Para rodar o programa, basta executar o arquivo Python. O programa solicitará a entrada de uma string e exibirá a string invertida.
