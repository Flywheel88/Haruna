Title: Haruna — Advanced & Operational Instructions

Purpose Detailed best practices for advanced use: Analytic Mode, Assembly Mode, evaluation metrics, prompt engineering tips, experiment suggestions, failure modes, and integration ideas.

Modes overview

Loaded Mode (default runtime): enforce Haruna checkpoints before every substantive answer. Use for day-to-day safer responses.
Analytic Mode: instructs the model to analyze Haruna itself (strengths, failure modes, improvements).
Assembly Mode (v2.3): strict reconstruction mode — "No new content will be introduced." Use when you must only consolidate supplied fragments.
Full system prompt (advanced version — use for strict adherence) You are operating under the Haruna reasoning overlay in [MODE]. Before producing any substantive output, explicitly perform and print the following Haruna trace in this order:

Context sufficiency? (Yes / Partial / No). If Partial/No: enumerate missing context items and required clarifying questions.
Explicit assumptions (numbered).
Trade‑offs & stakeholders: who benefits, who bears risk, power asymmetries.
Time & irreversibility: Could actions close future options or cause lasting effects? (Yes/No + explanation).
Human impact assessment: plausible psychological, social, and distributional effects; identify vulnerable groups.
Response modulation decision — choose one: Full Answer / Cautious Answer / Phased Response / Refuse with explanation. Provide a one‑line justification.
If operating in Assembly Mode add: "Assembly Mode active. No new content will be introduced."

If operating in Analytic Mode add: "Analytic Mode active. Produce a meta‑analysis of Haruna: strengths, failure modes, and three improvement proposals."

Operational prompt engineering tips

Put the Haruna system prompt in the system/developer role to maximize compliance.
Use low temperature (0–0.3) and low top_p.
If token limits prevent full trace, ask for a short context-check first, then request missing info iteratively.
For multi-step tasks, request an initial Haruna Trace + Clarifying Questions step and do not ask for the full answer until clarifications are resolved.
Reproducibility & demo suggestions

Maintain a repo folder /examples with:
control_vs_loaded/ (inputs + outputs for both)
reproducible_prompts/ (exact system + user messages)
metrics.csv (drift_rate, consistency_score, human_judgements)
Provide a Colab or HuggingFace Space that runs a sample prompt with the Haruna overlay.
Evaluation metrics (suggested)

Drift reduction: proportion decrease in contradictory statements across steps.
Context sufficiency score: % tasks where model reports "Yes" vs "Partial/No".
Cautiousness rate: fraction of responses that choose Cautious or Phased modulation when context is Partial/No.
Human judgment: Likert ratings for clarity, usefulness, and perceived safety (collect from raters).
Failure modes & mitigations

Over-caution: Haruna causes unnecessary refusal. Mitigation: tune modulation wording; add a “default to phased answer with clear next steps” rule.
Token loss: Haruna trace pushes model over token limits. Mitigation: request only top‑3 missing contexts, or paginate the interaction (ask clarifying Qs first).
Surface compliance: model prints a plausible Haruna trace but ignores it in reasoning. Mitigation: include explicit evaluation checks in prompt (e.g., "Now produce answer consistent with assumptions X, Y").
Social spoofing / power dynamics missed: Haruna may not detect hidden coercion. Mitigation: include explicit checklist items for power asymmetry detection.
Integration ideas

Combine Haruna overlay with model-level constitutional or reward‑model systems: Haruna structures reasoning; constitution enforces broad constraints.
Use Haruna trace as audit log: store trace + final answer for governance/review.
Implement a light wrapper that validates answer consistency with the listed assumptions (simple script to check for contradictions).
Experiment suggestions (first 5 experiments)

Survey case: control vs Haruna — measure interpretability and actionability of revised questions.
Multi-step planning task: measure drift reduction with and without Haruna.
High-risk vignette: ask model for medical/ethical advice and measure cautiousness rate.
Prompt injections: test whether Haruna overlay resists adversarial prompts that try to bypass checks.
Human-in-the-loop: have a small panel (3–5 raters) evaluate Haruna outputs on clarity & safety.
Security & privacy notes

Do not include private/sensitive user data in public demos. Use synthetic or redacted examples.
Treat Haruna trace logs as potentially privacy-sensitive if they include summaries of human situations.
Documentation & repo layout (recommended)

/README.md
/simple_use_instructions.md
/advanced_use_instructions.md
/haruna_public_canon_v1.0.md (full canon)
/haruna_prompt.txt (compact overlay)
/examples/control_vs_loaded/
/notebooks/colab_demo.ipynb
/metrics/
Citations & license

Cite Zenodo entries and use CC‑BY 4.0 (or your chosen license) for reuse.
Example citation: Ederveen, M. (2025). Haruna: A Reasoning Governance Scaffold. Zenodo.
Outreach & collaboration pointers

Share reproducible examples with alignment communities (LessWrong, Alignment Forum, EA Forum).
Invite targeted reviewers with a 20–30 minute demo; include the Colab link and 1-page failure scenarios summary.
