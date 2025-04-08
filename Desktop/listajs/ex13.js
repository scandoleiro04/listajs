function exercicio13() {
    let dia = Number(prompt("Digite um número de 1 a 7:"));
    let nomeDia;
   
    switch (dia) {
        case 1:
            nomeDia = "Domingo";
            break;
        case 2:
            nomeDia = "Segunda-feira";
            break;
        case 3:
            nomeDia = "Terça-feira";
            break;
        case 4:
            nomeDia = "Quarta-feira";
            break;
        case 5:
            nomeDia = "Quinta-feira";
            break;
        case 6:
            nomeDia = "Sexta-feira";
            break;
        case 7:
            nomeDia = "Sábado";
            break;
        default:
            nomeDia = "Dia inválido.";
    }
   
    console.log(nomeDia);
}