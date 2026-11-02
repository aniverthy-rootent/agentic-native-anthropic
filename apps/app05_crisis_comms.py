"""Crisis Communications

Task: A data breach affected 20,000 customers.
Framework: the Anthropic Claude API (anthropic SDK, no framework)
"""
from runtime import run_app

SLUG = 'crisis_comms'
TITLE = 'Crisis Communications'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'A data breach affected 20,000 customers.'

# (key, role, instruction)
AGENTS = [
    ('facts_gatherer', 'Facts Gatherer', 'Confirmed facts.'),
    ('stakeholder_planner', 'Stakeholder Planner', 'Audiences.'),
    ('statement_writer', 'Statement Writer', 'Public statement.'),
    ('q_a_preparer', 'Q&A Preparer', 'Tough questions.'),
    ('tone_reviewer', 'Tone Reviewer', 'Review tone.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
