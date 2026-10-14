# Lab 5: Reflection — School Bus Transport Register

**File analysed:** `school_transport.py`
**Tools used:** Pylint, Flake8, Bandit

## 1. Which tool was most useful, and why?

**Answer:** Bandit, because it found the two real security problems: shell
injection (B602) and SQL injection (B608). Pylint was best for overall quality
and gave a score to track progress (4.00 to 10.00). Flake8 mostly repeated
style issues Pylint already reported.

## 2. What was the most serious issue, and what could go wrong if it shipped?

**Answer:** The shell injection in `dispatchAlert`. It ran `shell=True` with
the route name, so input like `R1; <command>` could run extra commands. I fixed
it by removing the shell call. The SQL injection in `enrollRider` was next, and
I fixed it with `?` placeholders.

## 3. Did the tools miss anything or report something misleading?

**Answer:** They missed that `feeCollected` returned `None` instead of 0 for a
route with no riders, because `SUM` returns `None` on no rows. I fixed it with
`COALESCE`. Some Bandit warnings (the `subprocess` import, `assert` in demo
code) were low value here.

## 4. How would you use static analysis in future projects?

**Answer:** Run the tools while coding and before each commit, and add them to
CI for team projects. I would read each warning instead of fixing blindly,
since 10/10 doesn't prove the code is correct and testing is still needed.
