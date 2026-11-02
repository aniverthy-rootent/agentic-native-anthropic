"""LLM Red-Team Planner (defensive)

Task: Plan safe evaluation of a customer chatbot's guardrails.
Framework: the Anthropic Claude API (anthropic SDK, no framework)
"""
from runtime import run_app

SLUG = 'red_team'
TITLE = 'LLM Red-Team Planner (defensive)'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = "Plan safe evaluation of a customer chatbot's guardrails."

# (key, role, instruction)
AGENTS = [
    ('scope_definer', 'Scope Definer', 'Scope.'),
    ('risk_cataloger', 'Risk Cataloger', 'Risk categories.'),
    ('test_designer', 'Test Designer', 'Test design.'),
    ('metrics_agent', 'Metrics Agent', 'Metrics.'),
    ('report_writer', 'Report Writer', 'Report.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
