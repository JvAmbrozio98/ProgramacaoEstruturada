cpf = input("Digite seu cpf")
celular = input("Digite seu celular")
cep = input("Digite seu cep")

cpf_formatado = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]
celular_formatado =  "+55 "  +  "(" + celular[:2] + ") "  + celular[2:7] + "-" + celular[7:]
cep_formatado = cep[:5] + "-" + cep[5:]

print(cpf_formatado,celular_formatado,cep_formatado)