# Test suite for schibsted login 

## Requirements 

De la página mencionada más abajo, generar tests automatizados para verificar el correcto funcionamiento de:

- Proceso de Login
- Buscador, con los siguientes criterios:
	    - Marca Ford año 2013
	    - Marca Toyota (sin año)
	    - Marca Toyotta año 2002
	    - Marca Toyot año 2009
- Proceso de Logout

Puedes utilizar la herramienta que estimes conveniente, idealmente (pero no obligatorio) Selenium Webdriver.

Entregar la tarea en alguno de los siguientes formatos:

- .zip con todos los archivos necesarios
- Repositorio en sistema de control de versiones (github, gitlab, bitbucket, etc.)

Para lo anterior utilizar las siguientes credenciales:

- URL: http://www.schibsted.cl/testqa

- Usuario: test
- Password: 123123

## Installing

* Run setup.py to install required dependencies (selenium, nose, nose-html-reporting).

```html
python setup.py 
```

## Running the suite 

* Run suite.py to execute the regression suite. 


```html
nosetests suite.py --with-html
```
by running this command with the html argument a report is created. 