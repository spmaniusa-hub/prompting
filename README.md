# Prompting: Workflow & Utility Functions

**Repository:** [https://github.com/spmaniusa-hub/prompting](https://github.com/spmaniusa-hub/prompting)  
**Author:** Mani Subramanian  
**Python Version:** Python 3.11+ (Python standard library only)  

This repository contains workflow utilities and practical functions developed for prompting assignments and automated workflow pipelines.

---

## 1. Status Normalization Utility (`status_demo.py`)

The `normalize_status` function normalizes raw, varied task status strings into consistent canonical values.

### Canonical Status Mappings

| Input Status (Case-Insensitive, Trimmed) | Canonical Output Status |
|---|:---:|
| `"todo"` | `"pending"` |
| `"not started"` | `"pending"` |
| `"working"` | `"in_progress"` |
| `"IN PROGRESS"` | `"in_progress"` |
| `"done"` | `"completed"` |
| `"finished"` | `"completed"` |
| `"cancelled"` | `"unknown"` |
| *Any unsupported string, empty, or whitespace* | `"unknown"` |
| *Non-string inputs (`None`, `int`, `bool`, etc.)* | `"unknown"` |

### Key Requirements Implemented
- **Whitespace Tolerance:** Leading and trailing whitespace is safely ignored (e.g., `"  todo  "` &rarr; `"pending"`).
- **Case-Insensitive Matching:** Works uniformly across uppercase, lowercase, and mixed casing (e.g., `"IN PROGRESS"` &rarr; `"in_progress"`).
- **Graceful Fallbacks:** Non-string inputs and unrecognized values safely return `"unknown"`.
- **Zero Third-Party Dependencies:** Relies strictly on the Python standard library.

---

## 2. Usage Example

```python
from status_demo import normalize_status

# Basic conversions
print(normalize_status("todo"))         # -> "pending"
print(normalize_status("working"))      # -> "in_progress"
print(normalize_status("done"))         # -> "completed"

# Case and whitespace tolerance
print(normalize_status("  IN PROGRESS  "))  # -> "in_progress"
print(normalize_status("Not Started"))      # -> "pending"

# Unsupported and non-string inputs
print(normalize_status("cancelled"))    # -> "unknown"
print(normalize_status(None))           # -> "unknown"
print(normalize_status(123))            # -> "unknown"
```

---

## 3. Running the Verification Suite

Run the script directly to execute both the visual demonstration and the automated `unittest` test suite:

```bash
python3 status_demo.py
```

### Expected Output
```text
============================================================
Running normalize_status Demonstration & Unit Tests
============================================================

Demonstration Results:
  'todo'               -> 'pending'
  'not started'        -> 'pending'
  'working'            -> 'in_progress'
  'IN PROGRESS'        -> 'in_progress'
  'done'               -> 'completed'
  'finished'           -> 'completed'
  'cancelled'          -> 'unknown'
  '  todo  '           -> 'pending'
  None                 -> 'unknown'
  123                  -> 'unknown'
  'blocked'            -> 'unknown'

------------------------------------------------------------
Running unittest test suite...
------------------------------------------------------------
test_case_insensitivity (__main__.TestNormalizeStatus.test_case_insensitivity) ... ok
test_non_string_inputs (__main__.TestNormalizeStatus.test_non_string_inputs) ... ok
test_specification_examples (__main__.TestNormalizeStatus.test_specification_examples) ... ok
test_unsupported_and_empty_strings (__main__.TestNormalizeStatus.test_unsupported_and_empty_strings) ... ok
test_whitespace_handling (__main__.TestNormalizeStatus.test_whitespace_handling) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```
