@echo off
setlocal enabledelayedexpansion

set local_path=%~dp0
echo !local_path!
if not exist venv (
	echo  *** not exist venv, start to create
	call :create_venv
)
echo  *** start to install requirements
@echo.
!local_path!\venv\Scripts\pip3.exe install -r !local_path!\requirements.txt
@echo.
echo ��װ��������������˳�
pause>nul
exit



:create_venv
set local_path=%~dp0
python --version>nul
if %errorlevel% NEQ 0 (echo �޷�����python&&pause&&exit)
:loop
start "" /min /wait python -m venv venv
if %errorlevel% NEQ 0 (
    echo "û�а�װ venvģ��,������װ"
    start "" /min /wait python !local_path!get-pip.py
    start "" /wait pip.exe install venv
	goto :loop
)
start "" /min exit .\venv\Scripts\activate.bat
if %errorlevel%==0 (
	echo ��װpython���⻷���ɹ�
	REM ���ص��õĵط�
	goto :eof
) else (
	echo ��װʧ��
	pause
	exit
)
