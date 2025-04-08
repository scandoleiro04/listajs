function exercicio10() {
    let numero1 = Number(prompt("Digite o primeiro número:"));
    let numero2 = Number(prompt("Digite o segundo número:"));
    let operacao = prompt("Digite a operação (+, -, *, /):");
   
    let resultado;
    switch(operacao) {
        case "+":
            resultado = numero1 + numero2;
            break;
        case "-":
            resultado = numero1 - numero2;
            break;
        case "*":
            resultado = numero1 * numero2;
            break;
        case "/":
            resultado = numero1 / numero2;
            break;
        default:
            console.log("Operação inválida.");
            return;
    }
    console.log("Resultado: " + resultado);
}