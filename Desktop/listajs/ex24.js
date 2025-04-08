function exercicio24() {
    let somaPares = 0;
    let somaImpares = 0;
   
    for (let i = 0; i < 10; i++) {
        let numero = Number(prompt("Digite um número:"));
       
        if (numero % 2 === 0) {
            somaPares += numero;
        } else {
            somaImpares += numero;
        }
    }
   
    console.log("Soma dos pares: " + somaPares);
    console.log("Soma dos ímpares: " + somaImpares);
}