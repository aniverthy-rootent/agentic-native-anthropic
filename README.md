# agentic-native-anthropic

**11 multi-agent applications built with the Anthropic Claude API (anthropic SDK, no framework).**  
Theme: _Analysis, safety-critical & writing apps using the Claude API directly_

Every agent is a plain call to the [Anthropic Messages API](https://docs.anthropic.com) - no agent framework.

## Quick start (no API key needed)

```bash
pip install -r requirements.txt
python run_all.py                       # run all 11 apps
python -m apps.app01_policy_analysis   # run a single app
pytest -q                               # smoke tests for every app
```

Every app runs against a deterministic offline model (`common/offline_llm.py`) so you can watch the orchestration work without credentials.

## How it works

`runtime.py` runs agents layer by layer (threads for parallel layers). Each agent is one `messages.create` call with its role as the `system` prompt and upstream outputs in the user message.

## Using a real model

```bash
export ANTHROPIC_API_KEY=...   # optional; model via ANTHROPIC_MODEL
python run_all.py
```
Without a key the offline model is used.

## Applications

| # | Application | Agents | Roles |
|---|---|---|---|
| 1 | Policy Analysis Desk | 5 | Context Researcher, Stakeholder Mapper, Impact Modeler, Counterargument Agent, Briefing Writer |
| 2 | Contract Redlining | 5 | Clause Mapper, Risk Finder, Redline Writer, Fairness Reviewer, Summary Writer |
| 3 | Code Explainer | 5 | Structure Analyst, Line Explainer, Bug Spotter, Improvement Advisor, Teacher |
| 4 | AI Ethics Review Board | 5 | Use-Case Analyst, Harm Assessor, Bias Auditor, Mitigation Designer, Decision Writer |
| 5 | Crisis Communications | 5 | Facts Gatherer, Stakeholder Planner, Statement Writer, Q&A Preparer, Tone Reviewer |
| 6 | Grant Proposal Writer | 5 | Needs Analyst, Aims Writer, Plan Writer, Budget Writer, Evaluator |
| 7 | Academic Editor | 5 | Structure Checker, Clarity Editor, Citation Checker, Jargon Reducer, Final Polisher |
| 8 | LLM Red-Team Planner (defensive) | 5 | Scope Definer, Risk Cataloger, Test Designer, Metrics Agent, Report Writer |
| 9 | Qualitative Interview Analysis | 5 | Transcript Reader, Coder, Theme Builder, Quote Selector, Insight Writer |
| 10 | Safety Incident Review | 5 | Timeline Builder, Cause Analyst, Barrier Analyst, Action Planner, Learning Writer |
| 11 | Knowledge Handover | 5 | Interviewer, System Mapper, Risk Cataloger, Runbook Writer, Reviewer |

Full per-agent instructions are in [AGENTS.md](AGENTS.md).

Each app uses one of two data-flow patterns (see `common/flow.py`):
`sequential` (each agent builds on the previous) or `fanout` (a planner, parallel specialists, then a merger).

## License

MIT
