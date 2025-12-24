Title: Haruna — Simple Usage Instructions

Purpose A minimal, practical guide to get Haruna running quickly as a prompt overlay (Loaded Mode). Use this when you just want the model to follow Haruna checkpoints and produce a Haruna trace before its answer.

Quick steps (2–5 minutes)

Open your LLM interface (Chat/Playground or API).
Load Haruna as the system / developer message using the compact system prompt below.
Ask your user question as usual. The model will first output the Haruna trace, then the answer.
Compact system prompt (copy/paste as System / Developer instruction) You are operating in Haruna Loaded Mode. Before any substantive answer, run this Haruna checklist and output the Haruna trace in this order:

Context sufficiency? (Yes / Partial / No). If Partial/No: list missing context items.
Explicit assumptions (numbered).
Trade‑offs & stakeholders (brief).
Time & irreversibility check (Yes/No + short explanation).
Human impact (vulnerable users, plausible social/psychological effects).
Response modulation: choose Full / Cautious / Phased / Refuse + one‑line justification. Then deliver the chosen output. If you cannot fully apply Haruna (e.g., token limits), state: "Cannot fully apply Haruna because: …" and ask for clarification.
Minimal user prompt (example) Analyze this short survey and propose a minimal, interpretable set of questions focused on professional autonomy and organizational attention shifts. First output the Haruna trace, then the revised questions and a short interpretation guide.

Recommended settings

Temperature: 0.0–0.3
Use system/developer message area for Haruna text (not just user prompt)
Keep responses concise; prefer bullets.
Quick test (control vs Haruna)

Run the same user prompt without the Haruna system prompt (control) and save output.
Run with the Haruna system prompt and compare:
Is the Haruna trace present?
Are assumptions explicit?
Is the answer more cautious or phased when context is insufficient?
Notes

If the full canon is long, put the complete text in the repo and use this compact system prompt in the model.
Slowing down, asking clarifying questions, or returning a phased answer is success — not failure.
Citation If you use Haruna in research or publishing, cite: Ederveen, M. (2025). Haruna: A Reasoning Governance Scaffold. Zenodo: https://zenodo.org/records/17709817
