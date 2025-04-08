function exercicio16() {
    let idade = Number(prompt("Digite sua idade:"));
    let classificacao;
   
    switch(true) {
        case (idade <= 12):
            classificacao = "Criança";
            break;
        case (idade >= 13 && idade <= 17):
            classificacao = "Adolescente";
            break;
        case (idade >= 18 && idade <= 59):
            classificacao = "Adulto";
            break;
        case (idade >= 60):
            classificacao = "Idoso";
            break;
        default:
            classificacao = "Idade inválida.";
    }
   
    console.log("Classificação: " + classificacao);
}