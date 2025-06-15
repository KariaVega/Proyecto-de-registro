<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario Básico de Registro</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>

<div class="formulario-registro">
    <h2>Registro de Estudiante</h2>
    <form id="registroForm">
        <label for="nombre">Nombre Completo:</label>
        <input type="text" id="nombre" name="nombre" required>

        <label for="email">Correo Electrónico:</label>
        <input type="email" id="email" name="email" required>

        <label for="telefono">Teléfono:</label>
        <input type="tel" id="telefono" name="telefono" required>

        <label for="fechaNacimiento">Fecha de Nacimiento:</label>
        <input type="date" id="fechaNacimiento" name="fechaNacimiento" required>

        <label for="grado">Grado de Ingreso:</label>
        <select id="grado" name="grado" required>
            <option value="">Seleccione el grado</option>
            <option value="primero">Primero</option>
            <option value="segundo">Segundo</option>
            <option value="tercero">Tercero</option>
            <option value="cuarto">Cuarto</option>
            <option value="quinto">Quinto</option>
        </select>

        <button type="submit">Registrar</button>
    </form>
</div>

</body>
</html>
def test_create_user_number_type_first_name_get_error_response():
    user_body = test_functions.get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    print(response.status_code)
