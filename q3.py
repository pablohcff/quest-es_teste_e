fat_diário = [22174.1664, 2457.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]

menor_fat = min(fat_diário)
maior_fat = max(fat_diário)

media_fat = sum(fat_diário) / len(fat_diário)

dia_acima = 0

for valor in fat_diário:
    if valor > media_fat:
        dia_acima += 1

print(f"Menor faturamento em um dia no mês: {menor_fat}")
print(f"Maior faturamento em um dia no mês: {maior_fat}")
print(f"Média faturamento no mês: {media_fat}")
print(f"A quantidade de dias que tiveram um valor maior que a média foram: {dia_acima}")