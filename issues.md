# Issues Found in school_transport.py

Baseline: Pylint 4.00/10, Flake8 9 findings, Bandit 1 High / 1 Medium / 2 Low.

| Issue | Type | Line(s) | Description | Fix Approach |
| ----- | ---- | ------- | ----------- | ------------ |
| Shell command injection (B602, High) | Security | 24 | `dispatchAlert` builds a shell string from `route` and runs it with `shell=True`. A route like `R1; rm -rf x` would run extra commands. | Remove `shell=True` and pass a list of arguments, or replace the `echo` with `print`/`logging`. |
| SQL injection (B608, Medium) | Security | 9 | `enrollRider` puts `student`, `route` and `stop` straight into the SQL with an f-string. A quote in a name breaks or hijacks the query. | Use a parameterized query: `VALUES (?, ?, ?, ?)` with a tuple of values. |
| Bare `except` (E722, W0702) | Bug / Style | 30 | `feeCollected` catches every exception, including ones that hide real bugs. It also misses a real bug: `SUM` returns `None`, not 0, for a route with no riders. | Catch `sqlite3.Error` only, and use `COALESCE(SUM(fee), 0)` or `or 0` so the result is always a number. |
| File not closed safely, no encoding (R1732, W1514) | Reliability | 18-21 | `exportRoster` opens a file and closes it manually. If a write fails, the file stays open. No encoding is given, so output depends on the OS. | Use `with open(path, "w", encoding="utf-8") as out:`. |
| Unused argument `driver` (W0613) | Code quality | 13 | `routeRoster` takes `driver` but never uses it, and callers pass `None` or a name for nothing. | Remove the parameter and update both callers (lines 19 and 41). |
| Use of `assert` (B101, Low) | Security / Quality | 38 | `assert` is removed when Python runs with `-O`, so the check silently disappears. | Replace it with an explicit `if ... : raise` or print a failure message. |
| Non-snake_case function names (C0103) | Style | 8, 13, 17, 23, 27 | `enrollRider`, `routeRoster`, `exportRoster`, `dispatchAlert` and `feeCollected` use camelCase, which breaks PEP 8. | Rename to `enroll_rider`, `route_roster`, `export_roster`, `dispatch_alert`, `fee_collected` and update all calls. |
| Missing docstrings (C0114, C0116) | Documentation | 1, 8, 13, 17, 23, 27, 34 | The module and every function lack docstrings. | Add a short docstring to the module and to each function. |
| Lines too long (E501, C0301) | Style | 5, 9, 14, 29 | Lines run to 95-116 characters, over the 79 (Flake8) and 100 (Pylint) limits. | Wrap long strings and calls across lines. |
| Formatting errors (E231, E302) | Style | 8, 23 | Missing spaces after commas in the `enrollRider` signature, and only one blank line before `dispatchAlert`. | Add the spaces and a second blank line. |
| `subprocess` import flagged (B404, Low) | Security | 1 | Informational flag that importing `subprocess` carries risk. | Goes away if `subprocess` is no longer used. Otherwise keep it with a safe call. |

## Results After Fixes

| Tool | Before | After |
| ---- | ------ | ----- |
| Pylint | 4.00/10 | 10.00/10 |
| Flake8 | 9 findings | 0 findings |
| Bandit | 1 High, 1 Medium, 2 Low | 0 issues |

All issues in the table above were fixed. The program output is unchanged
(`dispatching bus R1` and `['Zoya']`), and `route_r1.txt` still lists Tara and Kabir.

Reports: `pylint_report.txt`, `bandit_report.txt` and `flake8_report.txt` are the
original runs. `pylint_after.txt`, `bandit_after.txt` and `flake8_after.txt` are
the runs after the fixes.
