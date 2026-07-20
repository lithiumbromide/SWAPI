param(
    [string]$InputDir = "api",
    [string]$OutputDir = "extracted"
)

$ErrorActionPreference = "Stop"

$sevenZip = Get-Command 7z.exe -ErrorAction SilentlyContinue
if (-not $sevenZip) {
    $defaultPath = "${env:ProgramFiles}\7-Zip\7z.exe"
    if (Test-Path $defaultPath) {
        $sevenZip = @{ Source = $defaultPath }
    }
}

if (-not $sevenZip) {
    Write-Error @"
7z.exe was not found.

Install 7-Zip and ensure 7z.exe is in PATH, or install it to:
$env:ProgramFiles\7-Zip
"@
    exit 127
}

$InputDir = (Resolve-Path $InputDir).Path

if (-not (Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir | Out-Null
}
$OutputDir = (Resolve-Path $OutputDir).Path

$pass = 1
$totalProcessed = 0
$totalSkipped = 0
$totalErrors = 0

while ($true) {

    Write-Host "========================================"
    Write-Host "PASS $pass"
    Write-Host "INPUT : $InputDir"
    Write-Host "OUTPUT: $OutputDir"
    Write-Host "========================================"

    $processedThisPass = 0
    $skippedThisPass = 0
    $errorsThisPass = 0

    $chmFiles = @(
        if (Test-Path $InputDir) {
            Get-ChildItem $InputDir -Recurse -File -Filter *.chm
        }
        if (Test-Path $OutputDir) {
            Get-ChildItem $OutputDir -Recurse -File -Filter *.chm
        }
    ) |
    Sort-Object FullName -Unique

    foreach ($chmFile in $chmFiles) {

        $chmPath = $chmFile.FullName
        $chmDir = $chmFile.DirectoryName
        $chmName = [IO.Path]::GetFileNameWithoutExtension($chmFile.Name)

        if ($chmDir.StartsWith($InputDir, [StringComparison]::OrdinalIgnoreCase)) {
            $relDir = $chmDir.Substring($InputDir.Length).TrimStart('\')
        }
        elseif ($chmDir.StartsWith($OutputDir, [StringComparison]::OrdinalIgnoreCase)) {
            $relDir = $chmDir.Substring($OutputDir.Length).TrimStart('\')
        }
        else {
            $relDir = ""
        }

        $outDir = if ($relDir) {
            Join-Path (Join-Path $OutputDir $relDir) $chmName
        }
        else {
            Join-Path $OutputDir $chmName
        }

        $markerFile = Join-Path $outDir ".chm_extracted"

        Write-Host
        Write-Host "CHM : $chmPath"
        Write-Host "OUT : $outDir"

        if (Test-Path $markerFile) {
            Write-Host "SKIP: marker exists"
            $skippedThisPass++
            continue
        }

        New-Item -ItemType Directory -Force -Path $outDir | Out-Null

        try {

            & $sevenZip.Source x "-o$outDir" -y $chmPath *> $null

            if ($LASTEXITCODE -eq 0 -and (Get-ChildItem $outDir -Recurse -File -ErrorAction SilentlyContinue | Select-Object -First 1)) {

                New-Item -ItemType File -Path $markerFile -Force | Out-Null
                Write-Host "OK"
                $processedThisPass++
            }
            else {
                Write-Host "ERROR"
                $errorsThisPass++
            }
        }
        catch {
            Write-Host "ERROR"
            $errorsThisPass++
        }
    }

    $totalProcessed += $processedThisPass
    $totalSkipped += $skippedThisPass
    $totalErrors += $errorsThisPass

    Write-Host
    Write-Host "PASS $pass SUMMARY:"
    Write-Host "processed: $processedThisPass"
    Write-Host "skipped:   $skippedThisPass"
    Write-Host "errors:    $errorsThisPass"

    if ($processedThisPass -eq 0) {
        break
    }

    $pass++
}

Write-Host
Write-Host "========================================"
Write-Host "FINAL SUMMARY"
Write-Host "processed: $totalProcessed"
Write-Host "skipped:   $totalSkipped"
Write-Host "errors:    $totalErrors"
Write-Host "passes:    $pass"
Write-Host "========================================"