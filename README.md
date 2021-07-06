# Deploy Desarrollo de Software

Está hecho en Django, Gunicorn, Postgres con motor web nginx como el proxy inverso

### Local

Usar `sudo docker-compose -f docker-compose-dev.yml up --build -d` para levantar la app en un daemon thread en local. Ejecutar `sudo docker-compose exec web python manage.py migrate --noinput` para migrar la base de datos.

Si ocurre un error, hacer `sudo docker-compose -f docker-compose-dev.yml down -v` para bajar la app y los volumenes, e intentar nuevamente

### Docker-compose

La app se encuentra arriba y funcionando en https://swdev9.ing.puc.cl/.

Pueden verse los detalles de los 3 requisitos en el archivo docker-compose. La aplicación se encuentra en un daemon thread y pueden bajarla del server, y luego volverla a subir con "sudo docker-compose up". Si quisieran bajar los volúmenes de la base de datos, o partir deployeando desde 0, para subirlos se debe hacer `sudo docker-compose up -d --build`, `sudo docker-compose exec web python manage.py migrate --noinput`, `sudo ./init-letsencrypt.sh` (script para obtener permisos SSL actualizados, si no se puede ejecutar se debe correr `chmod +x init-letsencrypt.sh`) y luego `sudo docker-compose up -d`.

Cambiar en las variables de entorno, en nginx/conf.d y en el archivo init-letsencrypt.sh los valores correspondientes al dominio nuevo.

Los detalles del proxy inverso se pueden ver tanto en docker-compose.yml como en nginx/conf.d con sus puertos correspondientes.
