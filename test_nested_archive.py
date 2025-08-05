#!/usr/bin/env python3
"""Demo script showing nested archive extraction capabilities."""

import tempfile
from pathlib import Path
from pyextractit.extractor import ExtractorConfig, RecursiveExtractor
from tests.create_fixtures import create_nested_archive_fixture


def demo_nested_archive_extraction():
    """Demonstrate nested archive extraction with detailed output."""
    
    print('🧪 PyExtractIt Nested Archive Extraction Demo')
    print('=' * 50)
    print('📦 Archive Structure: nested_sample.zip -> middle.tar -> innermost.tar.gz -> [foo.txt, bar.log]')
    print()

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Create the nested archive fixture
        print('🔧 Creating nested archive fixture...')
        archive_path = create_nested_archive_fixture(temp_path)
        print(f'✅ Created: {archive_path.name}')
        print()

        # Demo 1: Extract .txt files with pattern display
        pattern1 = r'.*\.txt$'
        print('📋 Demo 1: Extract .txt files with sequential naming')
        print(f'🔍 Pattern: "{pattern1}" (matches filenames ending with .txt)')
        config1 = ExtractorConfig(
            target_pattern=pattern1,
            prefix='txt_',
            output_dir=temp_path / 'extracted_txt',
            unlimited_depth=True
        )

        extractor1 = RecursiveExtractor(config1)
        result1 = extractor1.extract_from_archive(archive_path)

        if result1.success:
            print(f'✅ Success! Found {len(result1.matched_files)} .txt files')
            for match in result1.matched_files:
                print(f'   📄 {match.final_path.name}')
        else:
            print(f'❌ Failed: {result1.error_message}')
        print()

        # Demo 2: Extract .log files  
        pattern2 = r'.*\.log$'
        print('📋 Demo 2: Extract .log files with sequential naming')
        print(f'🔍 Pattern: "{pattern2}" (matches filenames ending with .log)')
        config2 = ExtractorConfig(
            target_pattern=pattern2,
            prefix='log_',
            output_dir=temp_path / 'extracted_log',
            unlimited_depth=True
        )

        extractor2 = RecursiveExtractor(config2)
        result2 = extractor2.extract_from_archive(archive_path)

        if result2.success:
            print(f'✅ Success! Found {len(result2.matched_files)} .log files')
            for match in result2.matched_files:
                print(f'   📄 {match.final_path.name}')
        else:
            print(f'❌ Failed: {result2.error_message}')
        print()

        # Demo 3: Extract all files with comprehensive stats
        pattern3 = r'.*(\.txt|\.log)$'
        print('📋 Demo 3: Extract all files (txt and log) with sequential naming')
        print(f'🔍 Pattern: "{pattern3}" (matches filenames ending with .txt OR .log)')
        config3 = ExtractorConfig(
            target_pattern=pattern3,
            prefix='all_',
            output_dir=temp_path / 'extracted_all',
            unlimited_depth=True
        )

        extractor3 = RecursiveExtractor(config3)
        result3 = extractor3.extract_from_archive(archive_path)

        if result3.success:
            print(f'✅ Success! Found {len(result3.matched_files)} files total')
            for match in result3.matched_files:
                print(f'   📄 {match.final_path.name}')
            print(f'🔍 Maximum depth reached: {result3.depth_reached}')
            print(f'📦 Total files processed: {result3.total_extracted}')
            print(f'⏱️  Extraction time: {result3.extraction_time:.3f} seconds')
        else:
            print(f'❌ Failed: {result3.error_message}')
        print()
        
        # Demo 4: Negative test examples
        print('📋 Demo 4: Negative Test Examples')
        
        # Test non-existent extension
        pattern4 = r'.*\.pdf$'
        print(f'🔍 Pattern: "{pattern4}" (should find 0 files)')
        config4 = ExtractorConfig(
            target_pattern=pattern4,
            prefix='pdf_',
            output_dir=temp_path / 'extracted_pdf',
            unlimited_depth=True
        )

        extractor4 = RecursiveExtractor(config4)
        result4 = extractor4.extract_from_archive(archive_path)

        if result4.success:
            print(f'✅ Expected result: Found {len(result4.matched_files)} .pdf files')
            if len(result4.matched_files) == 0:
                print('   ✅ Correctly found no matching files')
        else:
            print(f'❌ Failed: {result4.error_message}')
        
        # Test path-based pattern (should fail due to filename-only matching)
        pattern5 = r'.*/foo\.txt$'
        print(f'🔍 Pattern: "{pattern5}" (should find 0 files - path matching disabled)')
        config5 = ExtractorConfig(
            target_pattern=pattern5,
            prefix='path_',
            output_dir=temp_path / 'extracted_path',
            unlimited_depth=True
        )

        extractor5 = RecursiveExtractor(config5)
        result5 = extractor5.extract_from_archive(archive_path)

        if result5.success:
            print(f'✅ Expected result: Found {len(result5.matched_files)} path-based matches')
            if len(result5.matched_files) == 0:
                print('   ✅ Correctly found no files (filename-only matching working)')
        else:
            print(f'❌ Failed: {result5.error_message}')
        
        print()
        
        # Demo 5: Show exact filename matching
        pattern6 = r'^foo\.txt$'
        print('📋 Demo 5: Exact filename matching')
        print(f'🔍 Pattern: "{pattern6}" (exact match for foo.txt)')
        config6 = ExtractorConfig(
            target_pattern=pattern6,
            prefix='exact_',
            output_dir=temp_path / 'extracted_exact',
            unlimited_depth=True
        )

        extractor6 = RecursiveExtractor(config6)
        result6 = extractor6.extract_from_archive(archive_path)

        if result6.success:
            print(f'✅ Success! Found {len(result6.matched_files)} exact matches')
            for match in result6.matched_files:
                print(f'   📄 {match.final_path.name}')
                # Show file content
                content = match.final_path.read_text()[:100] + "..."
                print(f'   📝 Content preview: {content}')
        else:
            print(f'❌ Failed: {result6.error_message}')

    print()
    print('🎉 Demo completed!')
    print()
    print('� Key Features Demonstrated:')
    print('   • Deep recursive extraction through multiple archive formats')
    print('   • Sequential file naming (prefix_filename_sn1, sn2, etc.)')
    print('   • Filename-only pattern matching (no path matching)')
    print('   • Unlimited depth extraction for target files')
    print('   • Proper negative testing (patterns that should match nothing)')
    print('   • Multiple archive format support (ZIP -> TAR -> TAR.GZ)')


if __name__ == "__main__":
    demo_nested_archive_extraction()
