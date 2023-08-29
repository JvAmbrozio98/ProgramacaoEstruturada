#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

const char* names[] = {
    // Names array
};

typedef struct {
    char* nome;
    int idade;
    float altura;
    int peso;
} Pessoa;

int main() {
    srand(time(NULL));

    int quantidadeDePessoas;
    printf("Digite a quantidade de pessoas que vão ser verificadas: ");
    scanf("%d", &quantidadeDePessoas);

    int pessoaComMaisDe50 = 0, pessoaMenosDe40 = 0;
    float mediaDeAltura = 0;
    Pessoa pessoas[quantidadeDePessoas];

    for (int i = 0; i < quantidadeDePessoas; i++) {
        Pessoa pessoa;
        pessoa.nome = strdup(names[rand() % (sizeof(names) / sizeof(names[0]))]);
        pessoa.idade = rand() % 100 + 1;
        pessoa.altura = (float) (rand() % 101 + 120) / 100;
        pessoa.peso = rand() % 121 + 30;
        
        pessoas[i] = pessoa;
        
        printf("Nome: %s\n", pessoa.nome);
        printf("Idade: %d\n", pessoa.idade);
        printf("Altura: %.2f\n", pessoa.altura);
        printf("Peso: %d\n\n", pessoa.peso);

        if (pessoa.idade > 50) {
            pessoaComMaisDe50++;
        }
        if (pessoa.peso < 40) {
            pessoaMenosDe40++;
        } else if (pessoa.idade >= 10 && pessoa.idade <= 20) {
            mediaDeAltura += pessoa.altura;
        }
    }

    if (mediaDeAltura != 0) {
        mediaDeAltura /= quantidadeDePessoas;
    }

    
    printf("***************************************************************************\n");
    printf("A quantidade de pessoas com mais de 50 anos é: %d\n", pessoaComMaisDe50);
    printf("A média de altura para pessoas com idade entre 10 e 20: %.2f\n", mediaDeAltura);
    printf("A porcentagem das pessoas com peso inferior é: %.2f %%\n", (float) pessoaMenosDe40 / quantidadeDePessoas * 100);
    printf("***************************************************************************\n");

    return 0;
}
