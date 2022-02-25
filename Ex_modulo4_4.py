
valor_compra = float(input('Digite o valor de compra: \n'))
valor_frete = float(input('Digite o valor do frete: \n'))
fidelização = input('Possouí cartão fidelidade? ("s" sim, "n" não): \n')

valor_total = valor_compra + valor_frete

usar_cupom = valor_total > 100 or fidelização == 's'

print('O cupom de desconto é aplicado?', usar_cupom)
