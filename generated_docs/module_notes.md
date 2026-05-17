# RepoPilot Module Documentation

This document provides comprehensive module-level documentation for the RepoPilot project, including detailed API references, code structure guidelines, and examples of module interactions.

---

## Table of Contents

1. [Overview](#overview)
2. [Sample Repository Documentation](#sample-repository-documentation)
3. [Planned Modules](#planned-modules)
4. [Code Structure Guidelines](#code-structure-guidelines)
5. [API Documentation Format](#api-documentation-format)
6. [Module Interaction Examples](#module-interaction-examples)

---

## Overview

RepoPilot is organized into distinct modules, each with specific responsibilities. This modular architecture ensures maintainability, testability, and scalability as the project grows.

### Module Organization Principles

- **Separation of Concerns**: Each module handles a specific aspect of functionality
- **Loose Coupling**: Modules interact through well-defined interfaces
- **High Cohesion**: Related functionality is grouped together
- **Testability**: Modules are designed to be easily testable in isolation

---

## Sample Repository Documentation

The `sample_repo/` directory contains demonstration code used for testing RepoPilot's analysis and generation capabilities.

### Module: calculator.py

**Purpose**: Provides basic arithmetic operations for demonstration and testing.

**Location**: `repopilot/sample_repo/calculator.py`

**Module Type**: Utility Module

#### Functions

##### `add(a, b)`

Performs addition of two numbers.

**Signature**:
```python
def add(a, b)
```

**Parameters**:
- `a` (int | float): The first number to add
- `b` (int | float): The second number to add

**Returns**:
- `int | float`: The sum of `a` and `b`

**Description**:
Adds two numbers together and returns the result. Supports both integer and floating-point arithmetic.

**Example Usage**:
```python
from calculator import add

result = add(5, 3)
print(result)  # Output: 8

result = add(2.5, 3.7)
print(result)  # Output: 6.2
```

**Edge Cases**:
- Works with negative numbers: `add(-5, 3)` returns `-2`
- Works with zero: `add(0, 5)` returns `5`
- Works with large numbers: `add(1000000, 2000000)` returns `3000000`

**Time Complexity**: O(1)

**Space Complexity**: O(1)

---

##### `subtract(a, b)`

Performs subtraction of two numbers.

**Signature**:
```python
def subtract(a, b)
```

**Parameters**:
- `a` (int | float): The number to subtract from (minuend)
- `b` (int | float): The number to subtract (subtrahend)

**Returns**:
- `int | float`: The difference between `a` and `b` (a - b)

**Description**:
Subtracts the second number from the first and returns the result. Supports both integer and floating-point arithmetic.

**Example Usage**:
```python
from calculator import subtract

result = subtract(10, 3)
print(result)  # Output: 7

result = subtract(5.5, 2.3)
print(result)  # Output: 3.2
```

**Edge Cases**:
- Works with negative results: `subtract(3, 5)` returns `-2`
- Works with negative numbers: `subtract(-5, -3)` returns `-2`
- Works with zero: `subtract(5, 0)` returns `5`

**Time Complexity**: O(1)

**Space Complexity**: O(1)

---

##### `multiply(a, b)`

Performs multiplication of two numbers.

**Signature**:
```python
def multiply(a, b)
```

**Parameters**:
- `a` (int | float): The first number to multiply
- `b` (int | float): The second number to multiply

**Returns**:
- `int | float`: The product of `a` and `b`

**Description**:
Multiplies two numbers together and returns the result. Supports both integer and floating-point arithmetic.

**Example Usage**:
```python
from calculator import multiply

result = multiply(4, 5)
print(result)  # Output: 20

result = multiply(2.5, 4)
print(result)  # Output: 10.0
```

**Edge Cases**:
- Multiplication by zero: `multiply(5, 0)` returns `0`
- Multiplication by one: `multiply(5, 1)` returns `5`
- Negative numbers: `multiply(-3, 4)` returns `-12`
- Two negatives: `multiply(-3, -4)` returns `12`

**Time Complexity**: O(1)

**Space Complexity**: O(1)

---

##### `divide(a, b)`

Performs division of two numbers with zero-check validation.

**Signature**:
```python
def divide(a, b)
```

**Parameters**:
- `a` (int | float): The dividend (number to be divided)
- `b` (int | float): The divisor (number to divide by)

**Returns**:
- `float`: The quotient of `a` divided by `b`

**Raises**:
- `ValueError`: If `b` is zero (division by zero is not allowed)

**Description**:
Divides the first number by the second and returns the result. Includes validation to prevent division by zero, which would cause a runtime error.

**Example Usage**:
```python
from calculator import divide

result = divide(10, 2)
print(result)  # Output: 5.0

result = divide(7, 2)
print(result)  # Output: 3.5
```

**Error Handling**:
```python
try:
    result = divide(10, 0)
except ValueError as e:
    print(e)  # Output: Cannot divide by zero
```

**Edge Cases**:
- Division by zero: Raises `ValueError` with message "Cannot divide by zero"
- Division by one: `divide(5, 1)` returns `5.0`
- Division of zero: `divide(0, 5)` returns `0.0`
- Negative numbers: `divide(-10, 2)` returns `-5.0`
- Two negatives: `divide(-10, -2)` returns `5.0`

**Time Complexity**: O(1)

**Space Complexity**: O(1)

---

### Module: main.py

**Purpose**: Entry point for the sample calculator application, demonstrating usage of calculator functions.

**Location**: `repopilot/sample_repo/main.py`

**Module Type**: Application Entry Point

#### Functions

##### `main()`

Main entry point that demonstrates calculator functionality.

**Signature**:
```python
def main()
```

**Parameters**: None

**Returns**: None

**Description**:
Demonstrates the usage of calculator functions by performing sample arithmetic operations and printing the results to the console. This function serves as an example of how to use the calculator module.

**Example Usage**:
```python
if __name__ == "__main__":
    main()
```

**Output**:
```
Welcome to simple calc
2 + 3 = 5
10 - 5 = 5
```

**Implementation Details**:
- Imports `add` and `subtract` functions from the calculator module
- Prints a welcome message
- Demonstrates addition: 2 + 3
- Demonstrates subtraction: 10 - 5
- Uses f-strings for formatted output

**Dependencies**:
- `calculator.add`: For addition operation
- `calculator.subtract`: For subtraction operation

**Time Complexity**: O(1)

**Space Complexity**: O(1)

---

## Planned Modules

The following modules are planned for implementation in the `src/` directory.

### Module: src/analyzer/

**Purpose**: Code analysis and parsing functionality.

#### Planned Components

##### `python_analyzer.py`

**Purpose**: Analyze Python source code using Abstract Syntax Tree (AST) parsing.

**Planned Classes**:

**`PythonAnalyzer`**
- **Purpose**: Parse and extract metadata from Python source code
- **Methods**:
  - `__init__(source_code: str)`: Initialize with source code
  - `extract_functions() -> List[Dict[str, Any]]`: Extract all function definitions
  - `extract_classes() -> List[Dict[str, Any]]`: Extract all class definitions
  - `extract_imports() -> List[str]`: Extract import statements
  - `calculate_complexity() -> int`: Calculate cyclomatic complexity
  - `get_docstrings() -> Dict[str, str]`: Extract all docstrings

**Example Usage**:
```python
from src.analyzer.python_analyzer import PythonAnalyzer

source = """
def greet(name):
    '''Return a greeting message.'''
    return f"Hello, {name}!"
"""

analyzer = PythonAnalyzer(source)
functions = analyzer.extract_functions()
print(functions)
# Output: [{'name': 'greet', 'args': ['name'], 'lineno': 2, 'docstring': 'Return a greeting message.'}]
```

##### `file_scanner.py`

**Purpose**: Scan directories and identify code files for analysis.

**Planned Functions**:
- `scan_directory(path: str, recursive: bool = True) -> List[Path]`: Scan directory for Python files
- `filter_by_extension(files: List[Path], extensions: List[str]) -> List[Path]`: Filter files by extension
- `get_file_metadata(filepath: Path) -> Dict[str, Any]`: Get file size, modification time, etc.

##### `dependency_resolver.py`

**Purpose**: Analyze and resolve code dependencies.

**Planned Functions**:
- `extract_dependencies(source_code: str) -> List[str]`: Extract all dependencies
- `build_dependency_graph(files: List[Path]) -> Dict[str, List[str]]`: Build dependency graph
- `detect_circular_dependencies(graph: Dict) -> List[Tuple[str, str]]`: Detect circular imports

---

### Module: src/generator/

**Purpose**: Generate documentation and test files from analyzed code.

#### Planned Components

##### `doc_generator.py`

**Purpose**: Generate Markdown documentation from code analysis results.

**Planned Classes**:

**`DocumentationGenerator`**
- **Purpose**: Transform code metadata into formatted documentation
- **Methods**:
  - `__init__(template_dir: str)`: Initialize with template directory
  - `generate_function_doc(func_data: Dict) -> str`: Generate function documentation
  - `generate_class_doc(class_data: Dict) -> str`: Generate class documentation
  - `generate_module_doc(module_data: Dict) -> str`: Generate module documentation
  - `save_documentation(content: str, output_path: str)`: Save to file

**Example Usage**:
```python
from src.generator.doc_generator import DocumentationGenerator

generator = DocumentationGenerator(template_dir="templates/")
func_data = {
    'name': 'add',
    'args': ['a', 'b'],
    'docstring': 'Add two numbers',
    'returns': 'int'
}
doc = generator.generate_function_doc(func_data)
generator.save_documentation(doc, "generated_docs/add.md")
```

##### `test_generator.py`

**Purpose**: Generate test files from code analysis.

**Planned Classes**:

**`TestGenerator`**
- **Purpose**: Create pytest test cases from code structure
- **Methods**:
  - `__init__(test_framework: str = "pytest")`: Initialize with test framework
  - `generate_unit_tests(func_data: Dict) -> str`: Generate unit tests
  - `generate_edge_case_tests(func_data: Dict) -> str`: Generate edge case tests
  - `generate_fixtures(class_data: Dict) -> str`: Generate test fixtures
  - `save_tests(content: str, output_path: str)`: Save test file

##### `template_engine.py`

**Purpose**: Template management and rendering.

**Planned Functions**:
- `load_template(template_name: str) -> str`: Load template from file
- `render_template(template: str, context: Dict) -> str`: Render template with context
- `register_custom_filter(name: str, func: Callable)`: Register custom Jinja2 filter

---

### Module: src/ai/

**Purpose**: AI model integration and prompt management.

#### Planned Components

##### `model_client.py`

**Purpose**: Interface with AI models (OpenAI, Anthropic, etc.).

**Planned Classes**:

**`AIModelClient`**
- **Purpose**: Manage AI model connections and requests
- **Methods**:
  - `__init__(api_key: str, model: str)`: Initialize with API credentials
  - `send_prompt(prompt: str, max_tokens: int) -> str`: Send prompt to AI
  - `analyze_code(source_code: str) -> Dict`: Get AI analysis of code
  - `generate_documentation(code_metadata: Dict) -> str`: Generate docs with AI
  - `suggest_tests(func_data: Dict) -> List[str]`: Get test suggestions

##### `prompt_builder.py`

**Purpose**: Construct effective prompts for AI models.

**Planned Functions**:
- `build_analysis_prompt(source_code: str) -> str`: Create code analysis prompt
- `build_documentation_prompt(metadata: Dict) -> str`: Create documentation prompt
- `build_test_prompt(func_data: Dict) -> str`: Create test generation prompt
- `add_context(prompt: str, context: Dict) -> str`: Add context to prompt

##### `response_parser.py`

**Purpose**: Parse and validate AI model responses.

**Planned Functions**:
- `parse_json_response(response: str) -> Dict`: Parse JSON from response
- `extract_code_blocks(response: str) -> List[str]`: Extract code blocks
- `validate_response(response: str, schema: Dict) -> bool`: Validate response format

---

### Module: src/utils/

**Purpose**: Utility functions and helpers used across the application.

#### Planned Components

##### `file_handler.py`

**Purpose**: File I/O operations.

**Planned Functions**:
- `read_file(filepath: str) -> str`: Read file contents
- `write_file(filepath: str, content: str)`: Write content to file
- `list_python_files(directory: str) -> List[Path]`: List Python files
- `ensure_directory(path: str)`: Create directory if it doesn't exist

##### `config.py`

**Purpose**: Application configuration management.

**Planned Classes**:

**`Config`**
- **Purpose**: Centralized configuration management
- **Attributes**:
  - `ROOT_DIR`: Project root directory
  - `SRC_DIR`: Source code directory
  - `GENERATED_DOCS_DIR`: Documentation output directory
  - `GENERATED_TESTS_DIR`: Test output directory
  - `AI_MODEL`: AI model to use
  - `AI_API_KEY`: API key for AI service
  - `MAX_FILE_SIZE`: Maximum file size to process
  - `SUPPORTED_LANGUAGES`: List of supported languages

##### `logger.py`

**Purpose**: Logging configuration and utilities.

**Planned Functions**:
- `setup_logger(name: str, log_file: str = None) -> logging.Logger`: Configure logger
- `log_analysis_start(filepath: str)`: Log analysis start
- `log_generation_complete(output_path: str)`: Log generation completion
- `log_error(error: Exception, context: str)`: Log errors with context

---

## Code Structure Guidelines

### Module Organization

Each module should follow this structure:

```python
"""
Module docstring explaining purpose and usage.

Example:
    from module_name import function_name
    result = function_name(args)
"""

# Standard library imports
import os
import sys
from typing import List, Dict, Any

# Third-party imports
import requests
from jinja2 import Template

# Local imports
from src.utils.logger import setup_logger

# Module-level constants
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

# Module-level variables
logger = setup_logger(__name__)


class ClassName:
    """Class docstring with description and examples."""
    
    def __init__(self, param: str):
        """Initialize with parameters."""
        self.param = param
    
    def method_name(self, arg: int) -> str:
        """Method docstring with description."""
        pass


def function_name(param: str) -> Dict[str, Any]:
    """
    Function docstring with full description.
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When parameter is invalid
        
    Example:
        >>> result = function_name("test")
        >>> print(result)
        {'status': 'success'}
    """
    pass
```

### Naming Conventions

- **Modules**: lowercase with underscores (`file_handler.py`)
- **Classes**: PascalCase (`DocumentationGenerator`)
- **Functions**: lowercase with underscores (`extract_functions`)
- **Constants**: UPPERCASE with underscores (`MAX_FILE_SIZE`)
- **Private functions**: prefix with underscore (`_internal_helper`)

### Documentation Standards

Every module, class, and function must include:

1. **Docstring**: Clear description of purpose
2. **Parameters**: Type hints and descriptions
3. **Returns**: Type hint and description
4. **Raises**: List of exceptions that may be raised
5. **Examples**: Usage examples where appropriate

---

## API Documentation Format

### Function Documentation Template

```markdown
##### `function_name(param1, param2)`

Brief one-line description.

**Signature**:
```python
def function_name(param1: Type1, param2: Type2) -> ReturnType:
```

**Parameters**:
- `param1` (Type1): Description of first parameter
- `param2` (Type2): Description of second parameter

**Returns**:
- `ReturnType`: Description of return value

**Raises**:
- `ExceptionType`: When this exception occurs

**Description**:
Detailed description of what the function does, how it works, and any important implementation details.

**Example Usage**:
```python
result = function_name(arg1, arg2)
print(result)
```

**Edge Cases**:
- Case 1: Description and behavior
- Case 2: Description and behavior

**Time Complexity**: O(n)
**Space Complexity**: O(1)
```

### Class Documentation Template

```markdown
##### `ClassName`

Brief description of the class purpose.

**Purpose**: Detailed explanation of what the class does.

**Attributes**:
- `attribute1` (Type): Description
- `attribute2` (Type): Description

**Methods**:
- `method1(args) -> ReturnType`: Brief description
- `method2(args) -> ReturnType`: Brief description

**Example Usage**:
```python
obj = ClassName(param1, param2)
result = obj.method1(arg)
```

**Design Patterns**: Singleton / Factory / Observer / etc.
```

---

## Module Interaction Examples

### Example 1: Complete Analysis Pipeline

```python
from src.analyzer.python_analyzer import PythonAnalyzer
from src.generator.doc_generator import DocumentationGenerator
from src.utils.file_handler import read_file, write_file

# Read source code
source_code = read_file("sample_repo/calculator.py")

# Analyze code
analyzer = PythonAnalyzer(source_code)
functions = analyzer.extract_functions()
classes = analyzer.extract_classes()

# Generate documentation
doc_generator = DocumentationGenerator(template_dir="templates/")
for func in functions:
    doc = doc_generator.generate_function_doc(func)
    output_path = f"generated_docs/{func['name']}.md"
    write_file(output_path, doc)
```

### Example 2: AI-Enhanced Documentation

```python
from src.analyzer.python_analyzer import PythonAnalyzer
from src.ai.model_client import AIModelClient
from src.ai.prompt_builder import build_documentation_prompt
from src.generator.doc_generator import DocumentationGenerator

# Analyze code
analyzer = PythonAnalyzer(source_code)
metadata = analyzer.extract_functions()[0]

# Get AI enhancement
ai_client = AIModelClient(api_key="...", model="gpt-4")
prompt = build_documentation_prompt(metadata)
ai_suggestions = ai_client.send_prompt(prompt)

# Generate enhanced documentation
metadata['ai_description'] = ai_suggestions
doc_generator = DocumentationGenerator()
doc = doc_generator.generate_function_doc(metadata)
```

### Example 3: Test Generation Workflow

```python
from src.analyzer.python_analyzer import PythonAnalyzer
from src.generator.test_generator import TestGenerator
from src.ai.model_client import AIModelClient

# Analyze code
analyzer = PythonAnalyzer(source_code)
functions = analyzer.extract_functions()

# Generate tests
test_generator = TestGenerator(test_framework="pytest")
ai_client = AIModelClient(api_key="...", model="gpt-4")

for func in functions:
    # Get AI test suggestions
    test_cases = ai_client.suggest_tests(func)
    
    # Generate test file
    tests = test_generator.generate_unit_tests(func)
    edge_tests = test_generator.generate_edge_case_tests(func)
    
    # Save tests
    output_path = f"generated_tests/test_{func['name']}.py"
    test_generator.save_tests(tests + edge_tests, output_path)
```

---

## Best Practices

### Module Design

1. **Single Responsibility**: Each module should have one clear purpose
2. **Minimal Dependencies**: Reduce coupling between modules
3. **Clear Interfaces**: Define clear public APIs
4. **Error Handling**: Handle errors gracefully with informative messages
5. **Logging**: Log important operations and errors

### Code Quality

1. **Type Hints**: Use type hints for all function parameters and returns
2. **Docstrings**: Document all public functions and classes
3. **Testing**: Write tests for all modules
4. **Code Review**: Review code before merging
5. **Performance**: Consider performance implications

### Documentation

1. **Keep Updated**: Update documentation when code changes
2. **Examples**: Provide clear usage examples
3. **Edge Cases**: Document edge cases and limitations
4. **API Stability**: Mark experimental APIs clearly

---

## Future Enhancements

### Planned Module Additions

1. **src/cli/**: Command-line interface module
2. **src/web/**: Web interface module (optional)
3. **src/plugins/**: Plugin system for extensibility
4. **src/cache/**: Caching layer for performance
5. **src/metrics/**: Code quality metrics module

### Integration Points

- **CI/CD**: GitHub Actions integration
- **IDE Plugins**: VS Code extension
- **API Server**: REST API for remote access
- **Database**: Store analysis results

---

**Last Updated**: 2026-05-17  
**Version**: 0.1.0  
**Maintained by**: Team MOMO PANDA