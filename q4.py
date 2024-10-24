sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

valor_total = (sp + rj + mg + es + outros)

porcent_sp = (sp / valor_total) * 100
porcent_rj = (rj / valor_total) * 100
porcent_mg = (mg / valor_total) * 100
porcent_es = (es / valor_total) * 100
porcent_outros = (outros / valor_total) * 100

print(f'A porcentagem de SP foi: {porcent_sp:.2f}%')
print(f'A porcentagem de RJ foi: {porcent_rj:.2f}%')
print(f'A porcentagem de MG foi: {porcent_mg:.2f}%')
print(f'A porcentagem de ES foi: {porcent_es:.2f}%')
print(f'A porcentagem de Outros foi: {porcent_outros:.2f}%')