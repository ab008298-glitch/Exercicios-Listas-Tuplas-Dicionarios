
nome_arquivo = "banco-temperaturas-julho.txt"

total_linhas = 0
soma_temperaturas = 0.0
temperaturas = []
registros = []

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha:
            total_linhas += 1
            
            data_hora, temp_str = linha.split("\t")
            temperatura = float(temp_str)
            
            soma_temperaturas += temperatura
            temperaturas.append(temperatura)
            registros.append((data_hora, temperatura))

# 1. Quantas linhas ele possui no total?
print(f"Total de linhas: {total_linhas}")

# 2. Qual a média dos valores de temperatura exibidos?
media = soma_temperaturas / total_linhas
print(f"Média das temperaturas: {media:.2f}°C")

# 3. Qual é o valor mínimo e o valor máximo?
temp_min = min(temperaturas)
temp_max = max(temperaturas)
print(f"Temperatura mínima: {temp_min}°C")
print(f"Temperatura máxima: {temp_max}°C")

# 4. Considerando a temperatura mínima encontrada, qual foi o primeiro dia/horário em que ela foi registrada?
primeiro_registro_min = None
for data_hora, temperatura in registros:
    if temperatura == temp_min:
        primeiro_registro_min = data_hora
        break  

print(f"Primeiro registro da temperatura mínima ({temp_min}°C): {primeiro_registro_min}")