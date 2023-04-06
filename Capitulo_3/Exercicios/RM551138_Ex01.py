tipo_assinatura = input("Digite o tipo de assinatura do cliente (Basic, Silver, Gold ou Platinum): ")
faturamento_anual = float(input("Digite o faturamento anual do cliente: "))

if tipo_assinatura.upper() == "BASIC":
    bonus = faturamento_anual * 0.3
elif tipo_assinatura.upper() == "SILVER":
    bonus = faturamento_anual * 0.2
elif tipo_assinatura.upper() == "GOLD":
    bonus = faturamento_anual * 0.1
elif tipo_assinatura.upper() == "PLATINUM":
    bonus = faturamento_anual * 0.05
else:
    print("Tipo de assinatura inválido.")
    bonus = 0

print("O valor do bônus que o cliente deve pagar é de R$", bonus)
