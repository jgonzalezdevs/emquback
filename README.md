Pra ejecutar el backend se seben seguir los siguientes pasos:
1 - instalar python (en caso de no tenerlo)
2 - crear un entorno virtual haciendo: python3 -mvenv nombreentorno
3- activar el entorno haciendo: source nombreentorno/bin/activate
4 - hacer pip install -r requirements.txt
5 - se dejo una base de datos de muestra en sqlite asi que con esa se puede probar o eliminarla y hacer python manage.py makemigrations y python3 manage.py migrate
5 - python3 manage.py runserver
