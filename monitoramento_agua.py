"""
Sistema de Monitoramento do Reservatório de Água
Desenvolvimento de Sistemas I - Agenda 11
Estudante: Pedro Paulo Leão Fernandes Dos Santos
"""

from colorama import Fore, Style, init

# Inicializa o colorama (garante compatibilidade no Windows/Linux/macOS)
init(autoreset=True)


def obter_configuracao_nivel(nivel):
    """
    Retorna a cor e a mensagem correspondentes ao nível de água informado.
    """
    configuracoes = {
        1: (Fore.RED, "Muito baixo (crítico)"),
        2: (Fore.YELLOW, "Baixo"),
        3: (Fore.GREEN, "Médio"),
        4: (Fore.CYAN, "Alto"),
        5: (Fore.BLUE, "Muito alto (alerta)"),
    }

    # Retorna a cor e a situação ou um valor padrão caso o nível não exista
    return configuracoes.get(nivel, (Fore.WHITE, "Nível desconhecido"))


def simular_monitoramento():
    """
    Simula a leitura dos níveis do reservatório armazenados em uma lista
    e exibe os alertas coloridos no terminal.
    """
    # Lista armazenando os 5 níveis de água do reservatório
    niveis_reservatorio = [1, 2, 3, 4, 5]

    print("=" * 55)
    print("  PAINEL DE MONITORAMENTO DO RESERVATÓRIO DE ÁGUA")
    print("=" * 55 + "\n")

    for nivel in niveis_reservatorio:
        cor, situacao = obter_configuracao_nivel(nivel)

        # Exibe no terminal com a cor correspondente
        print(f"Nível {nivel}: {cor}{situacao}{Style.RESET_ALL}")

    print("\n" + "=" * 55)
    print("  SIMULAÇÃO CONCLUÍDA - ESTILO DO TERMINAL RESTAURADO")
    print("=" * 55)


if __name__ == "__main__":
    simular_monitoramento()