"""AI Ethics Review Board

Task: Review a facial-recognition pilot for a retail chain.
Framework: the Anthropic Claude API (anthropic SDK, no framework)
"""
from runtime import run_app

SLUG = 'ethics_review'
TITLE = 'AI Ethics Review Board'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Review a facial-recognition pilot for a retail chain.'

# (key, role, instruction)
AGENTS = [
    ('use_case_analyst', 'Use-Case Analyst', 'Describe use.'),
    ('harm_assessor', 'Harm Assessor', 'Harms.'),
    ('bias_auditor', 'Bias Auditor', 'Bias.'),
    ('mitigation_designer', 'Mitigation Designer', 'Mitigations.'),
    ('decision_writer', 'Decision Writer', 'Recommendation.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
