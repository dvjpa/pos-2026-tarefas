from xml.dom import minidom
import os

def parse_cardapio():

    arquivo = "Tarefa 01/cardapio.xml"
    
    if not os.path.exists(arquivo):
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado nesta pasta.")
        return

    try:
        dom = minidom.parse(arquivo)
        pratos = dom.getElementsByTagName("prato")
        
        print("\n" + "="*30)
        print("      MENU DE PRATOS")
        print("="*30)
        
        for prato in pratos:

            id_prato = prato.getAttribute("ID")
            nome = prato.getElementsByTagName("nome")[0].firstChild.data
            print(f"[{id_prato}] - {nome}")
        
        print("="*30)
        escolha = input("Digite o ID do prato (ex: P01) ou 'sair': ").strip()

        if escolha.lower() == 'sair':
            return

        for prato in pratos:

            if prato.getAttribute("ID") == escolha:
                nome = prato.getElementsByTagName("nome")[0].firstChild.data
                desc = prato.getElementsByTagName("descricao")[0].firstChild.data
                preco = prato.getElementsByTagName("preco")[0].firstChild.data
                moeda = prato.getElementsByTagName("preco")[0].getAttribute("moeda")
                cal = prato.getElementsByTagName("calorias")[0].firstChild.data
                tempo = prato.getElementsByTagName("tempopreparo")[0].firstChild.data
                
                print("\n" + "-"*40)
                print(f"DETALHES: {nome.upper()}")
                print(f"-"*40)
                print(f"Descrição: {desc}")
                print(f"Preço:     {moeda} {preco}")
                print(f"Calorias:  {cal} kcal")
                print(f"Preparo:   {tempo}")
                
                ingredientes = prato.getElementsByTagName("ingrediente")
                print("Ingredientes:", end=" ")
                lista_ing = [i.firstChild.data for i in ingredientes]
                print(", ".join(lista_ing))
                print("-"*40)
                return

        print(f"\n[!] Erro: ID '{escolha}' não encontrado. Use letras maiúsculas (ex: P01).")

    except Exception as e:
        print(f"Ocorreu um erro técnico: {e}")

if __name__ == "__main__":
    parse_cardapio()