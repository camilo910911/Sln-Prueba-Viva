hola,

para el desarrollo de la prueba tengo basicamente 4 URL a las que se puede acceder:

- http://127.0.0.1:8000/myapi/     -> No hace nada, simplemente muestra un hola mundo.
- http://127.0.0.1:8000/myapi/list/     -> Retorna la lista de los indices de las principales historias.
- http://127.0.0.1:8000/myapi/index/     -> Muestra la lista de las noticias basado en los parametros i y n. Ejemplo http://127.0.0.1:8000/myapi/index/?i=250&n=20, muestra 20 historias a partir de la historia numero 250.
- http://127.0.0.1:8000/myapi/redis_health/     -> Sirve para verificar el estado derl servidor redis. Muestra lista con los keys de los datos guardados en cache.

- Como no tengo Docker, para ejecutarlo se debe asegurar tener arriba el servidor redis con los parametros por defecto "redis://127.0.0.1:6379/1".
- Folder testenv: Contiene el ambiente de pruebas.
- Folder dev_prueba_viva: Contiene el proyecto con su respectiva App.
	- dev_prueba_viva: Programa principal.
	- myapi: API con solucion realizada del problema. 


