import json
import os

def carregar_dados():
    arquivo = "imobiliaria.json"
    if not os.path.exists(arquivo):
        print(f"Erro: O ficheiro '{arquivo}' não foi encontrado. rode primeiro a Tarefa 09.")
        return None

    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def exibir_menu(imoveis):
    print("\n" + "="*40)
    print("      SISTEMA DE IMÓVEIS (JSON)")
    print("="*40)
    
    for i, imovel in enumerate(imoveis):
        tipo = imovel.get("tipo", "Imóvel")
        bairro = imovel.get("endereco", {}).get("bairro", "N/A")
        print(f"[{i}] - {tipo} em {bairro}")
    
    print("="*40)

def exibir_detalhes(imovel):
    print("\n" + "*"*40)
    print("DETALHES DO IMÓVEL")
    print("*"*40)
    
    print(f"Tipo:      {imovel.get('tipo', 'N/A')}")
    print(f"Valor:     R$ {imovel.get('valor', 'N/A')}")
    
    end = imovel.get("endereco", {})
    print(f"Endereço:  {end.get('rua', 'N/A')}, Nº {end.get('numero', 'N/A')}")
    print(f"Bairro:    {end.get('bairro', 'N/A')}")
    print(f"Cidade:    {end.get('cidade', 'N/A')}")
    
    carac = imovel.get("caracteristicas", {})
    if carac:
        print("\nCaracterísticas:")
        for k, v in carac.items():
            print(f"- {k.capitalize()}: {v}")
    
    print(f"\nDescrição: {imovel.get('descricao', 'Sem descrição')}")
    print("*"*40)

def main():
    dados = carregar_dados()
    if not dados:
        return

    try:
        imoveis = dados["imobiliaria"]["imovel"]
      
        if not isinstance(imoveis, list):
            imoveis = [imoveis]
    except KeyError:
        print("Erro: A estrutura do JSON não é a esperada.")
        return

    while True:
        exibir_menu(imoveis)
        opcao = input("Digite o ID do imóvel ou 'sair': ").strip().lower()

        if opcao == 'sair':
            print("Programa encerrado.")
            break

        try:
            indice = int(opcao)
            if 0 <= indice < len(imoveis):
                exibir_detalhes(imoveis[indice])
            else:
                print(f"[!] Erro: Escolha um número entre 0 e {len(imoveis)-1}.")
        except ValueError:
            print("[!] Erro: Introduza um número válido.")

if __name__ == "__main__":
    main()