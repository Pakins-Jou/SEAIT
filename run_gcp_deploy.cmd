set currentFolder=%~dp0
cd  %currentFolder%
powershell -executionPolicy Unrestricted -File .\run_gcp_deploy.ps1
pause