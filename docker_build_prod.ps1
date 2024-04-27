$currentFolder = $PSScriptRoot
set-location $currentFolder
$app_name = "seait"
$buildEnv = 'prod'# or dev
copy-item  -Path "$PSScriptRoot\default_settings\Dockerfile" -Destination "$PSScriptRoot\" -Force
copy-item  -Path "$PSScriptRoot\default_settings\config.py" -Destination "$PSScriptRoot\" -Force
copy-item  -Path "$PSScriptRoot\settings\.flaskenv" -Destination "$PSScriptRoot\" -Force
$buildParams = Get-Content -path "$currentFolder\default_settings\$($buildEnv)_build_params.json" | ConvertFrom-Json
$dockerCommand = "docker build --build-arg PORT=`"$($buildParams.PORT)`"  --build-arg  FLASK_APP=`"$app_name.py`" --build-arg  FLASK_ENV=`"$($buildParams.FLASK_ENV)`" --build-arg  MONGODB_URL=`"$($buildParams.MONGODB_URL)`" --build-arg MONGODB_DB=`"$($buildParams.MONGODB_DB)`" --build-arg MONGODB_AUTH_MECHANISM=DEFAULT --build-arg SESSION_TYPE=`"$($buildParams.SESSION_TYPE)`"  --build-arg REDIS_URL=`"$($buildParams.REDIS_URL)`" --build-arg  REDIS_QUEUE_NAME=`"$($buildParams.REDIS_QUEUE_NAME)`"  -t  $app_name ."
invoke-expression $dockerCommand