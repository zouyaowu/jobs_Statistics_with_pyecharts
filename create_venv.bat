@echo off
setlocal enabledelayedexpansion


set local_path=%~dp0
python --version>nul
if %errorlevel% NEQ 0 (echo 未安装python&&pause&&exit)
:loop
start "" /min /wait python -m venv venv
if %errorlevel% NEQ 0 (
    start "" /min /wait python !local_path!get-pip.py
    start "" /wait pip.exe install venv
	goto :loop
)
start "" /min exit .\venv\Scripts\activate.bat
if %errorlevel%==0 (echo 安装成功&&pause&&exit) else (echo 安装失败&&pause&&exit)
