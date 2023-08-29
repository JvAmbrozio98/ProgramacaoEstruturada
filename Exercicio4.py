import random
import json
import time
import datetime

start_time = time.time()
names = [
    "Helena", "Alice", "Laura", "Maria Alice", "Sophia", "Manuela", "Maitê", "Liz", "Cecília", "Isabella", 
    "Luísa", "Eloá", "Heloísa", "Júlia", "Ayla", "Maria Luísa", "Isis", "Elisa", "Antonella", "Valentina", 
    "Maya", "Maria Júlia", "Aurora", "Lara", "Maria Clara", "Lívia", "Esther", "Giovanna", "Sarah", 
    "Maria Cecília", "Lorena", "Beatriz", "Rebecca", "Luna", "Olívia", "Maria Helena", "Mariana", "Isadora", 
    "Melissa", "Maria", "Catarina", "Lavínia", "Alícia", "Maria Eduarda", "Agatha", "Ana Liz", "Yasmin", 
    "Emanuelly", "Ana Clara", "Clara", "Ana Júlia", "Marina", "Stella", "Jade", "Maria Liz", "Ana Laura", 
    "Maria Isis", "Ana Luísa", "Gabriela", "Alana", "Rafaela", "Vitória", "Isabelly", "Bella", "Milena", 
    "Clarice", "Mirella", "Ana", "Emilly", "Betina", "Mariah", "Zoe", "Maria Vitória", "Nicole", "Laís", 
    "Melina", "Bianca", "Louise", "Ana Beatriz", "Heloíse", "Malu", "Melinda", "Letícia", "Maria Valentina", 
    "Chloe", "Maria Elisa", "Maria Heloísa", "Maria Laura", "Maria Fernanda", "Ana Cecília", "Hadassa", 
    "Ana Vitória", "Diana", "Ayla Sophia", "Eduarda", "Ana Lívia", "Isabel", "Elis", "Pérola", "Joana",
    # Masculine names
    "Lucas", "Miguel", "Arthur", "Davi", "Gabriel", "Pedro", "Bernardo", "Matheus", "Heitor", "Cauã", 
    "Enzo", "Lorenzo", "Gustavo", "Felipe", "Samuel", "Benjamin", "Rafael", "João", "Daniel", "Vitor", 
    "Eduardo", "Noah", "Leonardo", "Henrique", "Theo", "Isaac", "Murilo", "Caio", "Lucca", "Vinícius", 
    "Pedro Henrique", "João Pedro", "Bryan", "Davi Lucca", "Pietro", "Francisco", "Caleb", "Antônio", 
    "Enzo Gabriel", "Davi Lucas", "Bruno", "Yuri", "Emanuel", "Ian", "Tomás", "Nathan", "Ryan", "Luiz Felipe", 
    "Igor", "Ruan", "Otávio", "Luan", "Kaique", "Breno", "Davi Luiz", "Augusto", "Nicolas", "Guilherme", 
    "Daniel", "Carlos", "Calebe", "Vicente", "Fernando", "Marcelo", "Thiago", "João Lucas", "Raul", 
    "Felipe", "Fábio", "André", "Erick", "Paulo", "Giovanni", "Roberto", "Renan", "José", "Arthur Gabriel"]



quantidadeDePessoas = int(input("Digite a quantidade de pessoas que vão ser verificadas "))
pessoaComMaisDe50,pessoaMenosDe40 = 0,0
mediaDeAltura, pessoas = [], []

for i in range(quantidadeDePessoas):
    pessoa = {
    "nome" : names[random.randint(0,len(names) - 1)],
    "idade" : random.randint(1,100),
    "altura" : round(random.uniform(1.20,2.20 ),2) ,
    "peso" : random.randint(30,150 )
    }
    pessoas.append(pessoa)
    print(pessoa)
    
    if (pessoas [i]["idade"] > 50):
        pessoaComMaisDe50 += 1
    if (pessoas [i]["peso"] < 40):
        pessoaMenosDe40 += 1
    elif(pessoas[i]["idade"] >= 10 and pessoas[i]["idade"] <= 20  ) :
        mediaDeAltura.append(pessoas[i]["altura"])
with open('pessoas.json', 'w') as json_file:
    json.dump(pessoas, json_file, indent=4)


mediaDeAltura = sum(mediaDeAltura) / len(mediaDeAltura) if len(mediaDeAltura) != 0 else 0


print("***************************************************************************")
print(f'A quanditade de pessoas com mais de 50 anos é : {pessoaComMaisDe50}')
print(f'A média de altura para pessoas com idade entre 10  e 20: {mediaDeAltura:.2f}')
print(f'A porcentagems das pessoas com peso inferior é  : {round(((pessoaMenosDe40 / quantidadeDePessoas) *100),2) } %')
print("***************************************************************************")
end_time = time.time()
runtime = start_time - end_time
runtime_delta = datetime.timedelta(seconds=runtime)
print(runtime_delta)

