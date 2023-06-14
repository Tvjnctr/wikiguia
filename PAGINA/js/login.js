let loginForm = document.getElementById("formulario");

loginForm.addEventListener("submit", (e) => {
  e.preventDefault();
  let usuario = document.getElementById("input_usuario");
  let pass = document.getElementById("input_pass");

  if (usuario.value == "" || pass.value == "") {
    alert("Existen campos vacios!");
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
