import json
from datetime import date

STOCK_FILE = "stock.json"
MOEDAS_VALIDAS = {"1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}

def carregar_stock():
    try:
        with open(STOCK_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_stock(stock):
    with open(STOCK_FILE, "w") as f:
        json.dump(stock, f, indent=4)

def listar_produtos(stock):
    print("cod | nome | quantidade | preço")
    print("-" * 40)
    for produto in stock:
        print(f"{produto['cod']} {produto['nome']} {produto['quant']} {produto['preco']}e")

def inserir_moedas(moedas, saldo):
    for moeda in moedas:
        if moeda in MOEDAS_VALIDAS:
            saldo += MOEDAS_VALIDAS[moeda]
        else:
            print(f"Moeda inválida: {moeda}")
    return saldo

def selecionar_produto(stock, codigo, saldo):
    for produto in stock:
        if produto["cod"] == codigo:
            if produto["quant"] > 0:
                if saldo >= int(produto["preco"] * 100):
                    produto["quant"] -= 1
                    saldo -= int(produto["preco"] * 100)
                    print(f"Pode retirar o produto dispensado \"{produto['nome']}\"")
                else:
                    print(f"Saldo insuficiente para satisfazer o seu pedido")
                    print(f"Saldo = {saldo}c; Pedido = {int(produto['preco'] * 100)}c")
            else:
                print("Produto esgotado!")
            return saldo
    print("Código de produto inválido!")
    return saldo

def calcular_troco(saldo):
    troco = {}
    for moeda, valor in sorted(MOEDAS_VALIDAS.items(), key=lambda x: -x[1]):
        qtd = saldo // valor
        if qtd > 0:
            troco[moeda] = qtd
            saldo -= qtd * valor
    return troco

def main():
    stock = carregar_stock()
    print(f"maq: {date.today()}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    saldo = 0
    
    while True:
        entrada = input(">> ").strip().split()
        comando = entrada[0].upper()

        if comando == "LISTAR":
            listar_produtos(stock)
        elif comando == "MOEDA":
            saldo = inserir_moedas(entrada[1:], saldo)
            print(f"maq: Saldo = {saldo}c")
        elif comando == "SELECIONAR":
            saldo = selecionar_produto(stock, entrada[1], saldo)
            print(f"maq: Saldo = {saldo}c")
        elif comando == "SAIR":
            troco = calcular_troco(saldo)
            troco_str = ", ".join([f"{v}x {k}" for k, v in troco.items()])
            print(f"maq: Pode retirar o troco: {troco_str}.")
            print("maq: Até à próxima")
            break
        elif comando == "ADICIONAR":
            cod, nome, quant, preco = entrada[1], " ".join(entrada[2:-2]), int(entrada[-2]), float(entrada[-1])
            for produto in stock:
                if produto["cod"] == cod:
                    produto["quant"] += quant
                    print("Produto atualizado com sucesso!")
                    break
            else:
                stock.append({"cod": cod, "nome": nome, "quant": quant, "preco": preco})
                print("Produto adicionado com sucesso!")
        else:
            print("Comando inválido!")
    
    guardar_stock(stock)

if __name__ == "__main__":
    main()
