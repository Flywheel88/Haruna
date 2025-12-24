# Haruna
A language‑based scaffold for safer reasoning

Haruna — reasoning governance scaffold (MVP repo)
Short description Haruna is a language-based reasoning scaffold that structures LLM reasoning around context sufficiency, explicit assumptions, trade‑offs, time/irreversibility, and human impact. This repo provides a minimal reproducible artifactset: prompt overlays, a concrete survey case, and a simple Colab/python skeleton to try Haruna with an LLM.

Contents

README.md (this file)
haruna_prompt.txt — the Haruna overlay prompt (use as system or developer instruction)
survey_case.txt — a reproducible example: original survey, Haruna-guided reformulation
colab_skeleton.py — a simple runnable example for local/Colab use (fill in API key)
CONTRIBUTING.md — how to contribute or report issues
LICENSE — CC-BY 4.0 (short notice + link)
/examples — (optional) add outputs, experiments, metrics here
Quick start (5–10 min)

Haruna — a language-based reasoning scaffold. See simple_use_instructions.md for a quick start (Loaded Mode) and advanced_use_instructions.md for Analytic/Assembly modes, metrics, and best practices.

Clone the repo or use the GitHub UI to create files.
Run the Colab skeleton (colab_skeleton.py) or paste haruna_prompt.txt into your LLM system prompt.
Replace MODEL and API_KEY placeholders with your provider info.
Try the survey_case: compare the “control” vs “Haruna-guided” outputs.
Why this repo

Reproducible prompts reduce friction for reviewers.
Minimal, vendor-agnostic artifacts show how Haruna can be loaded as an overlay.
The survey case demonstrates how Haruna prevents misframed, ambiguous survey questions.
Citation If you use or adapt Haruna, please cite:

Ederveen, M. (2025). Haruna: A Reasoning Governance Scaffold for Context-, Time-, and Harm-Aware Artificial Intelligence. Zenodo. https://zenodo.org/records/17709817
Ederveen, M. (2025). Haruna: A Temporal–Intent Cognitive Scaffold for Stabilizing Multi-Step Reasoning in Large Language Models. Zenodo. https://zenodo.org/records/18037525
Contact Martin Ederveen — m.ederveen@btinternet.com

License CC‑BY 4.0 (see LICENSE file or https://creativecommons.org/licenses/by/4.0/)
