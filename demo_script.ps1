# ============================================
# BOB AI ASSISTANT - QUICK DEMONSTRATION SCRIPT
# ============================================
# This PowerShell script demonstrates Bob's capabilities
# Run with: .\demo_script.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "IBM Bob AI Assistant Demonstration" -ForegroundColor Cyan
Write-Host "Project: RepoPilot" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Function to pause and wait for user
function Pause-Demo {
    param([string]$message = "Press Enter to continue...")
    Write-Host ""
    Write-Host $message -ForegroundColor Yellow
    $null = Read-Host
}

# 1. Show Project Structure
Write-Host "=== STEP 1: Project Structure ===" -ForegroundColor Green
Write-Host "Displaying RepoPilot project structure..." -ForegroundColor White
Get-ChildItem -Recurse -Directory | Select-Object FullName | Format-Table -AutoSize
Pause-Demo

# 2. Display README
Write-Host "=== STEP 2: Project Overview ===" -ForegroundColor Green
Write-Host "Reading README.md..." -ForegroundColor White
Get-Content README.md | Select-Object -First 30
Write-Host "... (truncated for demo)" -ForegroundColor Gray
Pause-Demo

# 3. Run Sample Application
Write-Host "=== STEP 3: Running Sample Calculator ===" -ForegroundColor Green
Write-Host "Executing sample_repo/main.py..." -ForegroundColor White
Push-Location sample_repo
python main.py
Pop-Location
Pause-Demo

# 4. Test Calculator Functions
Write-Host "=== STEP 4: Testing Calculator Functions ===" -ForegroundColor Green
Write-Host "Running interactive calculator tests..." -ForegroundColor White

$pythonCode = @"
from calculator import add, subtract, multiply, divide

print('Testing add(15, 25):', add(15, 25))
print('Testing subtract(50, 20):', subtract(50, 20))
print('Testing multiply(7, 8):', multiply(7, 8))
print('Testing divide(100, 5):', divide(100, 5))

try:
    divide(10, 0)
except ValueError as e:
    print('Testing divide by zero - Error:', e)
"@

Set-Location sample_repo
$pythonCode | python
Set-Location ..
Pause-Demo

# 5. Show Generated Documentation
Write-Host "=== STEP 5: Generated Documentation ===" -ForegroundColor Green
Write-Host "Listing documentation files..." -ForegroundColor White
Get-ChildItem generated_docs | Format-Table Name, Length, LastWriteTime
Write-Host ""
Write-Host "Preview of architecture_overview.md:" -ForegroundColor White
Get-Content generated_docs/architecture_overview.md | Select-Object -First 20
Write-Host "... (truncated for demo)" -ForegroundColor Gray
Pause-Demo

# 6. Show Generated Tests
Write-Host "=== STEP 6: Generated Tests ===" -ForegroundColor Green
Write-Host "Displaying test files..." -ForegroundColor White
Get-ChildItem generated_tests | Format-Table Name, Length, LastWriteTime
Write-Host ""
Write-Host "Preview of test_core.py:" -ForegroundColor White
Get-Content generated_tests/test_core.py | Select-Object -First 25
Write-Host "... (truncated for demo)" -ForegroundColor Gray
Pause-Demo

# 7. Code Analysis
Write-Host "=== STEP 7: Code Analysis ===" -ForegroundColor Green
Write-Host "Analyzing calculator.py..." -ForegroundColor White
$calcFile = "sample_repo/calculator.py"
$lineCount = (Get-Content $calcFile | Measure-Object -Line).Lines
Write-Host "Total lines: $lineCount" -ForegroundColor Cyan
Write-Host ""
Write-Host "Function definitions found:" -ForegroundColor White
Select-String -Path $calcFile -Pattern "^def " | ForEach-Object {
    Write-Host "  Line $($_.LineNumber): $($_.Line.Trim())" -ForegroundColor Cyan
}
Pause-Demo

# 8. File Statistics
Write-Host "=== STEP 8: Project Statistics ===" -ForegroundColor Green
Write-Host "Calculating project metrics..." -ForegroundColor White
$pythonFiles = Get-ChildItem -Recurse -Filter *.py
$mdFiles = Get-ChildItem -Recurse -Filter *.md
Write-Host "Python files: $($pythonFiles.Count)" -ForegroundColor Cyan
Write-Host "Markdown files: $($mdFiles.Count)" -ForegroundColor Cyan
Write-Host ""
Write-Host "Total lines of Python code:" -ForegroundColor White
$totalLines = 0
$pythonFiles | ForEach-Object {
    $lines = (Get-Content $_.FullName | Measure-Object -Line).Lines
    $totalLines += $lines
    Write-Host "  $($_.Name): $lines lines" -ForegroundColor Cyan
}
Write-Host "Total: $totalLines lines" -ForegroundColor Green
Pause-Demo

# 9. Demonstration Complete
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Demonstration Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Bob AI Assistant successfully demonstrated:" -ForegroundColor White
Write-Host "  [OK] Project structure analysis" -ForegroundColor Green
Write-Host "  [OK] Code execution and testing" -ForegroundColor Green
Write-Host "  [OK] Documentation generation" -ForegroundColor Green
Write-Host "  [OK] Test suite creation" -ForegroundColor Green
Write-Host "  [OK] Code analysis and metrics" -ForegroundColor Green
Write-Host ""
Write-Host "For more details, see BOB_DEMONSTRATION.md" -ForegroundColor Yellow
Write-Host ""

# Made with Bob
