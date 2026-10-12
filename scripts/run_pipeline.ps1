param(
    [string]$ApiDir = "api",
    [Parameter(Mandatory = $true)][string]$ApiVersion,
    [string]$ExtractDir = "extracted",
    [string]$HtmlDir = "API_HTML",
    [string]$MarkdownDir = "markdown",
    [string]$IndexDir = "llm_index",
    [string]$Python = ".venv\Scripts\python.exe",
    [switch]$CleanExtract
)
$ErrorActionPreference = "Stop"
$timings = [ordered]@{}
function Invoke-Stage([string]$Name, [scriptblock]$Action) {
    Write-Host "==> $Name"
    $global:LASTEXITCODE = 0
    $watch = [Diagnostics.Stopwatch]::StartNew()
    & $Action
    if ($LASTEXITCODE) { throw "$Name failed with exit code $LASTEXITCODE" }
    $timings[$Name] = $watch.Elapsed
}
Push-Location (Split-Path -Parent $PSScriptRoot)
try {
    if (-not (Test-Path $Python)) {
        $venvDir = Split-Path -Parent (Split-Path -Parent $Python)
        Invoke-Stage "Create venv" {
            if (Get-Command py.exe -ErrorAction SilentlyContinue) { & py.exe -3 -m venv $venvDir } else { & python.exe -m venv $venvDir }
        }
    }
    $Python = (Resolve-Path $Python).Path
    & $Python -c "import importlib.util, sys; sys.exit(0 if all(importlib.util.find_spec(m) for m in ('bs4', 'lxml')) else 1)"
    if ($LASTEXITCODE) { Invoke-Stage "Install requirements" { & $Python -m pip install -r requirements.txt } }
    if ($CleanExtract -and (Test-Path $ExtractDir)) {
        $extractPath = (Resolve-Path $ExtractDir).Path.TrimEnd('\') + '\'
        if (((Resolve-Path $ApiDir).Path + '\').StartsWith($extractPath, [StringComparison]::OrdinalIgnoreCase)) { throw "Refusing to delete $ExtractDir because it contains $ApiDir" }
        Invoke-Stage "Clean extract directory" { Remove-Item -Recurse -Force $ExtractDir }
    }
    Invoke-Stage "Extract CHM (7-Zip)" { & "$PSScriptRoot\unpack_chm_recursive.ps1" -InputDir $ApiDir -OutputDir $ExtractDir }
    Invoke-Stage "Collect HTML" { & $Python scripts\collect_html.py $ExtractDir -o $HtmlDir --clean }
    Invoke-Stage "Convert to Markdown" { & $Python scripts\convert_sw_api_docs.py $HtmlDir -o $MarkdownDir --clean }
    Invoke-Stage "Build LLM index" { & $Python scripts\build_llm_index.py $MarkdownDir -o $IndexDir --api-version $ApiVersion }
    $manifest = Get-Content (Join-Path $IndexDir "manifest.json") -Raw | ConvertFrom-Json
    Write-Host ""
    Write-Host "Pipeline summary"
    foreach ($stage in $timings.Keys) { Write-Host ("  {0,-26} {1:hh\:mm\:ss}" -f $stage, $timings[$stage]) }
    Write-Host ("  {0,-26} {1}" -f "api_version", $manifest.api_version)
    Write-Host ("  {0,-26} {1}" -f "documents", $manifest.document_count)
    Write-Host ("  {0,-26} {1}" -f "modules", $manifest.module_count)
    Write-Host ("  {0,-26} {1}" -f "markdown_root", $manifest.markdown_root)
}
finally {
    Pop-Location
}
