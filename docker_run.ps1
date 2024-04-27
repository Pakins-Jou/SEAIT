$appName = "seait" 
$containerName="$($appName)_cntr"
$port=7800
"docker run -e PORT=$port -p $($port):$($port)  --name $containerName -d $appName " | cmd