function exercicio20() {
    let soma = 0;
    let contador = 0;
    let numero;
   
    do {
        numero = Number(prompt("Digite um número (valor negativo para sair):"));
        if (numero >= 0) {
            soma += numero;
            contador++;
        }
    } while (numero >= 0);
   
    let media = soma / contador;
    console.log("Média dos valores lidos: " + media);
}