from socket import *
servidor="127.0.0.1"
porta=43210
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor,porta))
obj_socket.listen(2)
print("Aguardando cliente....")
while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", str(msg_recebida)[2:-1])
        msg_enviada = bytes(input("Sua resposta: "), 'utf-8')
        con.send(msg_enviada)
        break
    con.close()
    """
    Vamos a uma explicação sobre o que está ocorrendo nesse código:

1. Primeiramente, importamos todas (*) as funções da biblioteca “socket”, isso será preciso para que
possamos criar objetos do tipo “socket”.
2. Criamos duas variáveis, “servidor” e “porta”, para armazenarmos esses dois dados que serão utilizados
posteriormente; em “servidor”, poderíamos utilizar também a palavra “localhost” para identificarmos que
o servidor é a própria máquina que está executando o código, o que também é representado pelo
endereço “127.0.0.1”, que foi aqui utilizado. Em “porta”, escolhemos uma porta representada por um
número inteiro entre 0 e 65535, em que normalmente as portas entre 0 e 1023 são portas utilizadas, por
padrão, para atribuições de serviços conhecidos por meio do sistema operacional.

3. Na quarta linha, criamos o nosso objeto socket “obj_socket”, por meio da função “socket()”, que exige
dois parâmetros: o primeiro definirá a família responsável por identificar os pacotes. Para o nosso
exemplo, definimos como AF_INET, o que significa que iremos utilizar a identificação do
emissor/receptor do(s) pacote(s) via DNS ou número IP (poderíamos utilizar a constante AF_UNIX, o
que mudaria a forma de identificar a origem/destino do(s) pacote(s)). Já o segundo parâmetro refere-se
ao transporte desse pacote, que pode ser SOCK_STREAM, que representa o protocolo TCP (o que nós
optamos) ou SOCK_DGRAM, que representa o protocolo de transporte UDP.
4. Na próxima linha, fazemos a associação no nosso objeto socket com o nosso servidor e porta.
5. Na linha em que utilizamos a função “listen()”, estamos definindo o máximo de clientes que o nosso
servidor irá atender simultaneamente, para o nosso caso, definimos que serão, no máximo, dois (2)
clientes.
6. Montamos, na sequência, dois laços infinitos (enquanto for verdadeiro): no primeiro, aguardamos a
chamada de um cliente (por meio da função accept()), assim que tivermos, receberemos uma tupla e
iremos direcionar a identificação do cliente para a variável “cliente” e a identificação da conexão para a
variável “con” e, então, iremos exibir a identificação do nosso cliente;
7. No segundo laço, aguardando uma solicitação que pode ser transmitida em pacotes de 1024 bytes,
exibimos a mensagem recebida e geramos uma mensagem para enviar no formato de “bytes” (por isso,
a mensagem começa com “b” e, em seguida, a string que se deseja), enviamos por meio do método
“send()” e encerramos esse segundo laço while.
8. Finalmente, fechamos a conexão e voltamos a aguardar uma nova conexão.

Todos os dados transmitidos via socket devem estar no formato byte. O socket não envia nem recebe da‐
dos strings, por exemplo.

*para melhorar a interatividade algumas linhas de codigo foram atualizada com observações: Em relação ao novo 
código do servidor apresentado, 
alteramos somente o conteúdo do segundo while, no qual
estamos convertendo a mensagem que recebemos para string (str(msg_recebida) e, em seguida, fazendo um
slice ([2:-1]) dela, em que pegamos do segundo caractere até o último caractere da string, com isso, quando re‐
cebermos, por exemplo: b’olah servidor’, será exibido apenas: olah servidor. Alteramos também a linha refe‐
rente ao conteúdo da variável msg_enviada, que antes era uma mensagem única e agora é definida por meio do
input(), no qual o usuário irá digitar o que desejar.

    """