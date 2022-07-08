Feature: Gestion de Proyecto

  #Escenarios relacionados con la creacion de proyectos
  Scenario: Crear proyecto exitosamente
    Given No hay proyecto llamado "Proyecto PSA"
    When Se trata de crear un proyecto llamado "Proyecto PSA"
    Then La solicitud sera exitosa
    And El sistema debera contener el proyecto "Proyecto PSA"

  Scenario: No se puede crear un proyecto que ya existe
    Given Existe un proyecto llamado "Proyecto PSA"
    When Se trata de crear un proyecto llamado "Proyecto PSA"
    Then La accion debera ser negada porque "El proyecto ya estaba registrado"

  #Escenarios relacionados con la modificacion de proyectos
  Scenario: Modificar campos del proyecto exitosamente
    Given Existe un proyecto llamado "Proyecto PSA"
    And El estado del proyecto es "Creado"
    When Se trata de modificar el estado del proyecto a "En Proceso"
    Then La solicitud sera exitosa
    And El estado del proyecto sera "En Proceso"

  Scenario: No se puede modificar el nombre de un proyecto a uno ya existente
    Given Existe un proyecto llamado "Proyecto PSA"
    And Existe un proyecto llamado "Proyecto PSA v2"
    When Se trata de modificar el nombre del proyecto "Proyecto PSA v2" a "Proyecto PSA"
    Then La accion debera ser negada porque "El nombre del proyecto ya existe"

  #Escenarios relacionados con la eliminacion de proyectos
  Scenario: Eliminar proyecto exitosamente
    Given Existe un proyecto llamado "Proyecto PSA"
    When Se trata de eliminar el proyecto "Proyecto PSA"
    Then La lista de proyectos no contiene "Proyecto PSA"
