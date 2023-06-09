from socket import *

servidor="127.0.0.1"
porta=43210

while True:
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((servidor, porta))
    msg = bytes(input("Sua mensagem: "), 'utf-8')
    obj_socket.send(msg)
    resposta=obj_socket.recv(1024)
    print("Resposta do Servidor: ", str(resposta)[2:-1])
    if str(msg)[2:-1].upper()=="FIM":
        break
obj_socket.close()
"""
Detalhando as linhas do código apresentado:

1. Importamos as funções da biblioteca socket e criamos duas variáveis, uma para representar o servidor,
caso o servidor não fosse a máquina local, poderíamos definir o IP do servidor externo, se fosse o caso.
Cuidado ao definir a porta, deve ser a mesma em que inicializamos o servidor.
2. Na quarta linha, definimos o conteúdo da variável “msg”, por meio de uma entrada do usuário (input).
Observe que utilizamos a função “bytes()” para converter o conteúdo do input, ou seja, a string para o
formato bytes, mais uma vez, lembrando: o socket transmite somente dados do tipo byte. A função
“bytes()” possui o segundo parâmetro que faz referência ao padrão de caracteres “utf-8”.
3. As três próximas linhas são referentes à criação do objeto socket (por meio da função “socket()”), à
conexão com o servidor, por meio da função “connect()”, e, finalmente, enviando uma mensagem para o
servidor, utilizando o método “send()”.
4. A variável resposta recebe o dado enviado pelo servidor, limitando o tamanho para 1024 bytes.
5. E finalizamos o código, exibindo a resposta e fechando conexão.

*atualizando a interatividade do codigo
Do lado do cliente, foi incluído o laço while, para que o cliente possa mandar mais que uma mensagem ao servi‐
dor, deixamos de fora do while somente a definição do servidor (ip e porta) e o encerramento da conexão. A res‐
posta do servidor também foi convertida para string e foi realizado o slice da string para considerar somente a
mensagem válida.

"""