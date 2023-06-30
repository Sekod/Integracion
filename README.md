# Integracion swagger
openapi: 3.0.1
info:
  title: API de delivery de Music Pro.
  description: Esta API se ancarga de manejar la informacion de Music Pro.
  version: 1.0.0
servers:
- url: http://127.0.0.1:8000/api
tags:
- name: Solicitudes
  description: Maneja la informacion de las solicitudes de delivery de Music Pro

paths:
  /solicitud/?format=json:
    post:
      tags:
      - Solicitudes
      summary: Inserta informacion de una nueva solicitud en la base de datos
  
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BodySolicitudesPost'
        required: true
      responses:
        200:
          description: (OK) La informacion de la solicitud se guardo correctamente
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExitoSolicitudesPost'
        400:
          $ref: '#/components/responses/BadRequest'
        401:
          $ref: '#/components/responses/Unauthorized' 
        404:
          $ref: '#/components/responses/NotFound'
        500:
          $ref: '#/components/responses/ServerError'
    
  /solicitud/{codigo}/?format=json:
    get:
      tags:
      - Solicitudes
      summary: Obtiene la infomacion de la base de datos de una solicitud.
      parameters:
      - name: codigo
        in: path
        description: Identificador de la solicitud a obtener
        required: true
        schema:
          type: integer
        
      responses:
        200:
          description: (OK) La informacion de la solicitud se obtuvo correctamente
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExitoSolicitudesGet'
        400:
          $ref: '#/components/responses/BadRequest'
        401:
          $ref: '#/components/responses/Unauthorized' 
        404:
          $ref: '#/components/responses/NotFound'
        500:
          $ref: '#/components/responses/ServerError'
  

components:
  responses:
    
    Unauthorized:
      description: (Unauthorized) No hay autorizacion para llamar al servicio
    
    NotFound:
      description: (NotFound) No se encontro informacion 
    
    BadRequest:
      description: (Bad Request) Los datos enviados son incorrectos o hay datos obligatorios no enviados
      
    ServerError:
      description: Error en servidor
        
    

  schemas:

    BodySolicitudesPost:
      type: object
      properties:
        codigo:
          type: integer
          description: codigo del envio
        nombre:
          type: string
          description: Nombre completo del cliente
        direccion_origen:
          type: string
          description: Direccion origen del envio
        direccion_destino:
          type: string
          description: Direccion destino del envio
  
    ExitoSolicitudesPost:
      type: object
      properties:
        respuesta:
          type: integer
          enum: [1]
          description: Bandera que nos dice si la llamada al servicio fue satisfactoria
        idSolicitud: 
          type: integer
          enum: [233]
          description: Id correspondiente a la solicitud
          
          
    ExitoSolicitudesGet:
      type: object
      properties:
        respuesta:
          type: integer
          enum: [1]
          description: Bandera que nos dice si la llamada al servicio fue satisfactoria
        codigo:
          type: integer
          description: codigo del envio
        precio:
          type: integer
          description: Precio del envio
        nombre:
          type: string
          description: Nombre completo del cliente
        direccion_origen:
          type: string
          description: Direccion origen del envio
        direccion_destino:
          type: string
          description: Direccion destino del envio
        

          
