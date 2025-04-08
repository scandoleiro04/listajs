function exercicio14() {
    let peso = Number(prompt("Digite seu peso (kg):"));
    let altura = Number(prompt("Digite sua altura (m):"));
   
    let imc = peso / (altura * altura);
    let classificacao;
   
    if (imc < 18.5) {
        classificacao = "Abaixo do peso";
    } else if (imc >= 18.5 && imc <= 24.9) {
        classificacao = "Peso normal";
    } else if (imc >= 25.0 && imc <= 29.9) {
        classificacao = "Sobrepeso";
    } else if (imc >= 30.0 && imc <= 34.9) {
        classificacao = "Obesidade grau I";
    } else if (imc >= 35.0 && imc <= 39.9) {
        classificacao = "Obesidade grau II (severa)";
    } else {
        classificacao = "Obesidade grau III (mórbida)";
    }
   
    console.log("IMC: " + imc.toFixed(2));
    console.log("Classificação: " + classificacao);
}
