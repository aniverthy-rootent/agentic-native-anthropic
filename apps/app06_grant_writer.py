"""Grant Proposal Writer

Task: Write a grant for a community coding program.
Framework: the Anthropic Claude API (anthropic SDK, no framework)
"""
from runtime import run_app

SLUG = 'grant_writer'
TITLE = 'Grant Proposal Writer'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Write a grant for a community coding program.'

# (key, role, instruction)
AGENTS = [
    ('needs_analyst', 'Needs Analyst', 'Needs.'),
    ('aims_writer', 'Aims Writer', 'Aims.'),
    ('plan_writer', 'Plan Writer', 'Activities.'),
    ('budget_writer', 'Budget Writer', 'Budget.'),
    ('evaluator', 'Evaluator', 'Evaluation plan.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
