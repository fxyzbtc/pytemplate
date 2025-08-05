#!/usr/bin/env python3
"""Create nested archive fixtures for testing."""

import zipfile
import tarfile
from pathlib import Path

def create_nested_archive_fixture(temp_dir: Path) -> Path:
    """Create a nested archive structure for testing.
    
    Returns:
        Path to the created nested archive
    """
    fixtures_dir = Path(__file__).parent / "fixtures"
    
    # Copy fixture files to temp directory
    foo_file = temp_dir / "foo.txt"
    bar_file = temp_dir / "bar.log"
    
    foo_file.write_text((fixtures_dir / "foo.txt").read_text())
    bar_file.write_text((fixtures_dir / "bar.log").read_text())
    
    # Step 1: Create the innermost TAR.GZ archive with our target files
    innermost_path = temp_dir / 'innermost.tar.gz'
    with tarfile.open(innermost_path, 'w:gz') as tar:
        tar.add(foo_file, arcname="foo.txt")
        tar.add(bar_file, arcname="bar.log")
    
    # Step 2: Create a TAR archive containing the TAR.GZ
    middle_path = temp_dir / 'middle.tar'
    with tarfile.open(middle_path, 'w') as tar:
        tar.add(innermost_path, arcname="innermost.tar.gz")
    
    # Step 3: Create a ZIP archive containing the TAR
    nested_archive_path = temp_dir / 'nested_sample.zip'
    with zipfile.ZipFile(nested_archive_path, 'w') as zip_file:
        zip_file.write(middle_path, "middle.tar")
    
    # Clean up intermediate files
    innermost_path.unlink()
    middle_path.unlink()
    foo_file.unlink()
    bar_file.unlink()
    
    return nested_archive_path
