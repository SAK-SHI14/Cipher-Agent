# CIPHER PowerShell Wrapper
# Usage: ./cipher.ps1

Write-Host "🔐 Booting CIPHER Intel Wrapper..." -ForegroundColor Magenta

# Check for Python
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "✘ Python not found. Please install Python and add it to PATH." -ForegroundColor Red
    exit
}

# Clear terminal for clean launch
Clear-Host

# Initialize CIPHER Intelligence
python cipher/main.py
