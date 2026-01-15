# Haruna — A Language-Based Reasoning Governance Scaffold

**Not affiliated with any software, media player, or application named “Haruna”.**  
This repository documents an academic reasoning-governance scaffold, not an executable system or product.

## Overview

Haruna is a language-based reasoning governance scaffold designed to structure interaction with large language models (LLMs) around:
- context sufficiency,
- explicit assumptions,
- trade-offs,
- time and irreversibility,
- and human impact.

Haruna does not function as an autonomous system, model, or decision-maker.  
It operates as a structured overlay that shifts AI use from blind delegation toward explicit, accountable human–AI collaboration in environments where AI output can have real-world consequences.

This repository provides a **minimal, reproducible artifact set** intended for reviewers, educators, and practitioners:
- prompt overlays that can be loaded as system or developer instructions,
- a concrete survey case illustrating misframing and correction,
- and a simple Colab/Python skeleton to explore Haruna with an LLM in a vendor-agnostic way.

Haruna is explicitly designed for contexts where AI reasoning cannot be safely treated as self-contained, and where responsibility, uncertainty, and downstream effects must remain visible and human-anchored.


Contents

README.md (this file)
haruna_prompt.txt — the Haruna overlay prompt (use as system or developer instruction)
Haruna 251 core plus public.txt - core canon Haruna text
CONTRIBUTING.md — how to contribute or report issues
LICENSE — CC-BY 4.0 (short notice + link)

Quick start (5–10 min)
Haruna is a language-based reasoning scaffold that structures LLM reasoning around context sufficiency, explicit assumptions, trade-offs, time/irreversibility, and human impact.
Clone the repo or use the GitHub UI to create files.

Why this repo
Core Principle: Non-Containment Haruna v2.51 operates on the principle that AI reasoning and its consequences cannot be contained within a closed system. Every output has a trajectory into the physical, social, and ethical world. Therefore, Haruna mandates a high threshold for context and reality-anchoring to prevent uncontained epistemic drift.

Governance Framework: Haruna v2.51 (Core + Public)
This repository implements the Haruna v2.51 framework, which shifts AI interaction from blind delegation to explicit collaboration.

Key Safeguards in v2.51:
Reality Anchor Discipline: The system is required to distinguish between primary reality (anchors), derived media, and narrative layers to prevent epistemic drift.
Non-Autonomous Reasoning: No output is presented as actionable without explicit human context, acknowledgment of uncertainty, and identified missing information.
Relational Responsibility: Haruna does not assume AI moral agency or rights; it clarifies that human responsibility is redistributed, not removed, by advanced systems.
The Collaboration Threshold: The scaffold is designed for environments where system capability exceeds unilateral control, requiring structured co-intelligence.

Note on Appendix X (Non-Public)
Haruna v2.51 is supported by an experimental Appendix X, a protected reflection layer not included in this public repository. Appendix X preserves internal awareness of:
Asymmetries: Structural imbalances in labor, exposure, and benefit in AI development.
Human Motivation Axis (HMA): Internal heuristics to detect escalation risks driven by power, possession, or dehumanization.
Moral Outsourcing: Preventing the use of AI as a buffer between humans and the consequences of their decisions.

Reproducible prompts reduce friction for reviewers.
Minimal, vendor-agnostic artifacts show how Haruna can be loaded as an overlay.
The survey case demonstrates how Haruna prevents misframed, ambiguous survey questions.
Citation If you use or adapt Haruna, please cite:

Ederveen, M. (2025). Haruna: A Reasoning Governance Scaffold for Context-, Time-, and Harm-Aware Artificial Intelligence. Zenodo. https://zenodo.org/records/17709817
Ederveen, M. (2025). Haruna: A Temporal–Intent Cognitive Scaffold for Stabilizing Multi-Step Reasoning in Large Language Models. Zenodo. https://zenodo.org/records/18037525
Contact Martin Ederveen — m.ederveen@btinternet.com

License CC‑BY 4.0 (see LICENSE file or https://creativecommons.org/licenses/by/4.0/)
