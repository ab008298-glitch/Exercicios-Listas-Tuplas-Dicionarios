nome_arquivo = "banco-temperaturas-julho.txt"


data_usuario = input("Digite a data no formato aaaa-mm-dd (ex: 2016-07-01): ").strip()

temperaturas_do_dia = []

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha:
            data_hora, temp_str = linha.split("\t")
            data = data_hora.split(" ")[0]
            
            if data == data_usuario:
                temperaturas_do_dia.append(float(temp_str))


if len(temperaturas_do_dia) > 0:
    temp_min_dia = min(temperaturas_do_dia)
    temp_max_dia = max(temperaturas_do_dia)
    amplitude_termica = temp_max_dia - temp_min_dia
    
    print(f"--- Resultados para o dia {data_usuario} ---")
    print(f"Temperatura Mínima: {temp_min_dia}°C")
    print(f"Temperatura Máxima: {temp_max_dia}°C")
    print(f"Amplitude Térmica: {amplitude_termica:.2f}°C")
else:
    print(f"\nA data {data_usuario} não está presente no arquivo.")