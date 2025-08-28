# pandas-spss

A Python project using pandas with `uv` package manager and Go task for environment management.

## 🚀 Quick Start

### Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) - Fast Python package installer and resolver
- [Go task](https://taskfile.dev/) - Task runner / build tool

### Installation

1. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install Go task** (if not already installed):
   ```bash
   # macOS
   brew install go-task
   
   # Or download from https://taskfile.dev/installation/
   ```

3. **Setup the project**:
   ```bash
   # Clone the repository
   git clone <your-repo-url>
   cd pandas-spss
   
   # Setup environment and install dependencies
   task setup
   ```

## 📋 Available Tasks

Use `task --list` to see all available tasks, or run individual tasks:

### Environment Management
- `task setup` - Setup the development environment with uv
- `task install` - Install dependencies using uv
- `task dev-install` - Install development dependencies
- `task shell` - Activate the virtual environment shell

### Development
- `task run` - Run the main application
- `task test` - Run tests with pytest
- `task lint` - Run linting with flake8
- `task format` - Format code with black
- `task type-check` - Run type checking with mypy
- `task check` - Run all checks (lint, type-check, test)

### Maintenance
- `task clean` - Clean up generated files

## 🐼 Project Structure

```
pandas-spss/
├── src/
│   ├── __init__.py
│   └── main.py          # Main application with pandas demo
├── tests/
│   ├── __init__.py
│   └── test_main.py     # Tests for main module
├── pyproject.toml       # Project configuration and dependencies
├── Taskfile.yml         # Go task configuration
└── README.md           # This file
```

## 🎯 Features

- **Fast dependency management** with `uv`
- **Automated environment setup** with Go task
- **Comprehensive testing** with pytest and tox
- **Multi-environment testing** with tox (Python 3.11, 3.12, 3.13)
- **Code quality tools**:
  - Black for code formatting
  - Flake8 for linting
  - MyPy for type checking
- **Sample pandas application** demonstrating data analysis

## 🧪 Running the Application

```bash
# Run the main application
task run

# Or directly with uv
uv run python src/main.py
```

The application will:
1. Create sample employee data
2. Perform data analysis
3. Display summary statistics
4. Save results to CSV

## 🧪 Running Tests

```bash
# Run all tests
task test

# Run with verbose output
uv run pytest tests/ -v

# Run specific test file
uv run pytest tests/test_main.py -v

# Run tests with tox (multiple Python versions)
tox

# Run specific tox environment
tox -e py313
tox -e lint
tox -e type-check

# Run tox with specific pytest arguments
tox -- pytest tests/ -v

# Or use the convenience script
./scripts/run-tox.sh py313
./scripts/run-tox.sh lint
./scripts/run-tox.sh type-check
```

## 🔧 Development Workflow

1. **Start development**:
   ```bash
   task dev-install  # Install dev dependencies
   task shell        # Activate virtual environment
   ```

2. **Make changes** to your code

3. **Check code quality**:
   ```bash
   task check        # Run all checks
   # Or individually:
   task format       # Format code
   task lint         # Check for issues
   task type-check   # Type checking
   task test         # Run tests
   ```

4. **Commit your changes**

## 🧪 Testing with Tox

Tox provides multi-environment testing capabilities:

### Available Environments
- `py311`, `py312`, `py313` - Test against different Python versions
- `lint` - Run code linting (black + flake8)
- `type-check` - Run type checking with mypy

### Usage
```bash
# Run all environments
task tox

# Run specific environment
task tox-lint
task tox-type-check

# Run with tox directly
tox -e py313
tox -e lint
tox -e type-check

# Run with custom arguments
tox -e py313 -- pytest tests/ -v
```

### Benefits
- **Multi-version testing**: Ensures compatibility across Python versions
- **Isolated environments**: Each test runs in a clean virtual environment
- **CI/CD ready**: Perfect for automated testing pipelines
- **Consistent results**: Same environment setup across different machines

## 📦 Dependencies

### Main Dependencies
- `pandas>=2.0.0` - Data manipulation and analysis
- `numpy>=1.24.0` - Numerical computing

### Development Dependencies
- `pytest>=7.0.0` - Testing framework
- `black>=23.0.0` - Code formatter
- `flake8>=6.0.0` - Linter
- `mypy>=1.0.0` - Type checker
- `tox>=4.0.0` - Multi-environment testing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `task check` to ensure code quality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

**uv not found**: Make sure uv is installed and in your PATH
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**task not found**: Install Go task
```bash
# macOS
brew install go-task

# Or download from https://taskfile.dev/installation/
```

**Permission denied**: Make sure the virtual environment directory is writable
```bash
task clean
task setup
```

### Getting Help

- Check the [uv documentation](https://docs.astral.sh/uv/)
- Check the [Go task documentation](https://taskfile.dev/)
- Open an issue in the repository
