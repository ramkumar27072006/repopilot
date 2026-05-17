# Bob Demonstration - Quick Start Commands

## Instant Demo Commands

### Windows (PowerShell)
```powershell
# Navigate to project
cd d:\IBM\repopilot

# Run automated demo script
.\demo_script.ps1

# Or run manual commands below
```

### Linux/macOS (Bash)
```bash
# Navigate to project
cd ~/IBM/repopilot

# Make script executable
chmod +x demo_script.sh

# Run automated demo script
./demo_script.sh

# Or run manual commands below
```

---

## Recording Commands

### Start Recording with asciinema
```bash
# Install asciinema
pip install asciinema

# Start recording
asciinema rec bob_demo.cast

# Stop recording: Press Ctrl+D

# Play recording
asciinema play bob_demo.cast

# Upload to share
asciinema upload bob_demo.cast
```

### Windows Terminal Transcript
```powershell
# Start transcript
Start-Transcript -Path "bob_demo.txt"

# Run your commands...

# Stop transcript
Stop-Transcript
```

---

## Essential Demo Commands

### 1. Show Project Structure
```bash
# Windows
tree /F /A

# Linux/macOS
tree -L 3
```

### 2. Run Sample Application
```bash
cd sample_repo
python main.py
```

**Expected Output:**
```
Welcome to simple calc
2 + 3 = 5
10 - 5 = 5
```

### 3. Test Calculator Interactively
```bash
cd sample_repo
python
```

```python
>>> from calculator import add, subtract, multiply, divide
>>> add(10, 20)
30
>>> subtract(100, 25)
75
>>> multiply(5, 6)
30
>>> divide(100, 4)
25.0
>>> exit()
```

### 4. View Documentation
```bash
# Windows
cd generated_docs
type architecture_overview.md

# Linux/macOS
cd generated_docs
cat architecture_overview.md
```

### 5. View Tests
```bash
# Windows
cd generated_tests
type test_core.py

# Linux/macOS
cd generated_tests
cat test_core.py
```

### 6. Code Analysis
```bash
# Count lines
# Windows
find /c /v "" sample_repo\calculator.py

# Linux/macOS
wc -l sample_repo/calculator.py

# Find functions
# Windows
findstr /n "def " sample_repo\calculator.py

# Linux/macOS
grep -n "def " sample_repo/calculator.py
```

---

## Complete Recording Script

### One-Line Demo (Copy & Paste)
```bash
cd d:/IBM/repopilot && echo "=== Bob Demo ===" && tree /F /A && cd sample_repo && python main.py && cd .. && dir generated_docs && dir generated_tests
```

### Full Demo Sequence
```bash
# 1. Navigate
cd d:/IBM/repopilot

# 2. Show structure
tree /F /A

# 3. Run app
cd sample_repo
python main.py

# 4. Test functions
python -c "from calculator import add, subtract; print('Add:', add(10,20)); print('Subtract:', subtract(50,20))"

# 5. Show docs
cd ../generated_docs
dir
type architecture_overview.md | more

# 6. Show tests
cd ../generated_tests
type test_core.py

# 7. Analysis
cd ../sample_repo
findstr /n "def " calculator.py
```

---

## Project Statistics Commands

### File Counts
```bash
# Windows
dir /s /b *.py | find /c /v ""
dir /s /b *.md | find /c /v ""

# Linux/macOS
find . -name "*.py" | wc -l
find . -name "*.md" | wc -l
```

### Line Counts
```bash
# Windows (PowerShell)
(Get-Content sample_repo\calculator.py | Measure-Object -Line).Lines

# Linux/macOS
wc -l sample_repo/calculator.py
```

### Search Patterns
```bash
# Windows
findstr /s /i "def " *.py

# Linux/macOS
grep -r "def " *.py
```

---

## Screen Recording Tools

### OBS Studio (Recommended for Full Screen)
1. Download: https://obsproject.com/
2. Add "Display Capture" source
3. Click "Start Recording"
4. Perform demo
5. Click "Stop Recording"

### Windows Game Bar (Built-in)
```
Win + G - Click Record button
```

### macOS QuickTime
```
QuickTime Player - File - New Screen Recording
```

---

## Pre-Recording Checklist

- [ ] Clear terminal: `cls` (Windows) or `clear` (Linux/macOS)
- [ ] Set terminal size: 120x30 recommended
- [ ] Navigate to project: `cd d:/IBM/repopilot`
- [ ] Test Python: `python --version`
- [ ] Start recording tool
- [ ] Run demo commands
- [ ] Stop recording
- [ ] Save/export recording

---

## Troubleshooting

### Python not found
```bash
# Check installation
python --version
python3 --version

# Add to PATH (Windows)
setx PATH "%PATH%;C:\Python39"
```

### Module import errors
```bash
# Ensure correct directory
cd d:/IBM/repopilot/sample_repo
python main.py
```

### Permission denied (Linux/macOS)
```bash
# Make script executable
chmod +x demo_script.sh
```

---

## Quick Demo Script Template

```bash
#!/bin/bash
echo "=== Bob AI Demo ==="
cd d:/IBM/repopilot
echo "1. Project Structure"
tree -L 2
echo "2. Running Application"
cd sample_repo && python main.py
echo "3. Documentation"
cd ../generated_docs && ls -la
echo "=== Demo Complete ==="
```

---

## Best Practices

1. **Start Clean**: Clear terminal before recording
2. **Add Pauses**: Give viewers time to read (2-3 seconds)
3. **Show Errors**: Demonstrate error handling
4. **Use Comments**: Explain what you're doing
5. **Keep It Short**: 5-10 minutes maximum
6. **Test First**: Run through once before recording

---

## Additional Resources

- Full Guide: [`BOB_DEMONSTRATION.md`](BOB_DEMONSTRATION.md)
- Project README: [`README.md`](README.md)
- Architecture: [`generated_docs/architecture_overview.md`](generated_docs/architecture_overview.md)

---

**Quick Help**: For detailed instructions, see [`BOB_DEMONSTRATION.md`](BOB_DEMONSTRATION.md)

**Team**: MOMO PANDA | **Version**: 1.0 | **Date**: 2026-05-17