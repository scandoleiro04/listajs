function exercicio7() {
    let numero1 = Number(prompt("Digite o primeiro número:"));
    let numero2 = Number(prompt("Digite o segundo número:"));
   
    if (numero1 > numero2) {
        console.log("O primeiro número é maior.");
    } else if (numero1 < numero2) {
        console.log("O segundo número é maior.");
    } else {
        console.log("Os números são iguais.");
    }
}