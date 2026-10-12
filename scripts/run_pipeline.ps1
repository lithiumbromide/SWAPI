param(
    [string]$ApiDir = "api",
    [Parameter(Mandatory = $true)][string]$ApiVersion,
    [string]$ExtractDir = "extracted",
    [string]$HtmlDir = "API_HTML",
    [string]$MarkdownDir = "markdown",
    [string]$IndexDir = "llm_index",
    [string]$Python = ".venv\Scripts\python.exe",
    [switch]$CleanExtract,
    [switch]$Force
)
$ErrorActionPreference = "Stop"
$callerDir = (Get-Location).ProviderPath
$repoRoot = Split-Path -Parent $PSScriptRoot
$timings = [ordered]@{}
function Invoke-Stage([string]$Name, [scriptblock]$Action) {
    Write-Host "==> $Name"
    $global:LASTEXITCODE = 0
    $watch = [Diagnostics.Stopwatch]::StartNew()
    & $Action
    if ($LASTEXITCODE) { throw "$Name failed with exit code $LASTEXITCODE" }
    $timings[$Name] = $watch.Elapsed
}
function Get-FullPath([string]$Path) {
    [IO.Path]::GetFullPath([IO.Path]::Combine((Get-Location).ProviderPath, $Path)).TrimEnd('\') + '\'
}
function Get-ModuleCount([string]$Path) {
    if (Test-Path $Path) { @(Get-ChildItem $Path -Directory).Count } else { 0 }
}
Push-Location $repoRoot
try {
    if (Test-Path $Python) {
        $Python = (Resolve-Path $Python).Path
    }
    elseif ($Python -match '[\\/]Scripts[\\/]python\.exe$') {
        $venvDir = Split-Path -Parent (Split-Path -Parent $Python)
        Invoke-Stage "Create venv" { if (Get-Command py.exe -ErrorAction SilentlyContinue) { & py.exe -3 -m venv $venvDir } else { & python.exe -m venv $venvDir } }
        $Python = (Resolve-Path $Python).Path
    }
    else {
        $command = Get-Command $Python -ErrorAction SilentlyContinue
        if (-not $command) { throw "Python interpreter '$Python' was not found. Pass python.exe on PATH, a full path, or a <venv>\Scripts\python.exe path to create that venv." }
        $Python = $command.Source
    }
    Invoke-Stage "Install requirements" { & $Python -m pip install --disable-pip-version-check --quiet -r requirements.txt }
    if ($CleanExtract -and (Test-Path $ExtractDir)) {
        $target = Get-FullPath $ExtractDir
        $isRoot = [IO.Path]::GetPathRoot($target).TrimEnd('\') + '\' -eq $target
        $protected = @($repoRoot, $callerDir, $ApiDir) | ForEach-Object { Get-FullPath $_ } | Where-Object { $_.StartsWith($target, [StringComparison]::OrdinalIgnoreCase) }
        if ($isRoot -or $protected) { throw "Refusing to delete '$ExtractDir' because it is a filesystem root or contains the repository, the current directory or the API directory." }
        Invoke-Stage "Clean extract directory" { Remove-Item -LiteralPath $target -Recurse -Force }
    }
    Invoke-Stage "Extract CHM (7-Zip)" { & "$PSScriptRoot\unpack_chm_recursive.ps1" -InputDir $ApiDir -OutputDir $ExtractDir }
    Invoke-Stage "Collect HTML" { & $Python scripts\collect_html.py $ExtractDir -o $HtmlDir --clean }
    $htmlModules = Get-ModuleCount $HtmlDir
    $markdownModules = Get-ModuleCount $MarkdownDir
    if ($htmlModules -lt $markdownModules -and -not $Force) {
        throw "'$HtmlDir' has $htmlModules module directories but '$MarkdownDir' has $markdownModules, so convert --clean would drop modules. Check the CHM set in '$ApiDir' or rerun with -Force."
    }
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
