set currentFolder=%~dp0
cd  %currentFolder%
powershell -executionPolicy unrestricted -File  .\docker_build_dev.ps1
docker-compose up -d
powershell -executionPolicy unrestricted -File  .\import_data.ps1
explorer "http://localhost:5000/admin"
pause