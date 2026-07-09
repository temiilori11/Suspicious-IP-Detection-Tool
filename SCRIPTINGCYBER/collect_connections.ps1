
$connections = Get-NetTCPConnection |
    Select-Object -Property LocalAddress, LocalPort, RemoteAddress, RemotePort, State, OwningProcess

$finalList = foreach ($conn in $connections) {
    $proc = Get-Process -Id $conn.OwningProcess -ErrorAction SilentlyContinue

    [PSCustomObject]@{
        ProcessName   = $proc.ProcessName
        LocalAddress  = $conn.LocalAddress
        LocalPort     = $conn.LocalPort
        RemoteAddress = $conn.RemoteAddress
        RemotePort    = $conn.RemotePort
        State         = $conn.State
    }
}

$finalList | Export-Csv -NoTypeInformation -Path "connections.csv"
Write-Host "Connection data saved to connections.csv"
