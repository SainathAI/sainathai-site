<# PowerShell Script to Fix Local Paths #>
<# Converts /sainathai-site/ paths to relative paths for local testing #>

$repoRoot = Get-Location
$timestamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
$backupDir = "$repoRoot/backups/$timestamp"

# HTML files to fix
$htmlFiles = @(
    "$repoRoot/index.html",
    "$repoRoot/about.html",
    "$repoRoot/contact.html",
    "$repoRoot/healthcare-automation.html",
    "$repoRoot/services/index.html"
)

Write-Host "Fixing local paths..." -ForegroundColor Green
Write-Host "Backup directory: $backupDir" -ForegroundColor Yellow

foreach ($file in $htmlFiles) {
    if (Test-Path $file) {
        # Create backup
        if (-Not (Test-Path $backupDir)) {
            New-Item -ItemType Directory -Path $backupDir | Out-Null
        }
        Copy-Item -Path $file -Destination "$backupDir/$(Split-Path $file -Leaf).backup"
        
        # Read content
        $content = Get-Content -Path $file -Raw
        
        # Replace all /sainathai-site/ paths with relative paths
        $content = $content -replace 'href="/sainathai-site/', 'href="./'
        $content = $content -replace 'src="/sainathai-site/', 'src="./'
        $content = $content -replace '\'/sainathai-site/', '\'./'
        
        # Write back
        Set-Content -Path $file -Value $content
        Write-Host "✓ Fixed: $(Split-Path $file -Leaf)" -ForegroundColor Green
    }
}

Write-Host "`n✅ All paths fixed for local development!" -ForegroundColor Green
Write-Host "Next: Run 'python -m http.server 8000' and visit http://localhost:8000" -ForegroundColor Yellow
