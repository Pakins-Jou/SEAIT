set currentFolder=%~dp0
cd  %currentFolder%
powershell -executionPolicy unrestricted -File  .\docker_build.ps1
docker-compose up -d
explorer "http://localhost:5000/admin"
pause