# RepoPilot Architecture Overview

## Project Vision

RepoPilot is an AI-powered repository analysis tool designed to automatically generate comprehensive documentation and tests for code repositories. The project aims to streamline the development workflow by:

- **Automating Documentation**: Generate clear, structured documentation from code analysis
- **Test Generation**: Create comprehensive test suites based on code structure and logic
- **Repository Intelligence**: Provide insights into code quality, structure, and patterns
- **Developer Productivity**: Reduce manual documentation burden and improve code maintainability

## Current Implementation Status

**Project Phase**: Initial Setup (0% Core Implementation)

RepoPilot is currently in its early-stage development phase with the following status:

- [x] Project structure established
- [x] Sample repository created for testing
- [x] Placeholder directories configured
- [ ] Core AI analysis engine (not implemented)
- [ ] Documentation generation system (not implemented)
- [ ] Test generation system (not implemented)
- [ ] Dependency management (not configured)

## Directory Structure

```
repopilot/
│
├── src/                    # Core application source code (empty - awaiting implementation)
│   ├── analyzer/          # (Planned) Code analysis modules
│   ├── generator/         # (Planned) Documentation and test generators
│   ├── ai/                # (Planned) AI integration layer
│   └── utils/             # (Planned) Utility functions and helpers
│
├── sample_repo/           # Demo repository for testing RepoPilot features
│   ├── calculator.py      # Sample Python module with basic math operations
│   └── main.py            # Sample entry point demonstrating calculator usage
│
├── generated_docs/        # Output directory for auto-generated documentation
│   └── (Documentation files will be created here)
│
├── generated_tests/       # Output directory for auto-generated test files
│   └── (Test files will be created here)
│
└── bob_sessions/          # Session storage for AI interactions and analysis history
    └── (Session data will be stored here)
```

## Directory Purpose Breakdown

### `/src/` - Core Application Code
**Status**: Empty (Implementation Pending)

This directory will contain the main application logic:

