function exercicio12() {
    let nota = Number(prompt("Digite a nota:"));
   
    if (nota < 5) {
        console.log("Reprovado");
    } else if (nota >= 5 && nota < 7) {
        console.log("Recuperação");
    } else {
        console.log("Aprovado");
    }
}