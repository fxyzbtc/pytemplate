#!/usr/bin/env python3
"""Create a nested sample archive with multiple compression layers."""

import zipfile
import tarfile
from pathlib import Path

def create_nested_archive():
    """Create a nested archive structure for testing."""
    
    # Step 1: Create the innermost TAR.GZ archive with our target files
    print('Creating innermost.tar.gz with foo.txt and bar.log...')
    with tarfile.open('innermost.tar.gz', 'w:gz') as tar:
        tar.add('foo.txt')
        tar.add('bar.log')
    
    # Step 2: Create a TAR archive containing the TAR.GZ
    print('Creating middle.tar containing innermost.tar.gz...')
    with tarfile.open('middle.tar', 'w') as tar:
        tar.add('innermost.tar.gz')
    
    # Step 3: Create a ZIP archive containing the TAR
    print('Creating nested_sample.zip containing middle.tar...')
    with zipfile.ZipFile('nested_sample.zip', 'w') as zip_file:
        zip_file.write('middle.tar')
    
    # Clean up intermediate files
    Path('innermost.tar.gz').unlink()
    Path('middle.tar').unlink()
    
    print('✅ Nested archive structure created!')
    print('📦 Structure: nested_sample.zip -> middle.tar -> innermost.tar.gz -> [foo.txt, bar.log]')
    print(f'📁 Final archive: {Path("nested_sample.zip").absolute()}')

if __name__ == "__main__":
    create_nested_archive()
