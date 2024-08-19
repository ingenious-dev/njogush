@REM Windows batch adaptation of daphne.bash (https://chatgpt.com/share/ddeebe28-2544-499b-993d-f42e7a019400)

@echo off
rem Get the directory of the script
set SCRIPT_DIR=%~dp0

rem Change to the script directory
cd /d %SCRIPT_DIR%

@REM rem rem Find executable files named daphne
@REM for /r %SCRIPT_DIR%\venv %%i in (daphne.exe) do set ar=%%i

@REM rem Run the Django server
@REM @REM %ar% -b 0.0.0.0 -p 6564 njogush.asgi:application
@REM %ar%  -p 6564 njogush.asgi:application

rem Find the python3 executable in the venv directory
@REM for /r %SCRIPT_DIR%\venv %%i in (python.exe) do set PYTHON_PATH=%%i
@REM + https://stackoverflow.com/questions/56204703/how-do-you-add-a-variable-to-a-string-in-a-batch-file
for /r "%SCRIPT_DIR%\venv" %%i in (python.exe) do set PYTHON_PATH=%%i

rem Run the Django server
"%PYTHON_PATH%" manage.py runserver 0.0.0.0:6564