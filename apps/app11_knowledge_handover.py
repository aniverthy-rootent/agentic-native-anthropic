"""Knowledge Handover

Task: Capture the knowledge of a departing database engineer.
Framework: the Anthropic Claude API (anthropic SDK, no framework)
"""
from runtime import run_app

SLUG = 'knowledge_handover'
TITLE = 'Knowledge Handover'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Capture the knowledge of a departing database engineer.'

# (key, role, instruction)
AGENTS = [
    ('interviewer', 'Interviewer', 'Questions.'),
    ('system_mapper', 'System Mapper', 'System map.'),
    ('risk_cataloger', 'Risk Cataloger', 'Tribal knowledge risks.'),
    ('runbook_writer', 'Runbook Writer', 'Runbooks.'),
    ('reviewer', 'Reviewer', 'Review gaps.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
