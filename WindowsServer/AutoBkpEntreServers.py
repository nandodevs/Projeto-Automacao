import os
import shutil
import datetime

#arquivo que contem a lista
server_list = 'cenario.txt'

#diretorio que contem os arquivos a serem copiados
bin_dir = r'\\server\pasta'

#funcao padrao para mostrar mensagens com data e hora
def show_msg(msg):
      print('%s: %s' % (str(datetime.datetime.now().strftime
      ("%Y-%m-%d %H:%M:%S")), msg))

#verifica se o arquivo com a lista de servidores existe
if not os.path.exists(server_list):
      show_msg('Arquivo %s nao encontrado' % (server_list))
      exit(1)

#verifica se o diretorio com os arquivos a serem copiados existe
if not os.path.exists(bin_dir):
      show_msg('Diretorio %s nao encontrado' % (bin_dir))
      exit(1)

#lista os arquivos a serem copiados
bin_files = os.listdir(bin_dir)

#verifica se existem arquivos a serem copiados
if len(bin_files) == 0:
      show_msg('Nenhum arquivo encontrado em %s para ser copiado'
       % (bin_dir))
      exit(1)

#abre o arquivo que contem a lista de servidores
servers = open(server_list, 'r')

#monta loop que executara os comandos para cada servidor
for entry in servers:
      (server, dir) = entry.rstrip().split('|')
      path = r'\\%s\%s' % (server, dir)

      #se o diretorio de destino nao existir, crie
      if not os.path.exists(path):
            os.mkdir(path)
      #monta loop que copiara cada arquivo para o servidor de destino
      for file in bin_files:
            shutil.copy(os.path.join(bin_dir, file), os.path.join(path, file))
            show_msg('Arquivo %s copiado para o servidor %s' % (file, server))

servers.close()