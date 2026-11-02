"""Academic Editor

Task: Improve the clarity of an abstract on federated learning.
Framework: the Anthropic Claude API (anthropic SDK, no framework)
"""
from runtime import run_app

SLUG = 'academic_editor'
TITLE = 'Academic Editor'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Improve the clarity of an abstract on federated learning.'

# (key, role, instruction)
AGENTS = [
    ('structure_checker', 'Structure Checker', 'Structure.'),
    ('clarity_editor', 'Clarity Editor', 'Clarity.'),
    ('citation_checker', 'Citation Checker', 'Citation style.'),
    ('jargon_reducer', 'Jargon Reducer', 'Jargon.'),
    ('final_polisher', 'Final Polisher', 'Polish.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
