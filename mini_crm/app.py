from model import model_lead
import control

def list_leads():
    leads = control.read_leads()

    # formatar como tabela
    for lead in leads:
        print(lead)

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    status = input("Etapa no funil de vendas: ")

    # validar dados
    # modelar dados
    # modelar leads como dicionario
    print(model_lead(name, email, status))

    # depois de modelar o lead como dict
    # enviar dict para o lead.json
    # usar control
    control.create_lead(model_lead(name, email, status))

    print("lead adiciona (func)")

def main():
    while True:
        print("\nMini CRM de Leads\n")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do programa")

        op = input("Escolha uma opção: ")

        if op == "1":
            add_lead()
        elif op == "2":
            list_leads()
        elif op == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()