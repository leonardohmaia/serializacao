import socket
import csv
import json
import xml.etree.ElementTree as ET
import yaml
import toml

# Dados do cliente
dados_cliente = [
    {"Nome": "Fulano", "CPF": "10326709722", "idade": "45", "mensagem": "segue comprovante de endereço"},

]

# Configurações do servidor
endereco_servidor = '127.0.0.1'
porta_servidor = 8888

for dados in dados_cliente:
    # Serialização CSV
    dados_csv = ','.join([f'{chave}: {valor}' for chave, valor in dados.items()])

    # Serialização JSON
    dados_json = json.dumps(dados)

    # Serialização XML
    xml_dados = ET.Element('cliente')
    for chave, valor in dados.items():
        ET.SubElement(xml_dados, chave).text = str(valor)
    xml_str = ET.tostring(xml_dados).decode('utf-8')

    # Serialização YAML
    dados_yaml = yaml.dump(dados)

    # Serialização TOML
    # Convertemos o dicionário do TOML em uma string simples
    
    	
    dados_toml = dados_toml = f"""
				    Nome = "{dados_cliente[0]['Nome']}"
				    CPF = "{dados_cliente[0]['CPF']}"
				    idade = {dados_cliente[0]['idade']}
				    mensagem = "{dados_cliente[0]['mensagem']}"
	"""
    dados_toml = toml.loads(dados_toml)
    print (dados_toml)

    # Enviar dados ao servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((endereco_servidor, porta_servidor))
        # Enviar cada formato de serialização separadamente com marcador
        s.sendall(f"CSV:{dados_csv}\nJSON:{dados_json}\nXML:{xml_str}\nYAML:{dados_yaml}\nTOML:{dados_toml}\n".encode())
