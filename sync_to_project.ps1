# ============================================================
# sync_to_project.ps1
# Mirrors the final, working RAG_Sanskrit_Arya code into
# d:\Sanskrit\RAG_Sanskrit_Project
# Run from anywhere in PowerShell as Administrator if needed.
# ============================================================

$SOURCE = "d:\RAG_Sanskrit_Arya"
$DEST   = "d:\Sanskrit\RAG_Sanskrit_Project"

Write-Host "`n=== Sanskrit RAG Project Sync Script ===" -ForegroundColor Cyan

# ---------- 1. Create folder structure ----------
Write-Host "`n[1/5] Creating folder structure..." -ForegroundColor Yellow
$folders = @(
    "$DEST\code",
    "$DEST\data",
    "$DEST\report"
)
foreach ($folder in $folders) {
    if (-not (Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder -Force | Out-Null
        Write-Host "  Created: $folder"
    } else {
        Write-Host "  Already exists: $folder"
    }
}

# ---------- 2. Copy all Python code files ----------
Write-Host "`n[2/5] Copying code files..." -ForegroundColor Yellow
$codeFiles = @(
    "loader.py",
    "chunker.py",
    "embedder.py",
    "vector_store.py",
    "retriever.py",
    "generator.py",
    "rag_pipeline.py",
    "main.py"
)
foreach ($file in $codeFiles) {
    $src = "$SOURCE\code\$file"
    $dst = "$DEST\code\$file"
    if (Test-Path $src) {
        Copy-Item -Path $src -Destination $dst -Force
        Write-Host "  Copied: code\$file"
    } else {
        Write-Host "  WARNING: Source not found: $src" -ForegroundColor Red
    }
}

# ---------- 3. Copy data files (Sanskrit documents) ----------
Write-Host "`n[3/5] Copying Sanskrit data files..." -ForegroundColor Yellow
# Copy ALL files in data\ so any PDFs/txts you add later also carry over
$dataFiles = Get-ChildItem -Path "$SOURCE\data" -File -ErrorAction SilentlyContinue
if ($dataFiles) {
    foreach ($f in $dataFiles) {
        Copy-Item -Path $f.FullName -Destination "$DEST\data\$($f.Name)" -Force
        Write-Host "  Copied: data\$($f.Name)"
    }
} else {
    Write-Host "  WARNING: No data files found in $SOURCE\data" -ForegroundColor Red
}

# ---------- 4. Copy root files ----------
Write-Host "`n[4/5] Copying root files (README, requirements, report)..." -ForegroundColor Yellow
$rootFiles = @("requirements.txt", "README.md")
foreach ($file in $rootFiles) {
    $src = "$SOURCE\$file"
    $dst = "$DEST\$file"
    if (Test-Path $src) {
        Copy-Item -Path $src -Destination $dst -Force
        Write-Host "  Copied: $file"
    } else {
        Write-Host "  WARNING: $src not found" -ForegroundColor Red
    }
}

# Copy report\report.md
$reportSrc = "$SOURCE\report\report.md"
$reportDst = "$DEST\report\report.md"
if (Test-Path $reportSrc) {
    Copy-Item -Path $reportSrc -Destination $reportDst -Force
    Write-Host "  Copied: report\report.md"
}

# ---------- 5. Remove old sample_sanskrit.txt if present in destination ----------
Write-Host "`n[5/5] Cleaning outdated files from destination..." -ForegroundColor Yellow
$oldSample = "$DEST\data\sample_sanskrit.txt"
if (Test-Path $oldSample) {
    Remove-Item -Path $oldSample -Force
    Write-Host "  Removed stale: data\sample_sanskrit.txt"
} else {
    Write-Host "  No stale files to clean."
}

# ---------- Done ----------
Write-Host "`n=== Sync Complete! ===" -ForegroundColor Green
Write-Host "Destination: $DEST"
Write-Host ""
Write-Host "Next steps:"
Write-Host "  1. cd $DEST"
Write-Host "  2. pip install -r requirements.txt"
Write-Host "  3. python code/main.py --mode ingest"
Write-Host "  4. python code/main.py --mode demo"
Write-Host ""
