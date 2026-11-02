"""Code Explainer

Task: Explain what a recursive descent parser does.
Framework: the Anthropic Claude API (anthropic SDK, no framework)
"""
from runtime import run_app

SLUG = 'code_explainer'
TITLE = 'Code Explainer'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Explain what a recursive descent parser does.'

# (key, role, instruction)
AGENTS = [
    ('structure_analyst', 'Structure Analyst', 'Structure.'),
    ('line_explainer', 'Line Explainer', 'Explain.'),
    ('bug_spotter', 'Bug Spotter', 'Spot bugs.'),
    ('improvement_advisor', 'Improvement Advisor', 'Suggest improvements.'),
    ('teacher', 'Teacher', 'Teach.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
