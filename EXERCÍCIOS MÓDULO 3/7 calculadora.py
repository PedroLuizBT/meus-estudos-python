def calculadora():
	print("=== Calculadora ===")
	print("Operações: +, -, *, /")

	while True:
		try:
			primeiro_numero = float(input("Digite o primeiro número: "))
			operador = input("Digite a operação: ").strip()
			segundo_numero = float(input("Digite o segundo número: "))

			if operador == "+":
				resultado = primeiro_numero + segundo_numero
			elif operador == "-":
				resultado = primeiro_numero - segundo_numero
			elif operador == "*":
				resultado = primeiro_numero * segundo_numero
			elif operador == "/":
				if segundo_numero == 0:
					print("Erro: não é possível dividir por zero.")
					continue
				resultado = primeiro_numero / segundo_numero
			else:
				print("Operação inválida.")
				continue

			print(f"Resultado: {resultado:g}")
		except ValueError:
			print("Erro: digite números válidos.")

		continuar = input("Deseja fazer outro cálculo? (s/n): ").strip().lower()
		if continuar != "s":
			print("Até logo!")
			break


if __name__ == '__main__':
	calculadora()
