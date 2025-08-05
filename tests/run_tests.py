"""Test runner for PyExtractIt tests."""

import pytest
import sys
from pathlib import Path

if __name__ == "__main__":
    # Add the package directory to Python path
    package_dir = Path(__file__).parent.parent / "pyextractit"
    sys.path.insert(0, str(package_dir.parent))
    
    # Run pytest with coverage
    pytest_args = [
        "--cov=pyextractit",
        "--cov-report=term-missing",
        "--cov-report=html",
        "-v",
        str(Path(__file__).parent)
    ]
    
    sys.exit(pytest.main(pytest_args))
