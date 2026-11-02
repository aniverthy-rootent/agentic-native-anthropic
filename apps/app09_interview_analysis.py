"""Qualitative Interview Analysis

Task: Code themes in 12 user interviews.
Framework: the Anthropic Claude API (anthropic SDK, no framework)
"""
from runtime import run_app

SLUG = 'interview_analysis'
TITLE = 'Qualitative Interview Analysis'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Code themes in 12 user interviews.'

# (key, role, instruction)
AGENTS = [
    ('transcript_reader', 'Transcript Reader', 'Read.'),
    ('coder', 'Coder', 'Initial codes.'),
    ('theme_builder', 'Theme Builder', 'Themes.'),
    ('quote_selector', 'Quote Selector', 'Quotes.'),
    ('insight_writer', 'Insight Writer', 'Insights.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
