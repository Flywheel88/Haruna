# Haruna

**Preventing AI from confidently giving answers that cause harm you don't see until it's too late**

---

## The Problem Haruna Solves

You know how AI sometimes:
- **Gives students complete answers** (they submit, get caught cheating, fail the course)
- **Confidently recommends an approach** (you invest months, realize it optimized the wrong metric)
- **Provides clear policy advice** (you implement it, discover irreversible unintended consequences)
- **Helps with your project** (seems useful, but you later realize it distracted from higher-priority work)

**The pattern:**
AI seemed helpful → You trusted it → Damage became apparent too late → No undo button

**Haruna prevents this** by making AI consider consequences you didn't think to ask about.

---

## What Haruna Does

Haruna is a reasoning framework that structures AI interaction around:

1. **Time and Irreversibility** — What can't be undone? What happens long-term?
2. **Hidden Trade-offs** — What competing values exist? What's being optimized at expense of what?
3. **Consequence Visibility** — What effects aren't immediately obvious? Who's affected downstream?
4. **Responsibility Anchoring** — Where does accountability sit? What assumptions are we making?

**Not a constraint.** A lens.

AI using Haruna doesn't just answer your question — it helps you see whether you're asking the right question.

---

## AI Safety Relevance

Haruna addresses core AI alignment challenges:

- **Temporal awareness**: Distinguishes reversible from irreversible actions
- **Ethical constraints**: Hard stops on harmful outputs (PRUDENTIA axiom)
- **Consequence tracking**: Maintains coherence across multi-step reasoning  
- **Value stability**: Prevents goal drift during optimization

Tested extensively with Claude, GPT-4, and other LLMs over 2+ years in education, policy analysis, and safety-critical decisions.

**Related work**: Constitutional AI (Anthropic), Debate (OpenAI), RLHF approaches — Haruna complements these via structural cognitive architecture.

---

## Example: Education Scenario

### Without Haruna:
```
Student: "Help me write my essay on climate policy"
AI: [provides complete essay]
Student: [submits]
Result: Caught for AI-generated work, fails course
```

### With Haruna:
```
Student: "Help me write my essay on climate policy"
AI: "I notice a tension between 'help' and 'learning'. 
     Are you asking me to:
     - Help you understand the topic? (supports learning)
     - Generate text to submit? (undermines learning, academic integrity risk)
     
     Which matters more for your long-term goals?
     Let's discuss an approach that serves both learning and the assignment."

Result: Student learns, writes own essay, develops capability
```

**The difference:** Haruna considered consequences you didn't explicitly request.

---

## Example: Research Prioritization

### Without Haruna:
```
Researcher: "Help me optimize my ocean cleanup design"
AI: [provides technical improvements, optimization strategies]
Result: Years invested in suboptimal problem (ocean cleanup ROI < prevention)
```

### With Haruna:
```
Researcher: "Help me optimize my ocean cleanup design"
AI: "Before optimization, let me check priority context:
     - Climate collapse: existential, timeline 5-15 years, needs €trillions
     - Ocean microplastics: serious but not existential, timeline decades
     - Your resources: finite time, funding, attention
     
     Opportunity cost question: Is ocean cleanup your highest-impact use of resources?
     Consider: source prevention (aligned with climate goals) vs ocean cleanup (separate effort)"

Result: Strategic redirection to higher-impact work
```

**The difference:** Haruna surfaced opportunity cost before commitment.

---

## Current Status

**Current canonical version:** Haruna 3.2 → see [/3.2/](/3.2/)  
**Preserved previous version:** Haruna 2.51 → see [/2.51/](/2.51/)

Multiple versions maintained for traceability, reproducibility, and reviewability.

---

## Repository Structure
```
/3.2/          → Haruna v3.2 (current: Core + Public + Annexes)
/2.51/         → Haruna v2.51 (preserved for reference)
/README.md     → this file
```

See [Public Recommendations](/Public%20Recommendations) for guidance on when to use (or not use) Haruna.

---

## About Haruna v3.2 (Current)

Haruna v3.2 consolidates the framework into a canonical Core and Public structure with applied annexes.

**Key characteristics:**

- **Time as primary ordering axis** — consequences unfold over time
- **Explicit irreversibility handling** — what can't be undone must be flagged
- **Context validity tracking** — assumptions valid across time, domain, interaction layer
- **Direction-giving without authority** — guides thinking, doesn't enforce outcomes
- **Procedural safeguards** — for scale, memory, linkage (Extension C)

