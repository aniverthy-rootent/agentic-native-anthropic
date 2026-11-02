"""Policy Analysis Desk

Task: Analyze the impact of a proposed carbon tax on households.
Framework: the Anthropic Claude API (anthropic SDK, no framework)
"""
from runtime import run_app

SLUG = 'policy_analysis'
TITLE = 'Policy Analysis Desk'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Analyze the impact of a proposed carbon tax on households.'

# (key, role, instruction)
AGENTS = [
    ('context_researcher', 'Context Researcher', 'Background.'),
    ('stakeholder_mapper', 'Stakeholder Mapper', 'Stakeholders.'),
    ('impact_modeler', 'Impact Modeler', 'Impacts.'),
    ('counterargument_agent', 'Counterargument Agent', 'Opposing views.'),
    ('briefing_writer', 'Briefing Writer', 'Briefing memo.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