- **analyzer/**: Code parsing, AST analysis, and repository scanning
- **generator/**: Template engines for documentation and test generation
- **ai/**: Integration with AI models for intelligent analysis
- **utils/**: Common utilities, configuration management, logging

### `/sample_repo/` - Test Repository
**Status**: Active

Contains sample Python code used to test and demonstrate RepoPilot's capabilities:

**calculator.py** - A simple calculator module with four operations:
```python
def add(a, b)        # Addition
def subtract(a, b)   # Subtraction
def multiply(a, b)   # Multiplication
def divide(a, b)     # Division with zero-check
```

**main.py** - Entry point demonstrating calculator usage:
```python
from calculator import add, subtract

def main():
    # Demonstrates basic calculator operations
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 5 = {subtract(10, 5)}")
```

### `/generated_docs/` - Documentation Output
**Status**: Active (Manual docs present)

Repository for all auto-generated documentation files. Currently contains:
- `architecture_overview.md` - This document
- `getting_started.md` - Contributor onboarding guide

Future outputs will include:
- API documentation
- Module-level documentation
- Function/class documentation
- Architecture diagrams

### `/generated_tests/` - Test Output
**Status**: Placeholder

Will contain auto-generated test files including:
- Unit tests
- Integration tests
- Test fixtures
- Coverage reports

### `/bob_sessions/` - Session Management
**Status**: Placeholder

Stores AI interaction sessions and analysis history for:
- Conversation context
- Analysis results caching
- User preferences
- Session recovery

## Technical Stack

### Core Technologies
- **Language**: Python 3.8+
- **AI Integration**: (To be determined - OpenAI API, local models, etc.)
- **Code Analysis**: AST (Abstract Syntax Tree) parsing
- **Documentation Format**: Markdown

### Planned Dependencies
- **Code Analysis**: `ast`, `inspect`, `tokenize`
- **AI Integration**: TBD (OpenAI, Anthropic, or local LLM)
- **Testing**: `pytest`, `unittest`
- **Documentation**: `markdown`, `jinja2` (for templates)
- **Utilities**: `pathlib`, `json`, `yaml`

## Planned Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    RepoPilot Workflow                        │
└─────────────────────────────────────────────────────────────┘

1. Repository Input
   │
   ├─→ User provides repository path or URL
   │
   ↓
2. Code Analysis
   │
   ├─→ Parse Python files using AST
   ├─→ Extract functions, classes, modules
   ├─→ Analyze dependencies and imports
   ├─→ Identify code patterns and structure
   │
   ↓
3. AI Processing
   │
   ├─→ Send code context to AI model
   ├─→ Generate documentation descriptions
   ├─→ Create test scenarios
   ├─→ Identify edge cases
   │
   ↓
4. Content Generation
   │
   ├─→ Format documentation in Markdown
   ├─→ Generate test files with pytest
   ├─→ Create README and API docs
   │
   ↓
5. Output
   │
   ├─→ Save to generated_docs/
   ├─→ Save to generated_tests/
   └─→ Provide summary report
```

## Architecture Design

### High-Level Architecture

```
┌──────────────────────────────────────────────────────────┐
│                     User Interface                        │
│                   (CLI / API / Web)                       │
└────────────────────┬─────────────────────────────────────┘
                     │
                     ↓
┌──────────────────────────────────────────────────────────┐
│                  Orchestration Layer                      │
│              (Workflow Management)                        │
└────────┬─────────────────────────┬───────────────────────┘
         │                         │
         ↓                         ↓
┌─────────────────┐       ┌─────────────────┐
│  Code Analyzer  │       │  AI Integration │
│                 │       │                 │
│ • AST Parser    │←─────→│ • Prompt Eng.   │
│ • File Scanner  │       │ • Model API     │
│ • Dependency    │       │ • Context Mgmt  │
│   Resolver      │       │                 │
└────────┬────────┘       └────────┬────────┘
         │                         │
         └────────┬────────────────┘
                  ↓
         ┌─────────────────┐
         │   Generators    │
         │                 │
         │ • Doc Generator │
         │ • Test Generator│
         │ • Template Eng. │
         └────────┬────────┘
                  │
                  ↓
         ┌─────────────────┐
         │  Output Manager │
         │                 │
         │ • File Writer   │
         │ • Formatter     │
         │ • Validator     │
         └─────────────────┘
```

### Component Responsibilities

**Code Analyzer**
- Parse Python source files
- Build abstract syntax trees
- Extract code metadata (functions, classes, docstrings)
- Analyze code complexity and patterns

**AI Integration**
- Manage AI model connections
- Construct effective prompts
- Handle API rate limiting and errors
- Process AI responses

**Generators**
- Transform analysis results into documentation
- Create test cases from code structure
- Apply templates and formatting
- Ensure output quality

**Output Manager**
- Write files to appropriate directories
- Validate generated content
- Handle file conflicts
- Generate summary reports

## Planned Features

### Phase 1: Foundation (Current)
- [ ] Project structure setup
- [ ] Basic file I/O operations
- [ ] Configuration management
- [ ] Logging system

### Phase 2: Code Analysis
- [ ] Python AST parser
- [ ] Function/class extraction
- [ ] Dependency graph builder
- [ ] Code metrics calculator

### Phase 3: AI Integration
- [ ] AI model integration (OpenAI/Anthropic)
- [ ] Prompt engineering framework
- [ ] Context window management
- [ ] Response parsing

### Phase 4: Documentation Generation
- [ ] Markdown documentation generator
- [ ] API documentation templates
- [ ] README generator
- [ ] Architecture diagram generator

### Phase 5: Test Generation
- [ ] Unit test generator
- [ ] Test fixture creator
- [ ] Edge case identifier
- [ ] Coverage analyzer

### Phase 6: Advanced Features
- [ ] Multi-language support
- [ ] Custom template system
- [ ] Interactive mode
- [ ] CI/CD integration

## Sample Repository Analysis

The `sample_repo/` demonstrates the type of code RepoPilot will analyze:

**Input**: `calculator.py` and `main.py`

**Expected Output**:

1. **Documentation** (`generated_docs/calculator_api.md`):
   - Module overview
   - Function signatures and descriptions
   - Parameter documentation
   - Return value descriptions
   - Usage examples
   - Error handling notes

2. **Tests** (`generated_tests/test_calculator.py`):
   - Unit tests for each function
   - Edge case tests (e.g., divide by zero)
   - Integration tests
   - Parametrized test cases

## Future Enhancements

- **Multi-Repository Analysis**: Analyze entire organizations
- **Incremental Updates**: Update docs when code changes
- **Custom Styles**: Configurable documentation styles
- **Interactive Docs**: Generate interactive API explorers
- **Quality Metrics**: Code quality scoring and recommendations
- **Collaboration**: Team-based documentation workflows

## Contributing to Architecture

When contributing to RepoPilot's architecture:

1. **Maintain Modularity**: Keep components loosely coupled
2. **Follow SOLID Principles**: Especially Single Responsibility
3. **Document Decisions**: Update this file with architectural changes
4. **Consider Scalability**: Design for large repositories
5. **Prioritize Testability**: Make components easy to test

## Related Documentation

- [Getting Started Guide](./getting_started.md) - Setup and contribution guide
- [API Documentation](./api_docs.md) - (Coming soon)
- [Development Guide](./development.md) - (Coming soon)

---

**Last Updated**: 2026-05-17
**Version**: 0.1.0 (Initial Setup Phase)
**Status**: Under Active Development