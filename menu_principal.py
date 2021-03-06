import pacientes as pt
import medicos as md
import consultas as ct
import administracao as adm

" Author: Everton Andrade "


def menu_principal():
    print(20 * "-=")
    print("       SISTEMA DE CLÍNICA MÉDICA")
    print(20 * "-=")

    print("--------------------\n"
          "1 - Pacientes\n"
          "2 - Médicos\n"
          "3 - Consultas\n"
          "4 - Administrativo\n"
          "5 - Fechar\n"
          "--------------------")

    while True:
        atendimento = int(input("Escolha o tipo de atendimento a ser usado: "))
        if atendimento == 1:
            pt.menu_pacientes()
        if atendimento == 2:
            md.menu_medicos()
        if atendimento == 3:
            ct.menu_consultas()
        if atendimento == 4:
            adm.menu_administracao()
        if atendimento == 5:
            break
        else:
            print("Opção inválida!\n")


menu_principal()
