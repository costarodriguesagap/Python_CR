import Utilitarios, platform, os

loop = True

if __name__ == "__main__":
    
    while loop:
        
        res_instalar = 0
        modulo = ""
        print("----- Opcao 1 - Instalar Modulo ------------------")    
        print("----- Opcao 2 - Actualizar Modulo ----------------")
        print("----- Opcao 3 - Desinstalar Modulo ---------------")
        print("----- Opcao 4 - Consultar Modulos Instalados -----")
        print("----- Opcao 5 - Executar comando PIP (ADHOC) -----")
        print("----- Opcao 6 - Consultar Versão do Python -------")
        print("----- Opcao 7 - Consultar Documentação Modulos ---")
        opcao_res = int(Utilitarios.get_input("\nInsira a sua Opcao: "))
        
        if opcao_res == 1:
            modulo = str(Utilitarios.get_input("Indique o Modulo a Instalar: "))
            res_instalar = int((Utilitarios.cmd_pip("pip show " + modulo, True)))
            if res_instalar == 0:
                print("Modulo já está Instalado")
            else:
                Utilitarios.cmd_pip("pip install --no-cache-dir " + modulo, True)

        if opcao_res == 2:
            modulo = str(Utilitarios.get_input("Indique o Modulo a Actualizar: "))
            res_instalar = int((Utilitarios.cmd_pip("pip show " + modulo, True)))
            if res_instalar == 1:
                print("Modulo ainda não se encontra Instalado, Instale primeiro o modulo na Opcao 1")
            else:
                Utilitarios.cmd_pip("pip install " + modulo + " --upgrade", True)

        if opcao_res == 3:
            modulo = str(Utilitarios.get_input("Indique o Modulo a Desinstalar: "))
            res_instalar = int((Utilitarios.cmd_pip("pip show " + modulo, True)))
            if res_instalar == 1:
                print("Modulo ainda não se encontra Instalado")
            else:
                Utilitarios.cmd_pip("pip uninstall -y " + modulo, True)

        if opcao_res == 4:
            Utilitarios.cmd_pip("pip list", True)

        if opcao_res == 5:
            Utilitarios.cmd_pip(str(Utilitarios.get_input("Insira o comando: ")), True)

        if opcao_res == 6:
            print("\nVersão Python: " + platform.python_version())

        if opcao_res == 7:
            modulo = str(Utilitarios.get_input("Indique o Modulo a Consultar: "))

            cmd_import = "import " + modulo
            cmd_cod  = "help(" + modulo + ")"
            exec cmd_import
            exec cmd_cod

            
        control = Utilitarios.get_input("\nPretende Continuar?: ('S' - Sim ou 'N' - Não) \nR:")

        if (control.upper() == "N"):
            loop = False

        os.system("cls")
