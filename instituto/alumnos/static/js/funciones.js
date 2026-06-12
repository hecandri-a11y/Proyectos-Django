
$(document).ready(function () {

    $("#formulario").submit(function (event) {

        event.preventDefault();

        let nombre = $("#nombre").val().trim();
        let apellido = $("#apellido").val().trim();
        let edad = $("#edad").val();
        let password = $("#password").val();
        let correo = $("#email").val().trim();
        let telefono = $("#telefono").val().trim();
        let ciudad = $("#ciudad").val();
        let genero = $("input[name='genero']:checked").val();
        let intereses = $("input[name='interes']:checked").length;
        let crimen = $("input[name='crimen']:checked").val();
        let fecha = $("#fecha").val();
        let mensaje = $("#mensaje").val().trim();

        let valido = true;

        // LIMPIAR MENSAJES
        $("#mensaje2").text("");
        $("#mensaje3").text("");
        $("#mensaje4").text("");
        $("#mensaje5").text("");
        $("#mensaje6").text("");
        $("#mensaje7").text("");
        $("#mensaje8").text("");
        $("#mensaje9").text("");
        $("#mensaje10").text("");
        $("#mensaje11").text("");
        $("#mensaje12").text("");
        $("#mensaje13").text("");
        $("#mensaje14").text("");

        // VALIDAR NOMBRE
        if (nombre == "") {
            $("#mensaje2").text("El nombre es obligatorio");
            valido = false;
        }

        // VALIDAR APELLIDO
        if (apellido == "") {
            $("#mensaje3").text("El apellido es obligatorio");
            valido = false;
        }

        // VALIDAR EDAD
        if (edad == "" || edad < 10 || edad > 100) {
            $("#mensaje4").text("Ingrese una edad válida");
            valido = false;
        }

        // VALIDAR CONTRASEÑA
        if (password.length < 6) {
            $("#mensaje5").text("La contraseña debe tener mínimo 6 caracteres");
            valido = false;
        }

        // VALIDAR CORREO
        if (correo == "" || !correo.includes("@")) {
            $("#mensaje6").text("Ingrese un correo válido");
            valido = false;
        }

        // VALIDAR TELÉFONO
        if (telefono == "" || telefono.length < 8) {
            $("#mensaje7").text("Ingrese un teléfono válido");
            valido = false;
        }

        // VALIDAR CIUDAD
        if (ciudad == "") {
            $("#mensaje8").text("Seleccione una ciudad");
            valido = false;
        }

        // VALIDAR GÉNERO
        if (!genero) {
            $("#mensaje9").text("Seleccione un género");
            valido = false;
        }

        // VALIDAR INTERESES
        if (intereses == 0) {
            $("#mensaje10").text("Seleccione al menos un interés");
            valido = false;
        }

        // VALIDAR CRIMEN
        if (!crimen) {
            $("#mensaje11").text("Seleccione una opción");
            valido = false;
        }

        // VALIDAR FECHA
        if (fecha == "") {
            $("#mensaje12").text("Seleccione una fecha");
            valido = false;
        }

        // VALIDAR MENSAJE
        if (mensaje == "") {
            $("#mensaje13").text("Ingrese un mensaje");
            valido = false;
        }

        // FORMULARIO CORRECTO
        if (valido) {
            $("#mensaje14").text("Formulario enviado correctamente");
        }

    });

});