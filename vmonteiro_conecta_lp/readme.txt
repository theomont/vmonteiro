Instruções de portabildiade

Para trabalhar dentro do ambiente virtual deve-se instalar o Virtualenv através do comando:
$ virtualenv -p python3 venv
(obs.: caso essa pasta exista exclua-a antes de realizar o comando)

Execute o ambiente virtual através do comando
$ . ./venv/bin/activate

Para garantir que todos os pacotes estão instalados nos eu ambiente virtual utilize o comando
$ ./venv/bin/pip3 install -r requirements.txt
Nota: Caso utilize algum outro pacote, após instala-lo atualize o requiremente.txt atraves do comando:
$ ./venv/bin/pip3 freeze > requirements.txt

A execução do código se dá através do flask Manager
$ python3 run.py runserver

Sendo assim todos os demais comandos também serão dados atraves do Flask Manager, como por exemplo:
$ python3 run.py db init
$ python3 run.py db migrate
$ python3 run.py db upgrade

Rodando no servidor a aplicação com acesso via dominio vinculado/ porta 80
$ python3 run.py runserver --host 0.0.0.0 --port 80

Acessando o servidor via SSH
$ ssh root@107.170.19.122 
