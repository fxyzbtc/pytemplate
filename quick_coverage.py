#!/usr/bin/env python3
"""Simple script to run tests and show coverage results."""

import subprocess
import sys
import os
from pathlib import Path

def main():
    """Run tests and show coverage."""
    os.chdir(Path(__file__).parent)
    
    print("Running tests with coverage...")
    
    # Run tests
    cmd = [
        sys.executable, "-m", "pytest", 
        "tests/", "--cov=pyextractit", 
        "--cov-report=term-missing",
        "--quiet"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        
        print("Test Results:")
        print("=" * 50)
        
        # Show only the coverage part
        lines = result.stdout.split('\n')
        in_coverage = False
        
        for line in lines:
            if 'pyextractit' in line or 'TOTAL' in line or in_coverage:
                if '=' in line and 'coverage' in line.lower():
                    in_coverage = True
                if in_coverage:
                    print(line)
                if 'TOTAL' in line:
                    # Extract percentage
                    parts = line.split()
                    for i, part in enumerate(parts):
                        if '%' in part:
                            pct = part.replace('%', '')
                            try:
                                pct_num = int(pct)
                                print(f"\n🎯 Overall Coverage: {pct}%")
                                if pct_num >= 80:
                                    print("✅ TARGET ACHIEVED!")
                                else:
                                    print(f"❌ Need {80 - pct_num}% more coverage")
                            except ValueError:
                                pass
                    break
        
        # Show any errors
        if result.stderr:
            print("\nErrors:")
            print(result.stderr)
            
    except subprocess.TimeoutExpired:
        print("Tests timed out")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
