# Módulo de proyectos
API en desarrollo. La versión más actualizada estará en el branch `develop`

# Requisitos

Los requisitos están especificados en el archivo `requeriments.txt`. Para instalarlos se requiere ejecutar el comando
```cmd
pip install -r requeriments.txt
```

# Levantar la API
Para levantar la API se debe entrar a la carpeta del proyecto y ejecutar el siguiente comando

```
uvicorn app.main:app --reload
```

# Correr los tests
Para correr los tests se debe entrar a la carpeta del proyecto y ejecutar el siguiente comando
```
behave
```
