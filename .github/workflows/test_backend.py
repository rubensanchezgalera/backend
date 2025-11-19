import requests

# URL del backend en local (para pruebas en CI/CD se usará localhost:
BASE_URL = "http://localhost:8000"

def test_students_endpoint_status():
    """Comprueba que el endpoint /students responde con 200."""
    response = requests.get(f"{BASE_URL}/students")
    assert response.status_code == 200, "El endpoint /students no responde correctamente."


def test_students_endpoint_returns_list():
    """Comprueba que la respuesta del endpoint es una lista."""
    response = requests.get(f"{BASE_URL}/students")
    data = response.json()
    assert isinstance(data, list), "El endpoint /students debe devolver una lista."


def test_student_fields_exist():
    """Comprueba que cada estudiante tiene los campos obligatorios."""
    response = requests.get(f"{BASE_URL}/students")
    students = response.json()

    required_fields = {
        "id",
        "nombre",
        "apellido1",
        "apellido2",
        "email",
        "telefono",
        "fecha_nacimiento"
    }

    for student in students:
        missing = required_fields - student.keys()
        assert not missing, f"Faltan campos en un estudiante: {missing}"
