function Get-ParameterValue {
   # Specifies a path to one or more locations. Wildcards are permitted.
   param([Parameter(Mandatory=$true,
              Position=0,
              ValueFromPipeline=$true,
              ValueFromPipelineByPropertyName=$true,
              HelpMessage="Name of parameter")]
   [ValidateNotNullOrEmpty()]
   [SupportsWildcards()]
   [string]
   $paramName
   ,[Parameter(Mandatory=$false,
   Position=1,
   ValueFromPipeline=$true,
   ValueFromPipelineByPropertyName=$true,
   HelpMessage="Default value to use if no value is provided")]
[ValidateNotNullOrEmpty()]
[SupportsWildcards()]
[string]
$defaultValue=$null
   
   )

   $paramValue = $null;
   while( ($null  -eq $paramValue -or $paramValue  -eq "") -and $defaultValue -eq $null ){    
        $paramValue = Read-Host  "Please provide a value for  $paramName"
   }
    if($null  -eq $paramValue){

        $paramValue  = $defaultValue
    }
   return  $paramValue 
   
}

$command = ".\gcp_deploy.ps1 -init `$true"
$command |cmd 

$command = ".\gcp_deploy.ps1 -auth `$true"
$command |cmd 

Write-Host "Please select a project from the list below:"
$command = ".\gcp_deploy.ps1 -listProjects `$true"
$command |cmd 


$projectID = "seait-422314"  
$projectName ="seait"
.\gcp_deploy.ps1 -projectName "seait" -setProjectID $true -projectID  "seait-422314" 

.\gcp_deploy.ps1 -projectName "seait" -listBillingAc $true 

$billingAccountID="012680-B87B67-46D47D"
 .\gcp_deploy.ps1 -projectName "seait" -projectID seait-422314 -linkBillingAc $true -billingAccount $billingAccountID

 .\gcp_deploy.ps1 -projectName "seait" -projectID seait-422314 -linkBillingAc $true -billingAccount 012680-B87B67-46D47D

 $region = "northamerica-northeast1"
$deployParameters=@{
"maxInstances"=1;
"port"=5000;
"envVars"="FLASK_APP=seait.py,FLASK_ENV=production,MONGODB_DB=seaitdb,REDIS_QUEUE_NAME=seaitdb";
"region"="$($region)";"serviceAccount"="seait-69@seait-422314.iam.gserviceaccount.com";"containerRepo"="docker.io/neoandrey/seait" 
};
$deployParameters=$deployParameters|Convertto-JSON


 .\gcp_deploy.ps1 -projectName "seait" -projectID seait-422314 -deploy $true -deployParams $deployParameters


docker tag seait gcr.io/seait-422314/seait



seait-69@seait-422314.iam.gserviceaccount.com

gcloud iam service-accounts list

docker exec gcloud-cli gcloud auth activate-service-account  --key-file=/opt/seait/seait-422314-b8dcceb194e7.json


docker exec gcloud-cli gcloud artifacts repositories create neorepo --repository-format=docker --location=northamerica-northeast1 --description="neorepo" --immutable-tags --async

docker exec gcloud-cli gcloud artifacts repositories list
docker exec gcloud-cli gcloud services enable cloudresourcemanager.googleapis.com
docker exec gcloud-cli gcloud projects add-iam-policy-binding seait-422314 --member='serviceAccount:seait' --role='roles/editor'
docker exec gcloud-cli gcloud projects add-iam-policy-binding seait-422314 --member=serviceAccount:seait --role=roles/artifactregistry.admin


docker exec gcloud-cli gcloud projects add-iam-policy-binding seait-422314 --member=serviceAccount:seait-69@seait-422314.iam.gserviceaccount.com  --role=roles/artifactregistry.admin

gcloud components install docker-credential-gcr
docker exec gcloud-cli gcloud auth configure-docker

docker exec gcloud-cli  gcloud run deploy seait  --image docker.io/neoandrey/seait --max-instances=1 --port 5000 --set-env-vars=FLASK_APP=seait.py,FLASK_ENV=production,MONGODB_DB=seaitdb,MONGODB_URL=mongodb+srv://neo:M0ng0DB123@neocrystalclstr01.fv9vk.mongodb.net/seait?retryWrites=true&w=majority,SESSION_TYPE=redis,REDIS_URL=redis://default:Red1sSeait123!@redis-11987.c280.us-central1-2.gce.cloud.redislabs.com:11987,REDIS_QUEUE_NAME=seaitdb,PORT=5000 --region=northamerica-northeast1 --allow-unauthenticated   --service-account seait-69@seait-422314.iam.gserviceaccount.com