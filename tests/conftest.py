"""Test configuration and fixtures for PyExtractIt tests."""

import tempfile
import zipfile
import tarfile
from pathlib import Path
from typing import Generator
import pytest

from pyextractit.models import ExtractionResult, FileMatch
from pyextractit.extractor import ExtractorConfig, RecursiveExtractor


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)


@pytest.fixture
def sample_config() -> ExtractorConfig:
    """Create a sample extractor configuration."""
    return ExtractorConfig(
        target_pattern=r".*\.txt$",
        prefix="test_",
        max_depth=5
    )


@pytest.fixture
def extractor(sample_config: ExtractorConfig) -> RecursiveExtractor:
    """Create a RecursiveExtractor instance."""
    return RecursiveExtractor(sample_config)


@pytest.fixture
def sample_files(temp_dir: Path) -> dict[str, Path]:
    """Create sample files for testing."""
    files = {}
    
    # Create some text files
    files['text1'] = temp_dir / "sample1.txt"
    files['text1'].write_text("This is sample text file 1", encoding='utf-8')
    
    files['text2'] = temp_dir / "sample2.txt"
    files['text2'].write_text("This is sample text file 2", encoding='utf-8')
    
    # Create a non-matching file
    files['image'] = temp_dir / "image.png"
    files['image'].write_bytes(b'\x89PNG\r\n\x1a\n')  # PNG header
    
    # Create a config file
    files['config'] = temp_dir / "config.json"
    files['config'].write_text('{"setting": "value"}', encoding='utf-8')
    
    return files


@pytest.fixture
def simple_zip(temp_dir: Path, sample_files: dict[str, Path]) -> Path:
    """Create a simple ZIP file for testing."""
    zip_path = temp_dir / "simple.zip"
    
    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        for file_path in sample_files.values():
            zip_file.write(file_path, file_path.name)
    
    return zip_path


@pytest.fixture
def nested_zip(temp_dir: Path, simple_zip: Path) -> Path:
    """Create a ZIP file containing another ZIP file."""
    nested_zip_path = temp_dir / "nested.zip"
    
    # Create some additional files
    extra_text = temp_dir / "extra.txt"
    extra_text.write_text("Extra text file", encoding='utf-8')
    
    with zipfile.ZipFile(nested_zip_path, 'w') as zip_file:
        # Add the simple zip
        zip_file.write(simple_zip, "inner.zip")
        # Add the extra file
        zip_file.write(extra_text, "extra.txt")
    
    return nested_zip_path


@pytest.fixture
def simple_tar(temp_dir: Path, sample_files: dict[str, Path]) -> Path:
    """Create a simple TAR file for testing."""
    tar_path = temp_dir / "simple.tar"
    
    with tarfile.open(tar_path, 'w') as tar_file:
        for file_path in sample_files.values():
            tar_file.add(file_path, arcname=file_path.name)
    
    return tar_path


@pytest.fixture
def tar_gz(temp_dir: Path, sample_files: dict[str, Path]) -> Path:
    """Create a TAR.GZ file for testing."""
    tar_gz_path = temp_dir / "compressed.tar.gz"
    
    with tarfile.open(tar_gz_path, 'w:gz') as tar_file:
        for file_path in sample_files.values():
            tar_file.add(file_path, arcname=file_path.name)
    
    return tar_gz_path


@pytest.fixture
def deeply_nested_archive(temp_dir: Path) -> Path:
    """Create a deeply nested archive structure for testing max depth."""
    current_path = temp_dir
    
    # Create the deepest file
    deep_file = current_path / "level5.txt"
    deep_file.write_text("Deep file content", encoding='utf-8')
    
    # Create nested zips from deep to shallow
    for level in range(5, 0, -1):
        zip_path = current_path / f"level{level}.zip"
        with zipfile.ZipFile(zip_path, 'w') as zip_file:
            if level == 5:
                zip_file.write(deep_file, "target.txt")
            else:
                inner_zip = current_path / f"level{level + 1}.zip"
                zip_file.write(inner_zip, f"level{level + 1}.zip")
    
    return current_path / "level1.zip"