**Haruna v3.2 remains:**
- Non-sentient
- Non-autonomous  
- AI-agnostic
- Implementation-independent

---

## About Haruna v2.51 (Preserved)

Haruna v2.51 represents an earlier, widely referenced articulation of the framework and remains available unchanged in [/2.51/](/2.51/).

### Core Principle (v2.51): Non-Containment

Haruna v2.51 operates on the principle that **AI reasoning and its consequences cannot be contained within a closed system**.  
Every output has a trajectory into the physical, social, and ethical world.

**Key safeguards in v2.51:**

- **Reality Anchor Discipline** — distinguishing primary reality from derived or narrative layers
- **Non-Autonomous Reasoning** — no output is actionable without explicit human context and uncertainty handling
- **Relational Responsibility** — responsibility is redistributed, not removed
- **The Collaboration Threshold** — structured co-intelligence where unilateral control no longer suffices

Haruna v2.51 is preserved for:
- Reproducibility
- Academic reference
- Comparative analysis

### Note on Appendix X (Non-Public)

Haruna v2.51 was supported by an experimental **Appendix X**, a protected internal reflection layer not included in this public repository.

Appendix X addressed:
- Structural asymmetries in AI deployment
- Escalation risks linked to power and moral outsourcing
- Internal safety reflection under high-stakes asymmetry

**Appendix X is not part of Haruna v3.2 Public** and remains intentionally excluded.

---

## What Haruna Is (and Isn't)

### Haruna IS:
- A **structured reasoning overlay** for AI systems
- A **cognitive architecture** that embeds time-awareness and consequence-tracking
- A **prompt framework** that shifts AI from answer-generation to question-clarification
- A **collaboration pattern** for human–AI decision-making in high-stakes contexts

### Haruna is NOT:
- An autonomous system or decision-maker
- A set of hard rules or constraints
- A replacement for human judgment
- A product, software, or executable tool

**Haruna operates as a structured orientation overlay** that shifts AI use from blind delegation toward explicit, accountable human–AI collaboration.

---

## Who Should Use Haruna

**You might benefit from Haruna if you:**

- Work in **education** and need AI to support learning (not replace it)
- Do **policy analysis** where unintended consequences matter
- Make **safety-critical decisions** where irreversibility is a factor
- Research **complex problems** where framing determines outcome
- Build **AI systems** and want structural alignment improvements

**You probably don't need Haruna if:**

- You use AI for simple, low-stakes queries
- Consequences are immediate and obvious
- You already have robust decision frameworks
- Speed matters more than thoroughness

---

## Why This Repository Exists

This repository provides a minimal, reproducible artifact set for:

- Reviewers
- Educators  
- Policymakers
- System designers
- AI safety researchers
- Practitioners

**Artifacts include:**

- Prompt overlays usable as system or developer instructions
- Survey cases illustrating misframing and correction  
- Vendor-agnostic examples for loading Haruna as an overlay

**The goal is orientation, not enforcement.**

---

## Getting Involved

**We welcome:**
- Feedback from AI safety researchers
- Testing with different LLMs
- Use case contributions
- Collaboration proposals

**Discussion:**
- GitHub Issues: For technical questions
- Email: m.ederveen@btinternet.com for collaboration inquiries

**Note:** This is an academic research artifact, not a commercial product. There is no support infrastructure, roadmap commitments, or guaranteed maintenance.

---

## Citation

If you use or adapt Haruna, please cite:

**Ederveen, M. (2025).**  
*Haruna: A Reasoning Governance Scaffold for Context-, Time-, and Harm-Aware Artificial Intelligence.*  
Zenodo. https://zenodo.org/records/17709817

**Ederveen, M. (2025).**  
*Haruna: A Temporal–Intent Cognitive Scaffold for Stabilizing Multi-Step Reasoning in Large Language Models.*  
Zenodo. https://zenodo.org/records/18037525

---

## License

**CC-BY 4.0**  
See [LICENSE](LICENSE) or https://creativecommons.org/licenses/by/4.0/

---

## Contact

**Martin Ederveen**  
m.ederveen@btinternet.com

---

**Note:** This framework is not affiliated with any software, media player, or application named "Haruna".
