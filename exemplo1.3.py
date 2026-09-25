preco_bala = 10
total_float = preco_bala + 3 
print(total_float)
print(total_float == 0.30)

quantidade = 3
total_cents = preco_bala* quantidade
reais = total_cents // 100
centavos = total_cents % 100

print(f"total:(reais), (centavos:02d)")

print(f"Total: {total_float:02d}")