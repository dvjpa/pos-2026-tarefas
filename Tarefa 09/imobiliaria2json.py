import xml.dom.minidom
import json
import os

def xml_para_dict(node):
    """
    Função recursiva que converte nós do XML em dicionários Python.
    """
    if node.nodeType == node.TEXT_NODE:
        return node.data.strip()

    filhos_elementos = [n for n in node.childNodes if n.nodeType == n.ELEMENT_NODE]
    if not filhos_elementos:
        return "".join([n.data for n in node.childNodes if n.nodeType == n.TEXT_NODE]).strip()

    res = {}
    for filho in filhos_elementos:
        valor = xml_para_dict(filho)
        tag = filho.tagName

        if tag in res:
            if not isinstance(res[tag], list):
                res[tag] = [res[tag]]
            res[tag].append(valor)
        else:
            res[tag] = valor
    return res

def converter():
    arquivo_xml = "Tarefa 05/imobiliaria.xml"
    arquivo_json = "imobiliaria.json"

    if not os.path.exists(arquivo_xml):
        print(f"Erro: O ficheiro '{arquivo_xml}' não foi encontrado.")
        return

    try:
        dom = xml.dom.minidom.parse(arquivo_xml)
        root = dom.documentElement
        
        dados_dict = {root.tagName: xml_para_dict(root)}

        with open(arquivo_json, "w", encoding="utf-8") as f:
            json.dump(dados_dict, f, indent=4, ensure_ascii=False)
        
        print(f"Sucesso! O ficheiro '{arquivo_json}' foi criado com êxito.")

    except Exception as e:
        print(f"Ocorreu um erro na conversão: {e}")

if __name__ == "__main__":
    converter()