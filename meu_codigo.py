tempo = int(input("quanto tempo voce trabalha na academia?"))
salario = float(input("qual o seu salario?"))
if tempo >= 10:
    print("voce tem direito a um aumento de 10%")
    print(f"seu salario atual é de R${salario * 1.10:.2f}")
elif tempo >= 5 and tempo < 10:
    print("voce tem direito a um aumento de 5%")
    print(f"seu salario atual é de R${salario * 1.05:.2f}")
else:
    print("voce nao tem direito a um aumento")
print("===== FICHA DO TREINADOR =====")
nome = input("qual o seu nome?")
idade = int(input("qual sua idade"))
peso = float(input("quanto voce pesa?"))
print("===== RESULTADO DO TREINADOR =====")
print(f"nome: {nome}")
print(f"idade: {idade} anos")
if idade < 18:
    print("voce é menor de idade")
elif idade > 18:
    print("voce é maior de idade")
else:
    print("voce tem exatamente 18 anos")
print(f"peso: {peso} kg")
print("===== OBRIGADO PELA COMPREENSAO =====")