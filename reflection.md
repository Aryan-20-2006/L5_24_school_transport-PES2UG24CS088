Which tool was most useful, and why? Bandit caught the two security issues (shell and SQL injection), Pylint gave the broadest coverage and the score, and Flake8 covered style.
What was the most serious issue, and what could go wrong if it shipped? For example, how a crafted route name could run commands through shell=True, or how a quote in a student name could break the SQL.
Did the tools miss anything or report something misleading? The None returned for an empty route, which none of the three flagged, and the Bandit warnings about assert and the subprocess import, which are low severity.
How would you use static analysis in future projects? For example, running the tools before each commit or in CI, and what a 10/10 score does and doesn’t prove.
