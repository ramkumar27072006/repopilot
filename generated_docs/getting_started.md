# Getting Started with RepoPilot

Welcome to RepoPilot! This guide will help you get started as a first-time contributor to this exciting AI-powered repository analysis tool.

## Welcome Contributors!

RepoPilot is in its early stages, which means **you have a unique opportunity** to shape the project from the ground up! Whether you're interested in AI integration, code analysis, test generation, or documentation systems, there's a place for you here.

**What makes this special:**
- Ground-floor opportunity to influence architecture
- Learn about AI integration and code analysis
- Collaborative, beginner-friendly environment
- See your contributions make immediate impact

## Prerequisites

Before you begin, ensure you have the following installed:

### Required
- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
  ```bash
  # Check your Python version
  python --version
  # or
  python3 --version
  ```

- **Git** - [Download Git](https://git-scm.com/downloads)
  ```bash
  # Check your Git version
  git --version
  ```

### Recommended
- **Code Editor**: [Visual Studio Code](https://code.visualstudio.com/) with Python extension
- **Virtual Environment Tool**: `venv` (included with Python) or `virtualenv`
- **Package Manager**: `pip` (included with Python)

### Optional (for future development)
- **AI API Keys**: OpenAI, Anthropic, or other LLM providers
- **Testing Tools**: pytest, coverage
- **Documentation Tools**: Sphinx, MkDocs

## Quick Start

### 1. Clone the Repository

```bash
# Clone the repository
git clone https://github.com/yourusername/repopilot.git

# Navigate to the project directory
cd repopilot
```

### 2. Set Up Virtual Environment

Creating a virtual environment keeps your project dependencies isolated:

**On Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt when activated.

### 3. Install Dependencies (When Available)

Currently, RepoPilot has no dependencies configured. As the project develops:

```bash
# Install dependencies (once requirements.txt is created)
pip install -r requirements.txt

# Install in development mode (once setup.py is created)
pip install -e .
```

### 4. Verify Installation

Test the sample repository code to ensure everything works:

```bash
# Navigate to sample repository
cd sample_repo

# Run the sample application
python main.py
```

**Expected Output:**
```
Welcome to simple calc
2 + 3 = 5
10 - 5 = 5
```

If you see this output, you're all set!

## Project Structure Explained

Understanding the project structure is key to contributing effectively:

```
repopilot/
│
├── src/                          # Main application code (YOUR WORK GOES HERE!)
│   └── (Empty - awaiting implementation)
│
├── sample_repo/                  # Test repository for development
│   ├── calculator.py            # Sample module to analyze
│   └── main.py                  # Sample entry point
│
├── generated_docs/              # Auto-generated documentation output
│   ├── architecture_overview.md # Project architecture (READ THIS!)
│   └── getting_started.md       # This file
│
├── generated_tests/             # Auto-generated test output
│   └── (Test files will appear here)
│
└── bob_sessions/                # AI session storage
    └── (Session data stored here)
```

### Key Directories for Contributors

**`/src/`** - This is where you'll spend most of your time! Currently empty and waiting for:
- Code analysis modules
- AI integration layer
- Documentation generators
- Test generators
- Utility functions

**`/sample_repo/`** - Use this to test your implementations:
- Contains simple Python code
- Perfect for testing analysis features
- Add more sample files as needed

**`/generated_docs/`** - Output directory for documentation:
- Your generators will write here
- Check this to verify output quality

**`/generated_tests/`** - Output directory for tests:
- Generated test files go here
- Validate test generation logic

## Where to Start Contributing

Since RepoPilot is in its initial phase, here are the best places to start:

### High-Priority Areas

#### 1. **Project Setup & Configuration**
**Difficulty**: Beginner  
**Impact**: High

Create essential project files:

```bash
# Create requirements.txt
touch requirements.txt
```

Add initial dependencies:
```txt
# requirements.txt
# Code Analysis
ast-comments>=1.0.0

# Testing
pytest>=7.0.0
pytest-cov>=4.0.0

# Utilities
pyyaml>=6.0
python-dotenv>=1.0.0

# Future: AI Integration
# openai>=1.0.0
# anthropic>=0.3.0
```

Create `setup.py`:
```python
from setuptools import setup, find_packages

setup(
    name="repopilot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add dependencies here
    ],
    python_requires=">=3.8",
)
```

#### 2. **Basic File Operations**
**Difficulty**: Beginner  
**Impact**: High

Create `src/utils/file_handler.py`:
```python
"""File handling utilities for RepoPilot."""
import os
from pathlib import Path
from typing import List

def read_file(filepath: str) -> str:
    """Read and return file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath: str, content: str) -> None:
    """Write content to file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def list_python_files(directory: str) -> List[Path]:
    """List all Python files in directory."""
    return list(Path(directory).rglob("*.py"))
```

#### 3. **Configuration Management**
**Difficulty**: Beginner  
**Impact**: Medium

Create `src/config.py`:
```python
"""Configuration management for RepoPilot."""
import os
from pathlib import Path

class Config:
    """Application configuration."""
    
    # Project paths
    ROOT_DIR = Path(__file__).parent.parent
    SRC_DIR = ROOT_DIR / "src"
    SAMPLE_REPO_DIR = ROOT_DIR / "sample_repo"
    GENERATED_DOCS_DIR = ROOT_DIR / "generated_docs"
    GENERATED_TESTS_DIR = ROOT_DIR / "generated_tests"
    
    # AI Configuration (for future use)
    AI_MODEL = os.getenv("AI_MODEL", "gpt-4")
    AI_API_KEY = os.getenv("AI_API_KEY", "")
    
    # Generation settings
    MAX_FILE_SIZE = 1024 * 1024  # 1MB
    SUPPORTED_LANGUAGES = ["python"]
```

#### 4. **Code Analysis Foundation**
**Difficulty**: Intermediate  
**Impact**: High

Create `src/analyzer/python_analyzer.py`:
```python
"""Python code analyzer using AST."""
import ast
from typing import List, Dict, Any

class PythonAnalyzer:
    """Analyze Python source code."""
    
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.tree = ast.parse(source_code)
    
    def extract_functions(self) -> List[Dict[str, Any]]:
        """Extract all function definitions."""
        functions = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                functions.append({
                    'name': node.name,
                    'args': [arg.arg for arg in node.args.args],
                    'lineno': node.lineno,
                    'docstring': ast.get_docstring(node)
                })
        return functions
    
    def extract_classes(self) -> List[Dict[str, Any]]:
        """Extract all class definitions."""
        classes = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                classes.append({
                    'name': node.name,
                    'lineno': node.lineno,
                    'docstring': ast.get_docstring(node),
                    'methods': [m.name for m in node.body 
                               if isinstance(m, ast.FunctionDef)]
                })
        return classes
```

### Creative Opportunities

#### 5. **Documentation Templates**
**Difficulty**: Beginner  
**Impact**: Medium

Create markdown templates in `src/generator/templates/`:
- `function_doc.md` - Template for function documentation
- `class_doc.md` - Template for class documentation
- `module_doc.md` - Template for module documentation

#### 6. **Test Generation Logic**
**Difficulty**: Intermediate  
**Impact**: High

Design test generation strategies:
- Unit test templates
- Edge case identification
- Fixture generation

### Advanced Contributions

#### 7. **AI Integration**
**Difficulty**: Advanced  
**Impact**: Very High

Implement AI model integration:
- OpenAI API wrapper
- Prompt engineering
- Response parsing
- Error handling

#### 8. **CLI Interface**
**Difficulty**: Intermediate  
**Impact**: High

Create command-line interface using `argparse` or `click`:
```bash
repopilot analyze ./my_repo
repopilot generate-docs ./my_repo
repopilot generate-tests ./my_repo
```

## Development Workflow

### 1. Create a Feature Branch

```bash
# Create and switch to a new branch
git checkout -b feature/your-feature-name

# Examples:
git checkout -b feature/add-python-analyzer
git checkout -b feature/setup-configuration
git checkout -b fix/file-handling-bug
```

### 2. Make Your Changes

- Write clean, readable code
- Follow Python conventions (PEP 8)
- Add docstrings to functions and classes
- Keep functions small and focused

### 3. Test Your Changes

```bash
# Run the sample code to verify
cd sample_repo
python main.py

# Once pytest is set up:
pytest tests/
```

### 4. Commit Your Changes

```bash
# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "Add Python AST analyzer for function extraction"

# Push to your fork
git push origin feature/your-feature-name
```

### 5. Create a Pull Request

- Go to GitHub and create a Pull Request
- Describe what you've implemented
- Reference any related issues
- Wait for review and feedback

## Coding Standards

### Python Style Guide

Follow [PEP 8](https://pep8.org/) conventions:

```python
# Good: Clear function names, type hints, docstrings
def extract_function_names(source_code: str) -> List[str]:
    """
    Extract all function names from Python source code.
    
    Args:
        source_code: Python source code as string
        
    Returns:
        List of function names found in the code
    """
    tree = ast.parse(source_code)
    return [node.name for node in ast.walk(tree) 
            if isinstance(node, ast.FunctionDef)]

# Bad: Unclear names, no documentation
def get_funcs(code):
    t = ast.parse(code)
    return [n.name for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]
```

### Best Practices

1. **Use Type Hints**
   ```python
   def process_file(filepath: str) -> Dict[str, Any]:
       pass
   ```

2. **Write Docstrings**
   ```python
   def analyze_code(source: str) -> dict:
       """
       Analyze Python source code and extract metadata.
       
       Args:
           source: Python source code as string
           
       Returns:
           Dictionary containing analysis results
           
       Raises:
           SyntaxError: If source code is invalid
       """
       pass
   ```

3. **Handle Errors Gracefully**
   ```python
   try:
       result = analyze_code(source)
   except SyntaxError as e:
       logger.error(f"Failed to parse code: {e}")
       return None
   ```

4. **Keep Functions Small**
   - One function = one responsibility
   - Aim for < 20 lines per function
   - Extract complex logic into helper functions

5. **Use Meaningful Names**
   ```python
   # Good
   def extract_function_signatures(source_code: str) -> List[str]:
       pass
   
   # Bad
   def get_stuff(s: str) -> List[str]:
       pass
   ```

## Testing Approach

### Writing Tests

Once pytest is configured, follow this structure:

```python
# tests/test_analyzer.py
import pytest
from src.analyzer.python_analyzer import PythonAnalyzer

def test_extract_functions():
    """Test function extraction from simple code."""
    source = """
def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b
"""
    analyzer = PythonAnalyzer(source)
    functions = analyzer.extract_functions()
    
    assert len(functions) == 2
    assert functions[0]['name'] == 'add'
    assert functions[1]['name'] == 'subtract'

def test_extract_functions_with_docstring():
    """Test function extraction includes docstrings."""
    source = '''
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"
'''
    analyzer = PythonAnalyzer(source)
    functions = analyzer.extract_functions()
    
    assert functions[0]['docstring'] == "Return a greeting message."
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_analyzer.py

# Run with verbose output
pytest -v
```

## Adding Dependencies

When you need to add a new dependency:

1. **Install it locally**
   ```bash
   pip install package-name
   ```

2. **Add to requirements.txt**
   ```bash
   pip freeze | grep package-name >> requirements.txt
   ```

3. **Document why it's needed**
   ```txt
   # requirements.txt
   
   # Code Analysis
   ast-comments>=1.0.0  # Enhanced AST parsing with comment support
   
   # Your new dependency
   package-name>=1.0.0  # Brief explanation of why we need this
   ```

4. **Update setup.py if needed**

## Debugging Tips

### Common Issues

**Issue**: Import errors when running code
```bash
# Solution: Install in development mode
pip install -e .
```

**Issue**: Python version mismatch
```bash
# Solution: Check and use correct Python version
python --version
# Use python3 if needed
python3 main.py
```

**Issue**: Virtual environment not activated
```bash
# Solution: Activate it
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### Debugging Tools

```python
# Use print statements for quick debugging
print(f"Debug: functions = {functions}")

# Use pdb for interactive debugging
import pdb; pdb.set_trace()

# Use logging for production code
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug(f"Processing file: {filepath}")
```

## Getting Help

### Resources

- **Architecture Overview**: Read [architecture_overview.md](./architecture_overview.md) for project structure
- **Python Documentation**: [docs.python.org](https://docs.python.org/)
- **AST Module**: [Python AST docs](https://docs.python.org/3/library/ast.html)
- **pytest**: [pytest documentation](https://docs.pytest.org/)

### Communication

- **GitHub Issues**: Report bugs or suggest features
- **Pull Requests**: Submit your contributions
- **Discussions**: Ask questions and share ideas

### Questions to Ask

When stuck, consider:
1. Have I read the architecture overview?
2. Have I checked existing code for examples?
3. Have I searched for similar issues on GitHub?
4. Can I break this problem into smaller steps?

## Learning Path

### For Beginners

1. **Week 1**: Set up environment, explore sample_repo
2. **Week 2**: Create configuration and file utilities
3. **Week 3**: Learn Python AST basics
4. **Week 4**: Implement simple code analyzer

### For Intermediate Developers

1. **Week 1**: Implement core analyzer module
2. **Week 2**: Create documentation generator
3. **Week 3**: Build test generator
4. **Week 4**: Integrate components

### For Advanced Developers

1. **Week 1**: Design AI integration architecture
2. **Week 2**: Implement AI model wrapper
3. **Week 3**: Create prompt engineering system
4. **Week 4**: Build end-to-end pipeline

## Contribution Checklist

Before submitting a pull request:

- [ ] Code follows PEP 8 style guidelines
- [ ] All functions have docstrings
- [ ] Type hints are used where appropriate
- [ ] Code is tested (manually or with pytest)
- [ ] No unnecessary dependencies added
- [ ] Commit messages are clear and descriptive
- [ ] Branch is up to date with main
- [ ] Documentation is updated if needed

## Your First Contribution

Ready to make your first contribution? Here's a simple starter task:

**Task**: Create a basic logger utility

1. Create `src/utils/logger.py`
2. Implement a simple logging configuration
3. Add docstrings and type hints
4. Test it by logging messages
5. Submit a pull request!

```python
# src/utils/logger.py
"""Logging utilities for RepoPilot."""
import logging
from pathlib import Path

def setup_logger(name: str, log_file: str = None, level: int = logging.INFO) -> logging.Logger:
    """
    Set up a logger with console and optional file output.
    
    Args:
        name: Logger name
        log_file: Optional log file path
        level: Logging level (default: INFO)
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (optional)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger
```

## Next Steps

1. **Read** the [Architecture Overview](./architecture_overview.md)
2. **Set up** your development environment
3. **Explore** the sample_repo code
4. **Choose** a contribution area from "Where to Start"
5. **Create** a feature branch
6. **Build** something awesome!
7. **Submit** your pull request

---

**Welcome aboard!** We're excited to have you contribute to RepoPilot. Every contribution, no matter how small, helps build something amazing. Don't hesitate to ask questions and learn as you go. Happy coding!

**Last Updated**: 2026-05-17  
**Version**: 0.1.0  
**Maintainers**: RepoPilot Team