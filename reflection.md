# Lab 5: Reflection — School Bus Transport Register

**File analysed:** `school_transport.py`
**Tools used:** Pylint, Flake8, Bandit

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

**Answer:** The easiest were the mechanical ones: naming (camelCase to
snake_case), docstrings, long lines and spacing, because the tools say exactly
what to change. The hardest were the security fix in `dispatchAlert` and the
`None` bug in `feeCollected`. For the first, `echo` is a Windows shell built-in,
so removing `shell=True` is not a simple swap and I had to choose a safe
replacement (`print`). The second was hard because no tool flagged it: `SUM`
returns `None` for a route with no riders, so I found it by reading the code.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

**Answer:** There were no clear false positives, but some warnings were low
value here. Bandit B404 flags the `import subprocess` line, which is only an
informational warning. Bandit B101 flagged the `assert` in `main()`, which is
demo code, though asserts are still unsafe for real checks because they are
removed with `python -O`. They are worth noting but not real bugs.

## 3. How would you integrate static analysis tools into your actual software development workflow?

**Answer:** I would run Pylint, Flake8 and Bandit in my editor while coding and
as a pre-commit check, so issues are caught before they are committed. For team
projects I would add them to CI (for example GitHub Actions) so every pull
request is checked. I would still read each warning rather than fix it blindly,
since some are informational and the tools do not replace testing.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

**Answer:** Security improved: Bandit went from 1 High, 1 Medium and 2 Low
issues to none, and the SQL and shell injections are gone. Robustness improved:
files are closed with `with`, the `except` is specific, and an empty route now
returns 0 instead of `None`. Readability improved with snake_case names,
docstrings and shorter lines. Pylint went from 4.00/10 to 10.00/10 and Flake8
from 9 findings to 0, and the program's output stayed the same.
