Feature: Gestion de Tarea

  #Escenarios relacionados con la creacion de tareas
  Scenario: Crear tarea exitosamente
    Given Existe un proyecto llamado "Proyecto PSA"
    When Se trata de crear una tarea llamada "Nueva Tarea"
    Then La solicitud sera exitosa
    And La lista de tareas debera contener "Nueva Tarea"

  Scenario: No se puede crear una tarea de un proyecto que no existe
    Given Un proyecto que no existe
    When Se trata de crear una tarea asociada al proyecto
    Then La accion debera ser negada porque "El proyecto no existe"

  #Escenarios relacionados con la modificacion de tareas
  Scenario: Modificar campos de la tarea exitosamente
    Given Existe un proyecto llamado "Proyecto PSA"
    And Existe una tarea llamada "Nueva Tarea" asociada al proyecto
    And El estado de la tarea es "Creada"
    When Se trata de modificar el estado de la tarea a "En desarrollo"
    Then La solicitud sera exitosa
    And El estado de la tarea sera "En desarrollo"

  Scenario: No se puede modificar campos de una tarea que no existe
    Given Existe un proyecto llamado "Proyecto PSA"
    And Una tarea que no existe
    When Se trata de modificar el estado de la tarea que no existe a "En desarrollo"
    Then La accion debera ser negada porque "La tarea no existe"


  #Escenarios relacionados con la eliminacion de tareas
  Scenario: Eliminar tarea exitosamente
    Given Existe un proyecto llamado "Proyecto PSA"
    And Existe una tarea llamada "Nueva Tarea" asociada al proyecto
    When Se trata de eliminar la tarea
    Then La lista de tareas no contiene la tarea
