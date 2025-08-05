## Test Fixes Summary

### ✅ **Fixed Test Failures:**

#### 1. **Max Depth Validation Issues**
- **Problem**: Inconsistent max depth validation ranges between extractor config and tests
- **Root Cause**: Default `max_depth` was 50, but tests expected 10; validator allowed 1-200, but validation tests expected 1-50
- **Solution**: 
  - Changed default `max_depth` from 50 to 10 in `ExtractorConfig`
  - Updated validator range from 1-200 to 1-50
  - Fixed test expectation in `test_extractor.py` from 201 to 51 for upper bound

#### 2. **CLI Overwrite Test**
- **Problem**: Test expected filename `extracted_sample1.txt` but actual output uses sequential naming `extracted_sample1_sn1.txt`
- **Root Cause**: Sequential naming feature changes the output filename pattern
- **Solution**: Updated test to expect the correct sequential naming pattern `extracted_sample1_sn1.txt`

#### 3. **Configuration Defaults Test**
- **Problem**: Test expected default `max_depth` of 10, but config had 50
- **Root Cause**: Default value mismatch
- **Solution**: Changed default `max_depth` from 50 to 10

### 🔧 **Changes Made:**

**File: `pyextractit/extractor.py`**
```python
# Changed default max_depth
max_depth: int = Field(default=10, ...)  # was: default=50

# Updated validator range
if v < 1 or v > 50:  # was: v > 200
    raise ValueError("Max depth must be between 1 and 50")  # was: 1 and 200
```

**File: `tests/test_cli.py`**
```python
# Updated expected filename for overwrite test
existing = output_dir / "extracted_sample1_sn1.txt"  # was: "extracted_sample1.txt"
```

**File: `tests/test_extractor.py`**
```python
# Updated validation error message expectations
with pytest.raises(ValueError, match="Max depth must be between 1 and 50"):  # was: 1 and 200
    max_depth=51  # was: 201
```

### 📊 **Test Results:**
- **Before**: 3 failed, 104 passed
- **After**: All tests passing ✅
- **Fixed Tests**:
  - `tests/test_cli.py::TestCLI::test_extract_overwrite`
  - `tests/test_validation.py::TestExtractorValidation::test_max_depth_validation`
  - `tests/test_validation.py::TestExtractorValidation::test_config_with_all_defaults`
  - `tests/test_extractor.py::TestExtractorConfig::test_invalid_max_depth`

### 🎯 **Impact:**
- All tests now pass consistently
- Configuration validation is properly aligned across all components
- Sequential file naming feature is properly tested
- Max depth limits are sensible (1-50 instead of 1-200)
- Default max depth is more reasonable (10 instead of 50)

The fixes ensure that PyExtractIt's configuration validation is consistent across all components and that the new sequential naming feature is properly tested.
