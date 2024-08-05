# Tercera pre entrega Bustos

## Base de datos
1. Soloamente esta creado el usuario admin con permisos de administrador.
```
user: admin
pass: admin
```
2. En las tablas SQL estan cargados:
   1. Clientes: solo esta cargado el cliente leandro bustos
   2. Detalles de pedido: solo tenemos cargada una orden 
   3. Pedidos: solo hay un pedido
   4.  Products: solo hay tres productos 

## Pruebas y funcionalidad
1. En el header de la pagina web encontrarás los botones de inicio, libros, crear pedido, consultar pedido. En toda la pagina se usa el archivo base.html que tiene el cuerpo principal para luego usar herencia con jinja en el resto de los archivos html
   1. Inicio: te lleva a la pagina de inicio de la libreria con fotos y descripcion.
   2. Libros: muestra todos los libros cargados en la base de datos.
   3. Crear pedido: posee un formulario que es para cargar un pedido de uno o varios libros existentes en stock. A su vez, este formulario permite la creación de un usuario comprador en caso de no seleccionar un usuario existente. El fomulario permite agregar mas de un libro
   4.  Consultar pedido: un form que al poner el numero de pedido te trae toda la info
2. Para cargar el stock de los libros, dado que es una tarea del vendedor/administrador, la misma se debe hacer desde el url localhost:8000/admin. Con el usuario admin y pass admin

## Modelo de base de datos

## Pasos para ejecutar la aplicacion
1. Descarga el repositorio 
2. Parate dentro de la carpeta que contenga `manage.py`, en este caso debes pararte dentro de `proyectos_libros`
3. Ejecuta `python manage.py runserver`para correr el servidor
   


## Pasos en caso que se quiere arrancar el proyecto desde cero
### Elimina todos los archivos innecesarios para empezar de 0
1. Borra la base de datos db.sqlite3
2. Borra los archivos .py, salvo el `__init__.py`

### Orden de instalacion correcta de la aplicacion
1. Clona el projecto ejecutando el comando `git clone <url>`
2. Dirigete a la carpeta del proyecto usando `cd <nombre de la carpeta>`
3. Crear un entorno virtual (debe tener instalado pipenv), ejecuta `pipenv --python 3.12.4` 
4. Ejecuta `pipenv shell`para iniciar el virtual envirioment
5. Ejecuta 
6. pipenv install -r requirements.txt

### Primeros pasos para configurar la app
Una vez seteado el ambiente, debemos iniciar la app y su configuracion.
1. Cambiate a la carpeta principal del proyecto (proyecto_libros)
2. Ejecuta el sisguiente comando para preparar las migraciones de la base da datos `python manage.py makemigrations`
3. Ejecuta las migraciones para crear la base python manage.py migrate
4. Crea un usuario admin `python manage.p createsuperuser`, completa los datos. Para esta caso se uso usario admin y contraseña admin

### Ejecutar el servidor
1. Ejecuta `python manage.py runserver`para correr el servidor

