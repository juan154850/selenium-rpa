@echo off

REM Paso 1: Ejecutar el entorno virtual
call venv\Scripts\activate
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

REM Paso 2: Instalar las dependencias
pip install -r requirements.txt
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

REM Paso 3: Ejecutar el programa
python main.py
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

REM Finalizar el entorno virtual (opcional)
deactivate

REM Abrir el archivo nobel_winners.csv
start nobel_winners.csv

REM Pausa para ver los resultados antes de cerrar la ventana (opcional)
pause
