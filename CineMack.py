# Sistema de Gestão do CineMack - Projeto 2

# Dados iniciais
filmes = {
    "Filme 1": {"preco_base": 20, "capacidade": 50, "sessoes": [{"vendas": {"inteira": 0, "meia": 0, "vip": 0}, "avaliacoes": []} for _ in range(2)]},
    "Filme 2": {"preco_base": 15, "capacidade": 40, "sessoes": [{"vendas": {"inteira": 0, "meia": 0, "vip": 0}, "avaliacoes": []} for _ in range(2)]},
    "Filme 3": {"preco_base": 10, "capacidade": 30, "sessoes": [{"vendas": {"inteira": 0, "meia": 0, "vip": 0}, "avaliacoes": []} for _ in range(2)]}
}

def calcular_preco(preco_base, tipo):
    """Calcula o preço do ingresso com base no tipo."""
    if tipo == "inteira":
        return preco_base
    elif tipo == "meia":
        return preco_base / 2
    elif tipo == "vip":
        return preco_base * 1.5

def mostrar_opcoes_sessoes():
    """Exibe as opções de sessões para compra de ingresso."""
    print("\nEscolha uma sessão:")
    opcoes = []
    contador = 1  # Inicia o contador para a numeração correta das opções
    for filme, info in filmes.items():
        for sessao_num, sessao in enumerate(info["sessoes"], start=1):
            opcoes.append((filme, sessao_num))
            print(f"{contador}. {filme} - Sessão {sessao_num}")
            contador += 1
    return opcoes

def comprar_ingresso():
    """Realiza a compra de ingressos para uma sessão específica."""
    opcoes = mostrar_opcoes_sessoes()
    escolha = int(input("Escolha a sessão (1-6): ")) - 1
    filme, sessao_num = opcoes[escolha]
    sessao = filmes[filme]["sessoes"][sessao_num - 1]

    capacidade = filmes[filme]["capacidade"]
    vendidos = sum(sessao["vendas"].values())
    disponiveis = capacidade - vendidos

    print(f"\nAssentos disponíveis para {filme} - Sessão {sessao_num}: {disponiveis}")
    if disponiveis > 0:
        tipo_ingresso = input("Escolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP): ")
        quantidade = int(input("Quantidade de ingressos: "))
        
        if quantidade > disponiveis:
            print("Quantidade excede assentos disponíveis. Tente novamente.")
            return
        
        tipos = {"1": "inteira", "2": "meia", "3": "vip"}
        tipo = tipos.get(tipo_ingresso)

        if tipo:
            preco = calcular_preco(filmes[filme]["preco_base"], tipo)
            sessao["vendas"][tipo] += quantidade
            print(f"Ingressos comprados com sucesso! Total: R${preco * quantidade:.2f}")
        else:
            print("Tipo de ingresso inválido.")
    else:
        print("Sessão lotada.")

def avaliar_filme():
    """Permite ao usuário avaliar um filme."""
    print("\nEscolha um filme para avaliar:")
    for idx, filme in enumerate(filmes.keys(), start=1):
        print(f"{idx}. {filme}")
    escolha = int(input("Escolha o filme (1-3): ")) - 1
    filme = list(filmes.keys())[escolha]
    
    avaliacao = int(input(f"Avalie o {filme} (1 a 5 estrelas): "))
    if 1 <= avaliacao <= 5:
        for sessao in filmes[filme]["sessoes"]:
            sessao["avaliacoes"].append(avaliacao)
        print("Avaliação registrada!")
    else:
        print("Avaliação inválida. Tente novamente.")

def gerar_relatorio():
    """Gera e exibe o relatório final do dia."""
    total_ingressos = 0
    receita_total = 0
    print("\n--- Relatório do Dia ---")
    
    for filme, info in filmes.items():
        preco_base = info["preco_base"]
        for idx, sessao in enumerate(info["sessoes"], start=1):
            print(f"\n{filme} - Sessão {idx}:")
            total_sessao = 0
            for tipo, qtd in sessao["vendas"].items():
                preco = calcular_preco(preco_base, tipo)
                receita = qtd * preco
                total_sessao += receita
                print(f"  {tipo.capitalize()}: {qtd} ingressos - R${receita:.2f}")
            receita_total += total_sessao
            total_ingressos += sum(sessao["vendas"].values())

            # Média de avaliações
            if sessao["avaliacoes"]:
                media_avaliacoes = sum(sessao["avaliacoes"]) / len(sessao["avaliacoes"])
                print(f"  Média de avaliações: {media_avaliacoes:.2f}")
            else:
                print("  Média de avaliações: N/A")
    
    print(f"\nTotal de ingressos vendidos: {total_ingressos}")
    print(f"Receita total do dia: R${receita_total:.2f}")

def main():
    """Programa principal que gerencia o sistema."""
    while True:
        print("\n--- Sistema de Gestão do CineMack ---")
        print("1. Comprar ingresso")
        print("2. Avaliar um filme")
        print("3. Encerrar o dia e exibir relatório")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            comprar_ingresso()
        elif opcao == '2':
            avaliar_filme()
        elif opcao == '3':
            gerar_relatorio()
        elif opcao == '4':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
main()