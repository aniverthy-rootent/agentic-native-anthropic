"""Safety Incident Review

Task: Review a near-miss at a manufacturing plant.
Framework: the Anthropic Claude API (anthropic SDK, no framework)
"""
from runtime import run_app

SLUG = 'incident_review'
TITLE = 'Safety Incident Review'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Review a near-miss at a manufacturing plant.'

# (key, role, instruction)
AGENTS = [
    ('timeline_builder', 'Timeline Builder', 'Timeline.'),
    ('cause_analyst', 'Cause Analyst', 'Causes.'),
    ('barrier_analyst', 'Barrier Analyst', 'Barriers.'),
    ('action_planner', 'Action Planner', 'Corrective actions.'),
    ('learning_writer', 'Learning Writer', 'Lessons.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
