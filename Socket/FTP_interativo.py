import os
from ftplib import *
ftp_ativo=False
ftp = FTP(input("Digite o FTP que se deseja conectar: ")) #digite por exemplo ftp.ibge.gov.br
print(ftp.getwelcome())
usuario=input("Digite o usuario: ") #pode deixar em branco
senha=input("Digite a senha: ") #pode deixar em branco
ftp.login(usuario, senha)
print("Conexão bem sucedida.Diretório atual de trabalho: ", ftp.pwd(),"")
menu="1"
while menu=="1" or menu=="2" or menu=="3":
    menu=input("Escolha a opção desejada: "     " + <1> - para Listar arquivos" +      "<2> - para definir um diretório"       "<3> - para baixar um arquivo: ")
    if menu=="1":
        print(ftp.dir())
    elif menu=="2":
        ftp.cwd(input("Digite o diretório que deseja entrar: "))
        print("Diretório corrente é: ", ftp.pwd())
    elif menu=="3":
        tipo=input("Digite <B> para arquivo binário ou "           "qualquer outra letra para arquivo ASCII: ").upper()
        if tipo=="B":
            with open(input("Digite o nome do arquivo destino: "), 'wb') as arq:
                ftp.retrbinary('RETR ' + input("Arquivo de origem: "), arq.write)
        else:
            with open(input("Digite o nome do arquivo destino: "), 'w') as arq:
                def escreverLinha(data):
                    arq.write(data)
                    arq.write(os.linesep)
                ftp.retrlines('RETR ' + input("Arquivo de origem:"), escreverLinha)
        print("Arquivo baixado com sucesso!")
ftp.quit()
"""
Com base nesse código, realizamos uma interação maior com o usuário, o que permite utilizar o código em di‐
versas situações. Vamos acompanhar linha a linha:

1. Linhas 1 e 2: realizamos os imports das bibliotecas que serão necessárias para o decorrer do código.

2. Linha 3: configuramos nossa variável para uma conexão passiva.

3. Linha 4: definimos o objeto “ftp”, que representará nossa conexão conforme o que o usuário digitar.

Quando executar digite, por exemplo, “ftp.ibge.gov.br”.

4. Linhas 5, 6, 7, 8 e 9: exibimos a mensagem de boas-vindas, solicitamos usuário e senha (pode deixar
vazios os dois, para o exemplo do “ibge”), estabelecemos o login, por fim, mostramos uma mensagem de
que a conexão foi estabelecida e apresentamos o diretório atual.

5. Linhas 10, 11, 12, 13, 14 e 15: criamos uma variável “menu” para que o usuário escolha uma das opções
desejadas, enquanto o usuário digitar algo igual a 1, 2 ou 3, o laço será repetido e o usuário perguntado
novamente sobre qual ação deseja realizar.

6. Linhas 16 e 17: se o usuário digitar o número “1”, iremos exibir uma listagem do diretório atual, exibindo
arquivos e diretórios; após a exibição, irá voltar para o menu. IR PARA O TOPO
ÍNDICE


7. Linhas 18, 19 e 20: se o usuário digitar o número “2”, iremos mudar de diretório de acordo com o que o
usuário digitar. Seguindo o nosso exemplo, digite: “seculoxx”, em seguida, será exibido o diretório atual e
voltará ao menu, utilize novamente a opção “1” para exibir o conteúdo do diretório “seculoxx”.

8. Linhas 21, 22 e 23: se o usuário digitar o número “3”, iremos perguntar o que ele deseja baixar. Se for um
arquivo binário, ele deverá digitar a letra “b”. Qualquer outro caractere irá considerar o que ele deseja
baixar como ASCII. Seguindo o nosso exemplo, digite “B”.

9. Linhas 24, 25 e 26: nesse caso, se o usuário digitou “B”, iremos pedir o nome do arquivo destino. Diante
do nosso exemplo, digite “zipado.zip” (o nome do arquivo deve ser completo, inclusive, com a extensão),
em seguida, ele pedirá o arquivo de origem; seguindo o nosso exemplo, escolheremos o arquivo
“representacao_politica.zip” (o nome do arquivo deve ser completo, inclusive, com a extensão). Cuidado
que o nome do arquivo deve ser exatamente igual ao que está aparecendo na listagem. Aguarde até
surgir a mensagem “Arquivo baixado com sucesso” e, então, aparecerá o menu novamente. Escolha a
opção “3” para baixar um arquivo e, na próxima pergunta, digite qualquer letra diferente de “B”, pois
iremos baixar um arquivo “ASCII”.

10. Linhas 27 e 28: se o usuário digitar qualquer letra diferente de “B”, representa que deseja baixar um
arquivo “ASCII”. Ele solicitará o nome do arquivo de destino; seguindo o nosso exemplo, digite:
“textobaixado.txt” (inclusive com a extensão).

11. Linhas 29, 30 e 31: criamos a função para realizar a leitura das linhas e a identificação do sistema
operacional em relação ao separador de linha utilizado dentro do arquivo.

12. Linha 32: irá solicitar o nome do arquivo de origem. Seguindo o nosso exemplo, digite o arquivo
“leia_me.txt”, exatamente igual. E então, o “arq” será escrito com base no “leia_me.txt”.

13. Linha 33: exibimos a mensagem de que o arquivo foi baixado (CUIDADO com a tabulação dessa linha) e
voltaremos para o menu.

14. Linha 34: somente será executada se o usuário digitar algo diferente de “1”, “2” ou “3”, o que encerrará a
conexão.

Se você seguiu os nossos passos, durante a explicação das linhas, deverá ter, no mesmo diretório do arquivo
“FTP_Interativo.py”, os arquivos: “zipado.zip” e “textobaixado.txt”. Nele, poderá exibi-los ou descompactá-los,
no caso do arquivo compactado. Assim, o seu usuário poderá interagir em qualquer servidor FTP, navegar entre
os diretórios e baixar arquivos ASCII ou binários.

Agora, imagine se pudermos criar uma interface a fim de sairmos do console, o que acha? Legal, não é mesmo?
Vamos desenvolver nossas interfaces, criar ferramentas mais interativas e conectar nossas ferramentas a disposi‐
tivos IoT. Aguarde... cenas do próximo capítulo!
"""