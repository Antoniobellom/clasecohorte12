function operacion(func, a, b) {
    return func(a, b);
}

function multiplicar(x, y) {
    return x * y;
}

let resultado = operacion(multiplicar, 5, 3);
console.log(resultado);  // Output: 15

funciones anonimas

let sumar = (a, b) => a + b;
let resultado = sumar(5, 3);
console.log(resultado);  // Output: 8

funciones

function sumar(a, b) {
    return a + b;
}

let resultado = sumar(5, 3);
console.log(resultado);  // Output: 8

function nombreDeLaFuncion(parametros) {
    // Cuerpo de la función
    return valor;
}