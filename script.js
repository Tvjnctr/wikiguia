let loginForm = document.getElementById("formulario");

loginForm.addEventListener("submit", (e) => {
  e.preventDefault();
  let usuario = document.getElementById("input_usuario");
  let pass = document.getElementById("input_pass");

  if (usuario.value == "" || pass.value == "") {
    alert("Existen campos vacios!");
  } 
  else if (!/\d/.test(pass.value)) {
    alert("La contraseña debe contener al menos un número!");
  }
  else if ((usuario.value).length > 20 || (usuario.value).length < 3 ){
    alert("El nombre es incorrecto!");
  }
  else {
    // perform operation with form input
    alert("Login Correcto");
    console.log(
      `usuario ${usuario.value}
       pass ${pass.value}`
    );

    usuario.value = "";
    pass.value = "";
  }
});


function alerta() {
  alert("Estamos trabajando para habilitar esta función");
}
