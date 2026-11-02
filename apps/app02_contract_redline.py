"""Contract Redlining

Task: Redline a freelance agreement for the freelancer.
Framework: the Anthropic Claude API (anthropic SDK, no framework)
"""
from runtime import run_app

SLUG = 'contract_redline'
TITLE = 'Contract Redlining'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Redline a freelance agreement for the freelancer.'

# (key, role, instruction)
AGENTS = [
    ('clause_mapper', 'Clause Mapper', 'Map clauses.'),
    ('risk_finder', 'Risk Finder', 'Find risks.'),
    ('redline_writer', 'Redline Writer', 'Propose edits.'),
    ('fairness_reviewer', 'Fairness Reviewer', 'Check balance.'),
    ('summary_writer', 'Summary Writer', 'Summarize changes.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
