let regForm = document.getElementById("regform");

regForm.addEventListener("submit", (e) => {
  e.preventDefault();
  let nombre = document.getElementById("input_nombre");
  let correo = document.getElementById("input_correo");
  let pass1 = document.getElementById("input_pass1");
  let pass2 = document.getElementById("input_pass2");


  if (nombre.value == "" || correo.value == "" || pass1.value == "" || pass2.value == "") {
    alert("Existen campos vacios!");
  }
  else if (pass1.value.length < 6) {
    alert("La contraseña debe tener al menos 6 caracteres!");
  }
  else if (!/\d/.test(pass1.value)) {
    alert("La contraseña debe contener al menos un número!");
  }
  else if (!/[\W_]/.test(pass1.value)) {
    alert("La contraseña debe contener al menos un carácter especial!");
  }
  else if (!/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(correo.value)) {
    alert("El correo no es válido!");
  }
  else if
    (pass1.value !== pass2.value) {
    alert("Las contraseñas no coinciden!");
  }
  else {
    // perform operation with form input
    alert("Login Correcto");
    console.log(
      `nombre ${nombre.value}
       correo ${correo.value}
       pass1 ${pass1.value}`
    );

    nombre.value = "";
    correo.value = "";
  }
});

function alerta() {
  alert("Estamos trabajando para habilitar esta función");
}
