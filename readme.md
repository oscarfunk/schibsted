# Test Regression Suite for Schibsted: 
  
  login, search vehicules and logout features. 

## Assigment: Requirements 

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

OR alternative: run pip against the requirement.txt file

```html
* pip install -r requirements.txt
```


## Running the suite 

* Run suite.py to execute the regression suite. 


```html
nosetests suite.py --with-html
```
by running this command with the html argument a report is created. 


## Project structure:


```html
Documentation
Location	./docs/
Purpose	Package reference documentation
```


```html
Test Suite
Location ./tests
Regression tests for webpage functionalities 
```

```html
Setup.py and Requirements File 
Location	./setup.py   ./requirements 
Purpose	Development dependencies 
```


```html
Resources files (Python modules)
Location ./res
Python modules for page object patterns and webpage locators. By following this technique a layer of separation between the test code and technical implementation is created.
```

```html
Libraries
Location ./lib 
Python dependencies. 
```

```html
Results 
Location ./results 
To store regression test execution reports 
```

```html
Suite.py
Location ./suite.py
```

## FUTURE IMPROVEMENTS - Technical Debt and Refactoring

- Use relative paths for capturing screenshot and create a separate method in a python module. Now is using (C:\\....)
- Create a method to compare search results retrived via Web Search vs Expected Results (i.e Database values)
- Use data pool for feeding test cases (Excel, .txt)
- Improve test reporting capabilities 

