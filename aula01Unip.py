def criarAluno () :
    ra = input("Digite seu RA:")
    nome = input("Digite seu Nome:")
    curso = input("Digite seu curso: ")
    disciplina = input("Digite sua  disciplina")
    notaPrimeiraProva = float(input("Digite a nota da primeira prova "))
    notaSegundaProva = float(input("Digite a nota da segunda prova "))
    notaProvaSub = float(input("Digite a nota da  prova substitutiva "))
    notaExame = float(input("Digite a nota do exame "))
    print(f" Ola {nome} com o RA: {ra} , vc faz parte do curso {curso} estah prestando a disciplina {disciplina} . Sua nota na primeira prova eh {notaPrimeiraProva:.2f} e {notaSegundaProva:.2f}  na segunda prova  , no exame e substitutiva suas perspectivas notas sao {notaExame:.2f} {notaProvaSub:.2f} ")



criarAluno()
    