#!/usr/bin/env python3
"""
Jupyter configuration for pandas-spss project.
This file helps set up the Jupyter environment with the correct Python path.
"""

import os
import sys
from pathlib import Path

# Add the src directory to Python path
project_root = Path(__file__).parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

# Set environment variables
os.environ['PYTHONPATH'] = str(src_path)

print(f"✅ Jupyter configuration loaded")
print(f"📁 Project root: {project_root}")
print(f"📁 Source path: {src_path}")
print(f"🐍 Python path includes: {src_path}")
