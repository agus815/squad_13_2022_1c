# Squad 13
Este es el repositorio del Squad 13 de la materia Análisis de la Información de FIUBA. Corresponde al primer cuatrimestre de 2022.

## Integrantes
- Lucía Lourengo Caridade, padrón 104880
- Agustina Doly Su, padrón 105708
- Enrique Morici, padrón 107115

## Objetivo
El objetivo del proyecto consiste en implementar una versión MVP del nuevo software para manejar la gestión de la empresa PSA.

# Módulo de proyectos
**IMPORTANTE:** La versión más actualizada de la aplicación estará siempre en el branch ```develop```.

## Objetivo del módulo
La finalidad de este módulo es poder gestionar los proyectos y tareas del cliente. Por *"gestionar"* se entiende realizar altas, bajas y modificiaciones de todos los proyectos y tareas.

## Dependencias

Las dependencias del módulo se deviden en dos categorías según su finalidad **dentro de este módulo**:

### Funcionamiento de la API
- FastAPI - Framework utilizado para el desarrollo.
- Pydantic - Librería para validación de datos.
- SQLAlchemy - Conexión con la Base de Datos.
- Asyncio - Este proyecto únicamente lo utiliza para obtener mayor detalle en las excepciones / errores que se muestran en la consola (La librería tiene muchas más utilidades que no son explotadas en el módulo).
- Typing - Soporte para tipos de datos no convencionales.

### Testing
- Behave - Framework utilizado para las pruebas.
- Requests - Peticiones a la API en producción.

## Estructura del proyecto
```
.
├── app
│   ├── cruds
│   │   └─── crud_proyectos.py
│   │   └─── crud_tareas.py
│   ├── models
│   │   └─── models_proyectos.py
│   │   └─── models_tareas.py
│   ├── routes
│   │   └─── proyecto_routes.py
│   │   └─── tarea_routes.py
│   ├── schemas
│   │   └─── schemas_proyectos.py
│   │   └─── schemas_tareas.py
│   ├── config.py
│   ├── database.py
│   └── main.py
├── features
│   ├── steps
│   │   └─── bdd_context.py
│   │   └─── steps.py
│   ├── proyectos.feature
│   └── tareas.feature
├── .env
├── Dockerfile
├── heroku.yml
└── requirements.txt
```

## Deploy
En la estructura del proyecto, se encuentran los archivos para hacer el deploy del proyecto creando un container de Docker donde funcionará la API.

*El deploy de este módulo está hecho en [Heroku](https://www.heroku.com/platform), con lo cual se debe contemplar un paso adicional que es configurar el servicio de hosting para que se pueda realizar el deploy del container.*

[Desde aquí](http://backend-proyectos-g13.herokuapp.com/proyectos/) se puede acceder al endpoint de la API. La ruta por default es ```/proyectos```, donde se listan todos los proyectos registrados.

## Documentación
[FastAPI](https://fastapi.tiangolo.com/) provee de un Swagger con toda la documentación necesaria para entender el funcionamiento de la API (Routes, Schemas, Response Models, Request Bodys, entre otros). El mismo es accesible colocando ```/docs``` al final de la ruta de la API. Por comidad, se puede acceder al mismo desde [Este enlace](https://backend-proyectos-g13.herokuapp.com/docs)

## Referencias de herramientas utilizadas

### API
- [FastAPI](https://fastapi.tiangolo.com/).
- [Pydantic](https://pydantic-docs.helpmanual.io/).
- [SQLAlchemy](https://www.sqlalchemy.org/).

### Base de Datos
- [PostgreSQL](https://www.postgresql.org/).
- [ElephantSQL](https://www.elephantsql.com/) - *Hosting*.
- [DBeaver](https://dbeaver.io/) - *Gestor recomendado*.

### Testing
- [Beheave](https://behave.readthedocs.io/en/stable/).

### Deploy
- [Heroku](https://www.heroku.com/platform).
- [Docker](https://www.docker.com/).

