from behave import *
import requests
from bdd_context import BDD_Context

exception = []


@given('No hay proyecto llamado "{nombre_proyecto}"')
def delete_proyecto_if_exists(context, nombre_proyecto):
    response = requests.get('https://backend-proyectos-g13.herokuapp.com/proyectos/')
    for proyecto in response.json():
        if proyecto["nombre"] == nombre_proyecto:
            codigo = proyecto["codigo"]
            requests.post('https://backend-proyectos-g13.herokuapp.com/proyectos/delete', json={'codigo': codigo})
    BDD_Context.save_response_code(context, response)


@when('Se trata de crear un proyecto llamado "{nombre_proyecto}"')
def create_proyecto(context, nombre_proyecto):
    try:
        response = requests.post('https://backend-proyectos-g13.herokuapp.com/proyectos/create', json={
            'nombre': nombre_proyecto,
            "tipo": "Desarrollo",
            "estado": "Creado",
            "fecha_limite": '2022-09-02',
            "tareas": []})
        response.raise_for_status()
        BDD_Context.save_proyect_code(context, response.json())
        BDD_Context.save_response_code(context, response)
    except requests.exceptions.HTTPError as err:
        BDD_Context.save_response_message(context, err.response.json()["detail"])


@then('La solicitud sera exitosa')
def solicitud_exitosa(context):
    assert (context.response_code == 200)


@then('El sistema debera contener el proyecto "{nombre_proyecto}"')
def lista_contiene_proyecto(context, nombre_proyecto):
    proyecto_correcto = False
    ruta = 'https://backend-proyectos-g13.herokuapp.com/proyectos/' + str(context.proyect_code)
    response = requests.get(ruta)
    if response.json()["nombre"] == nombre_proyecto:
        proyecto_correcto = True
    assert proyecto_correcto


@given('Existe un proyecto llamado "{nombre_proyecto}"')
def create_proyecto_if_not_exists(context, nombre_proyecto):
    existe_proyecto = False
    response = requests.get('https://backend-proyectos-g13.herokuapp.com/proyectos/')
    for proyecto in response.json():
        if proyecto["nombre"] == nombre_proyecto:
            existe_proyecto = True
            BDD_Context.save_proyect_code(context, proyecto)
    if not existe_proyecto:
        create_proyecto(context, nombre_proyecto)


@then('La accion debera ser negada porque "{error_message}"')
def assert_error_message(context, error_message):
    assert (context.error_message == error_message)


@given('El estado del proyecto es "{estado}"')
def set_project_state(context, estado):
    ruta = 'https://backend-proyectos-g13.herokuapp.com/proyectos/' + str(context.proyect_code)
    response = requests.get(ruta)
    respuesta = response.json()
    respuesta["estado"] = estado
    respuesta.pop("tareas")
    requests.post('https://backend-proyectos-g13.herokuapp.com/proyectos/update', json=respuesta)


@when('Se trata de modificar el {campo} del proyecto a "{nuevo_campo}"')
def modify_project(context, campo, nuevo_campo):
    ruta = 'https://backend-proyectos-g13.herokuapp.com/proyectos/' + str(context.proyect_code)
    response = requests.get(ruta)
    respuesta = response.json()
    respuesta[campo] = nuevo_campo
    respuesta.pop("tareas")
    try:
        response = requests.post('https://backend-proyectos-g13.herokuapp.com/proyectos/update', json=respuesta)
        response.raise_for_status()
        BDD_Context.save_response_code(context, response)
    except requests.exceptions.HTTPError as err:
        BDD_Context.save_response_message(context, err.response.json()["detail"])


@then('El estado del proyecto sera "{estado}"')
def assert_state(context, estado):
    ruta = 'https://backend-proyectos-g13.herokuapp.com/proyectos/' + str(context.proyect_code)
    response = requests.get(ruta)
    assert (response.json()["estado"] == estado)


@when('Se trata de modificar el nombre del proyecto "{nombre_original}" a "{nombre_nuevo}"')
def modify_name(context, nombre_original, nombre_nuevo):
    ruta = 'https://backend-proyectos-g13.herokuapp.com/proyectos/' + str(context.proyect_code)
    response = requests.get(ruta)
    respuesta = response.json()
    respuesta["nombre"] = nombre_nuevo
    respuesta.pop("tareas")
    try:
        response = requests.post('https://backend-proyectos-g13.herokuapp.com/proyectos/update', json=respuesta)
        response.raise_for_status()
        BDD_Context.save_response_code(context, response)
    except requests.exceptions.HTTPError as err:
        BDD_Context.save_response_message(context, err.response.json()["detail"])


@when('Se trata de eliminar el proyecto "{nombre_proyecto}"')
def delete_proyecto(context, nombre_proyecto):
    response = requests.get('https://backend-proyectos-g13.herokuapp.com/proyectos/')
    for proyecto in response.json():
        if proyecto["nombre"] == nombre_proyecto:
            codigo = proyecto["codigo"]
            response = requests.post('https://backend-proyectos-g13.herokuapp.com/proyectos/delete', json={'codigo': codigo})
            BDD_Context.save_response_code(context, response)
            return


@then('La lista de proyectos no contiene "{nombre_proyecto}"')
def lista_no_contiene_proyecto(context, nombre_proyecto):
    contiene_proyecto = False
    response = requests.get('https://backend-proyectos-g13.herokuapp.com/proyectos/')
    for proyecto in response.json():
        if proyecto["nombre"] == nombre_proyecto:
            contiene_proyecto = True
    assert (not contiene_proyecto)
