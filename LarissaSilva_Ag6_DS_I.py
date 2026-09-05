def calcular_desconto():
    print("🛍️ Sistema de Desconto Progressivo - Loja Online 🛍️\n")
    
    try:
        # Solicitar o valor total da compra ao usuário
        valor_compra = float(input("Digite o valor total da compra (R$): "))
        
        # Validar para evitar valores negativos
        if valor_compra < 0:
            print("❌ Erro: O valor da compra não pode ser negativo.")
            return
            
    except ValueError:
        # Tratar erros caso o usuário digite letras ou caracteres inválidos
        print("❌ Erro: Por favor, digite apenas números válidos para o valor.")
        return

    # Estruturar para definir o percentual de desconto progressivo
    if valor_compra < 200.00:
        percentual_desconto = 0.05  # 5% de desconto para compras abaixo de R$ 200
    elif valor_compra < 300.00:
        percentual_desconto = 0.10  # 10% de desconto para compras de R$ 200 até R$ 299,99
    else:
        percentual_desconto = 0.15  # 15% de desconto para compras a partir de R$ 300

    # Realizar o cálculo do valor do desconto e do valor final a ser pago
    valor_desconto = valor_compra * percentual_desconto
    valor_final = valor_compra - valor_desconto

    # Exibir os resultados formatados de forma clara pro cliente
    print("\n--- 🧾 Resumo da Compra ---")
    print(f"Valor original: R$ {valor_compra:.2f}")
    print(f"Desconto aplicado: {int(percentual_desconto * 100)}% (R$ {valor_desconto:.2f})")
    print(f"Valor total a ser pago: R$ {valor_final:.2f}")
    print("----------------------------\n")

# Executar a função principal do programa
if __name__ == "__main__":
    calcular_desconto()