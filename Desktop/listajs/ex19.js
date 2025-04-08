function exercicio19() {
    let soma = 0;
    let numero;
   
    do {
        numero = Number(prompt("Digite um número (0 para sair):"));
        soma += numero;
    } while (numero !== 0);
   
    console.log("Soma total: " + soma);
}