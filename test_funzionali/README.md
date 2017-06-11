## Test Funzionali



Per avviare i test eseguire testSuiteComplessiva.py con python 3


All'interno della cartella htmlcov dentro index.html si trova il riassunto dei test

	Statement coverage  	92%
	Branch coverage  		88%
	
	
Per verificare i dati installare il modulo coverage.py
	
	pip install coverage
	
	
Successivamente eseguire il comando:

	coverage run --branch testSuiteComplessiva.py
	
	
Per stampare su terminale il reseconto:

	coverage report
	
	
Per maggiori informazioni:

	https://coverage.readthedocs.io/en/coverage-4.4.1/
	