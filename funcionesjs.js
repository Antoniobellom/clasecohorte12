function suma(a, b) {
  return a + b;
}

var resultado = suma(5, 3);

console.log("La suma de 5 y 3 es: " + resultado);

function mayor(edad) {
  if (edad > 18) {
    console.log("Eres mayor de edad");
  } else if (edad === 18) {
    console.log("Tienes exactamente 18 años");
  } else {
    console.log("No eres mayor de edad");
  }
}

let edad = 18;
mayor(edad);

let auto = {
    auto: 'marca'
}