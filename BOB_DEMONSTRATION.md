# Bob AI Assistant - Complete Demonstration Guide

## Overview
This guide demonstrates how IBM Bob works with the RepoPilot project, including terminal commands for recording the application in action.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Recording Setup](#recording-setup)
3. [Demonstration Scenarios](#demonstration-scenarios)
4. [Terminal Commands Reference](#terminal-commands-reference)
5. [Expected Outputs](#expected-outputs)

---

## Prerequisites

### Required Software
- **Python 3.8+** installed
- **Git** for version control
- **Terminal recording tool** (choose one):
  - **asciinema** (recommended for terminal recording)
  - **Windows Terminal** with built-in recording
  - **OBS Studio** for screen recording
  - **Terminalizer** for animated terminal recordings

### Install Recording Tools

**Windows (PowerShell)**:
```powershell
# Install asciinema via pip
pip install asciinema

# Or use Windows Terminal (built-in)
# Or install OBS Studio from https://obsproject.com/
```

**macOS/Linux**:
```bash
# Install asciinema
pip install asciinema
# or
brew install asciinema  # macOS
sudo apt-get install asciinema  # Ubuntu/Debian
```

---

## Recording Setup

### 1. Start Terminal Recording

**Using asciinema (Cross-platform)**:
```bash
# Start recording
asciinema rec bob_demo.cast

# When done, press Ctrl+D to stop
# Upload to asciinema.org (optional)
asciinema upload bob_demo.cast
```

**Using Windows Terminal**:
```powershell
# Windows Terminal doesn't have built-in recording
# Use PowerShell transcript instead
Start-Transcript -Path "bob_demo_transcript.txt"

# When done
Stop-Transcript
```

**Using OBS Studio**:
1. Open OBS Studio
2. Add "Display Capture" or "Window Capture" source
3. Click "Start Recording"
4. Perform demonstrations
5. Click "Stop Recording"

---

## Demonstration Scenarios

### Scenario 1: Basic Project Setup and Exploration

```bash
# Navigate to project directory
cd d:/IBM/repopilot

# Show project structure
tree /F
# or on Linux/macOS: tree -L 3

# List all files
dir /s /b
# or on Linux/macOS: find . -type f

# Show README content
type README.md
# or on Linux/macOS: cat README.md
```

### Scenario 2: Running the Sample Application

```bash
# Navigate to sample repository
cd sample_repo

# Run the calculator application
python main.py

# Expected output:
# Welcome to simple calc
# 2 + 3 = 5
# 10 - 5 = 5
```

### Scenario 3: Testing Calculator Functions

```bash
# Create a test script
cd d:/IBM/repopilot/sample_repo

# Run Python interactive mode
python

# In Python shell:
>>> from calculator import add, subtract, multiply, divide
>>> add(10, 20)
30
>>> subtract(100, 25)
75
>>> multiply(5, 6)
30
>>> divide(100, 4)
25.0
>>> divide(10, 0)  # This will raise ValueError
>>> exit()
```

### Scenario 4: Viewing Generated Documentation

```bash
# Navigate to generated docs
cd d:/IBM/repopilot/generated_docs

# List documentation files
dir
# or on Linux/macOS: ls -la

# View architecture overview
type architecture_overview.md
# or on Linux/macOS: cat architecture_overview.md

# View getting started guide
type getting_started.md

# View module notes
type module_notes.md
```

### Scenario 5: Viewing Generated Tests

```bash
# Navigate to generated tests
cd d:/IBM/repopilot/generated_tests

# List test files
dir
# or on Linux/macOS: ls -la

# View test file
type test_core.py
# or on Linux/macOS: cat test_core.py

# Run tests (if pytest is installed)
pytest test_core.py -v
```

### Scenario 6: Bob AI Interaction Demonstration

```bash
# This demonstrates how Bob would interact with the project

# 1. Code Analysis
cd d:/IBM/repopilot

# Bob analyzes the calculator module
python -c "import ast; print(ast.dump(ast.parse(open('sample_repo/calculator.py').read())))"

# 2. File Operations
# Bob can read files
type sample_repo\calculator.py

# Bob can search for patterns
findstr /s /i "def " sample_repo\*.py
# or on Linux/macOS: grep -r "def " sample_repo/

# 3. Documentation Generation
# Bob generates documentation by analyzing code structure
python -c "import inspect; import sys; sys.path.insert(0, 'sample_repo'); import calculator; print(inspect.getdoc(calculator))"
```

---

## Terminal Commands Reference

### Essential Commands for Recording

#### 1. Project Navigation
```bash
# Windows
cd d:\IBM\repopilot
dir
tree /F

# Linux/macOS
cd ~/IBM/repopilot
ls -la
tree -L 3
```

#### 2. File Viewing
```bash
# Windows
type filename.txt
more filename.txt
notepad filename.txt

# Linux/macOS
cat filename.txt
less filename.txt
nano filename.txt
```

#### 3. Python Execution
```bash
# Run Python script
python script.py

# Run Python module
python -m module_name

# Interactive Python
python
>>> import module
>>> help(module)
>>> exit()

# Execute Python one-liner
python -c "print('Hello from Bob')"
```

#### 4. Code Analysis
```bash
# Count lines of code
# Windows
find /c /v "" *.py

# Linux/macOS
wc -l *.py

# Search for patterns
# Windows
findstr /s /i "pattern" *.py

# Linux/macOS
grep -r "pattern" *.py
```

#### 5. Git Operations
```bash
# Show repository status
git status

# Show commit history
git log --oneline -10

# Show file differences
git diff filename.py

# Show branch information
git branch -a
```

---

## Expected Outputs

### 1. Running main.py
```
Welcome to simple calc
2 + 3 = 5
10 - 5 = 5
```

### 2. Calculator Function Tests
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
```

### 3. Project Structure
```
repopilot/
├── README.md
├── bob_sessions/
├── generated_docs/
│   ├── architecture_overview.md
│   ├── getting_started.md
│   ├── module_notes.md
│   ├── refactor_report.md
│   └── test_coverage_notes.md
├── generated_tests/
│   └── test_core.py
├── sample_repo/
│   ├── calculator.py
│   └── main.py
└── src/
```

---

## Complete Recording Script

Here's a complete script you can follow for a comprehensive demonstration:

```bash
# ============================================
# BOB DEMONSTRATION RECORDING SCRIPT
# ============================================

# Start recording
asciinema rec bob_complete_demo.cast

# 1. Introduction
echo "=== IBM Bob AI Assistant Demonstration ==="
echo "Project: RepoPilot - Intelligent Code Documentation Tool"
echo ""

# 2. Show project structure
echo "=== Project Structure ==="
cd d:/IBM/repopilot
tree /F /A
echo ""

# 3. Display README
echo "=== Project Overview ==="
type README.md | more
echo ""

# 4. Run sample application
echo "=== Running Sample Calculator Application ==="
cd sample_repo
python main.py
echo ""

# 5. Interactive Python demonstration
echo "=== Testing Calculator Functions ==="
python << EOF
from calculator import add, subtract, multiply, divide

print("Testing add(15, 25):", add(15, 25))
print("Testing subtract(50, 20):", subtract(50, 20))
print("Testing multiply(7, 8):", multiply(7, 8))
print("Testing divide(100, 5):", divide(100, 5))

try:
    divide(10, 0)
except ValueError as e:
    print("Testing divide by zero:", e)
EOF
echo ""

# 6. Show generated documentation
echo "=== Generated Documentation ==="
cd ../generated_docs
dir
echo ""
echo "--- Architecture Overview ---"
type architecture_overview.md | more
echo ""

# 7. Show generated tests
echo "=== Generated Tests ==="
cd ../generated_tests
type test_core.py
echo ""

# 8. Code analysis
echo "=== Code Analysis ==="
cd ../sample_repo
echo "Lines of code in calculator.py:"
find /c /v "" calculator.py
echo ""
echo "Function definitions:"
findstr /n "def " calculator.py
echo ""

# 9. Conclusion
echo "=== Demonstration Complete ==="
echo "Bob successfully analyzed, documented, and tested the RepoPilot project"
echo ""

# Stop recording (Ctrl+D)
```

---

## Advanced Recording Techniques

### 1. Create Animated GIF from Recording
```bash
# Convert asciinema recording to GIF
npm install -g asciicast2gif
asciicast2gif bob_demo.cast bob_demo.gif
```

### 2. Add Timestamps and Annotations
```bash
# Use asciinema with custom settings
asciinema rec --title "Bob AI Demo" --idle-time-limit 2 bob_demo.cast
```

### 3. Split Recording into Segments
```bash
# Record different scenarios separately
asciinema rec scenario1_setup.cast
asciinema rec scenario2_execution.cast
asciinema rec scenario3_analysis.cast
```

---

## Troubleshooting

### Common Issues

**Issue**: Python not found
```bash
# Solution: Check Python installation
python --version
# or
python3 --version

# Add Python to PATH if needed
```

**Issue**: Module import errors
```bash
# Solution: Ensure you're in the correct directory
cd d:/IBM/repopilot/sample_repo
python main.py
```

**Issue**: Recording tool not working
```bash
# Solution: Install alternative tool
pip install asciinema
# or use built-in Windows Terminal
```

---

## Best Practices for Recording

1. **Clear Terminal**: Start with a clean terminal window
   ```bash
   cls  # Windows
   clear  # Linux/macOS
   ```

2. **Set Terminal Size**: Use consistent terminal dimensions
   ```bash
   # Recommended: 120x30 or 100x30
   ```

3. **Add Pauses**: Give viewers time to read output
   ```bash
   timeout /t 3  # Windows (3 seconds)
   sleep 3  # Linux/macOS
   ```

4. **Use Comments**: Explain what you're doing
   ```bash
   echo "Now testing the calculator functions..."
   ```

5. **Show Errors**: Demonstrate error handling
   ```python
   try:
       divide(10, 0)
   except ValueError as e:
       print(f"Expected error: {e}")
   ```

---

## Recording Checklist

- [ ] Install recording tool (asciinema/OBS)
- [ ] Navigate to project directory
- [ ] Start recording
- [ ] Show project structure
- [ ] Run sample application
- [ ] Demonstrate calculator functions
- [ ] View generated documentation
- [ ] View generated tests
- [ ] Perform code analysis
- [ ] Show Bob's capabilities
- [ ] Stop recording
- [ ] Save/upload recording

---

## Additional Resources

- **asciinema**: https://asciinema.org/
- **OBS Studio**: https://obsproject.com/
- **Terminalizer**: https://terminalizer.com/
- **Windows Terminal**: https://aka.ms/terminal

---

**Created**: 2026-05-17  
**Version**: 1.0  
**Team**: MOMO PANDA

*This demonstration guide showcases IBM Bob's capabilities in analyzing, documenting, and testing code repositories.*