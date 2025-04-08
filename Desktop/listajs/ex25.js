function exercicio25() {
    let n = Number(prompt("Digite o número de termos da série Fibonacci:"));
    let fib1 = 0, fib2 = 1;
   
    console.log(fib1);
    console.log(fib2);
   
    for (let i = 3; i <= n; i++) {
        let fib = fib1 + fib2;
        console.log(fib);
        fib1 = fib2;
        fib2 = fib;
    }
}
