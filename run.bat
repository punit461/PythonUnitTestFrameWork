@echo off

rem Set the path to your virtual environment activate script
set VENV_PATH=%~dp0venv\Scripts\activate.bat

rem Activate the virtual environment
call "%VENV_PATH%"

rem Run pytest
echo Running unit-test suites - ALL
python .\test_suites