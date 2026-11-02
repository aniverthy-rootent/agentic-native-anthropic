"""Native Claude runtime: direct Messages API calls, no agent framework.

With ANTHROPIC_API_KEY set it calls Claude; otherwise it runs offline."""
from __future__ import annotations

import os
from concurrent.futures import ThreadPoolExecutor

from common.flow import compose_input, dependencies, execution_layers, system_prompt
from common.offline_llm import offline_complete

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5-5")


def call_llm(system: str, user: str, provider=None) -> str:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return offline_complete(system, user)
    import anthropic

    client = anthropic.Anthropic()
    msg = client.messages.create(
        model=MODEL, max_tokens=800, system=system,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(b.text for b in msg.content if b.type == "text")

def _run_layers(agents, task, pattern, provider):
    deps = dependencies(pattern, len(agents))
    outputs: dict[str, str] = {}

    def one(i):
        key, role, instr = agents[i]
        ups = [(agents[j][1], outputs[agents[j][0]]) for j in deps[i]]
        return key, call_llm(system_prompt(role, instr), compose_input(task, ups), provider)

    for layer in execution_layers(pattern, len(agents)):
        if len(layer) == 1:
            k, v = one(layer[0])
            outputs[k] = v
        else:
            with ThreadPoolExecutor(max_workers=len(layer)) as pool:
                for k, v in pool.map(one, layer):
                    outputs[k] = v
    return {key: outputs[key] for key, _, _ in agents}


def run_app(title, agents, task, pattern="sequential", provider=None) -> dict:
    return _run_layers(agents, task, pattern, provider)
