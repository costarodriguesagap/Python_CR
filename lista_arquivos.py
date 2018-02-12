import Utilitarios,Directorio,sys

def obtem_arquivos(path_raiz,f_w):
  res = Directorio.scan_dir(path_raiz)
  for arch in res[1]:
    if arch[0] == "D":
      obtem_arquivos(path_raiz+"\\"+arch[1],f_w)
    else:
      try:
        file_name = str(path_raiz)+"\\"+arch[1]+'\n'
        if arch[1][:2] != "~$":
          f_w.write(file_name)
      except:
        print("Erro na escrita ficheiro ....")

if __name__ == "__main__":
  path_ini = str(Utilitarios.get_input("Directorio raiz para Pesquisa?\n"))
  diract = Directorio.act_dir()
  
  try:
    f_res = open("resultado1.txt",'w')
    obtem_arquivos(path_ini,f_res)
    f_res.close()
  except:
    print("Erro na abertura do ficheiro ....")
    
  cmd ="start "+diract+"\\resultado1.txt"
  Utilitarios.cmd_exec(cmd,False)
