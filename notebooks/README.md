# Jupyter Notebooks Directory

This directory contains Jupyter notebooks for interactive data analysis and exploration using the pandas-spss project.

## 📓 Available Notebooks

### `pandas_spss_demo.ipynb`
A demonstration notebook showcasing the project's core functionality:
- Sample data generation using pandas
- Data analysis and statistical summaries
- Data visualization with matplotlib and seaborn
- Interactive data exploration
- Export capabilities for analysis results

## 🚀 Getting Started

### Starting Jupyter

```bash
# Start Jupyter Lab (recommended)
task jupyter

# Start Jupyter Notebook (classic interface)
task jupyter-notebook

# Or use the convenience script
./scripts/start-jupyter.sh
```

### Accessing Project Functions

The notebooks have access to the project's source code. You can import functions directly:

```python
from main import create_sample_data, analyze_data

# Create sample data
df = create_sample_data()

# Analyze the data
results = analyze_data(df)
```

## 🔧 Features

- **Interactive Analysis**: Run code cells and see results immediately
- **Data Visualization**: Create charts and graphs with matplotlib and seaborn
- **Project Integration**: Direct access to project functions and modules
- **Export Capabilities**: Save analysis results, charts, and data

## 📊 Dependencies

The notebooks use the following packages (automatically installed with the project):
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `matplotlib` - Data visualization
- `seaborn` - Statistical data visualization
- `jupyter` - Notebook interface

## 🧪 Testing

Test the Jupyter environment:

```bash
# Test with tox
task jupyter-test

# Or directly
tox -e jupyter
```

## 💡 Tips

- The `src/` directory is automatically added to the Python path
- Use `%matplotlib inline` for inline plots
- Save your work frequently
- Use markdown cells for documentation and explanations
