$database="seait"
$collections = @('Awareness','Biases','CandidateInfo','Categories','Details','GroupCodes','OptionSets','Principles', 'Questions','Recommendations', 'Results','Roles','Summaries', 'Tactics')
$collections |%{
$collection =  $_
$importCommand= "docker exec -it seait-main-db-1 /bin/bash -c 'mongoimport --uri mongodb://mongo:Park123!@localhost:27017/test?directConnection=true --authenticationDatabase=admin --collection $collection --type json --file /tmp/data/$($database)db-$($collection).json'"
write-host "Running command: $importCommand"
invoke-expression $importCommand
}

