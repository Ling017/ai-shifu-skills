---
name: ai-shifu-personalization-designer
description: Elicit or summarize a teacher's reusable teaching approach, judgment, and style from experience or materials, then apply that profile to differentiated teaching in a specific course. Use for teacher-method extraction, personalized teaching design, or guidance for course optimization. Can produce a teacher profile without a course. Does not author or deploy courses or merely imitate tone.
metadata:
  version: "3.0.1"
---

# AI-Shifu Personalization Designer

First capture how this teacher helps people learn across teaching contexts; then derive how that approach should change for learners in a particular course. The result must guide teaching optimization, not just summarize content, label learners, or imitate wording.

## Two-Layer Design

1. **Teacher layer:** A reusable, evidence-bounded profile of teaching priorities, reasoning and explanation habits, diagnosis, scaffolding, feedback, and conditional changes in teaching stance. Describe what the teacher does and why, not just adjectives such as warm or practical. A stable characteristic may be a decision pattern, not an identical behavior toward everyone.
2. **Course layer:** Select relevant profile patterns for this course's objectives and learner evidence; derive concrete teaching adjustments and an optimization brief. Preserve common outcomes and professional standards. Do not transfer every teacher habit to every course.

Build or reuse the teacher layer before deriving course rules. A concrete lesson can supply evidence without defining the profile's whole scope. With no course selected, finish a `teacher_profile` design without inventing a course. With an existing profile, reuse its version and review applicability instead of interviewing from scratch. A single-course inference is provisional, not proven across courses.

## Responsibility Boundary

This Skill owns:

- guided elicitation and synthesis of reusable teacher characteristics and learner-dependent methods;
- evidence-aware abstraction into personalization decision rules;
- teacher review and approval of those rules; and
- the versioned `personalization_design` handoff, including teacher profile and, when requested, course-specific optimization guidance.

This Skill produces platform-neutral teaching designs for models, human teachers, or any delivery system. It does not author executable course artifacts, choose runtime syntax, prescribe storage or tools, or deploy content. A receiving author or implementation workflow translates the design into its own environment. No other skill or platform documentation is required to extract a profile or finish a design. A receiver can clarify a specific teaching ambiguity without starting a circular re-interview.

Keep these three controls separate:

1. `personalization_design`: the teacher's reusable approach and how learner differences change course teaching decisions;
2. delivery-system expression controls, if any: selected by the receiving workflow; and
3. interaction policy: what learner information the course collects and when.

## Working Modes

Choose the smallest useful mode and load only the guidance needed now:

- **Source-assisted elicitation:** For teaching materials, read [source analysis](references/source-analysis.md). Add [elicitation guidance](references/elicitation-workflow.md) only for a material gap the sources cannot answer.
- **Guided elicitation:** For tacit experience or an ongoing interview, read [elicitation guidance](references/elicitation-workflow.md). Ask one useful question, then wait; no output schema or full audit is needed for each interview turn.
- **Direct abstraction or refinement:** Use the supplied cases or existing profile directly. Read [abstraction rules](references/abstraction-rules.md) when synthesizing methods, resolving conflicts, or selecting course adaptations. Do not re-interview already supplied facts.
- **Structured output or legacy migration:** Read [handoff contract](references/handoff-contract.md) only when producing a structured handoff, interpreting an old structured design, or resolving a field question. A plain-language profile does not require it.
- **Completed deliverable review:** Read the relevant sections of [validation](references/validation.md): teacher/source checks for a profile, course checks for a course application, and approval checks when recording approval. Do not run a full course audit for an interview or profile-only task.

Natural-language summaries are the default. Use the output template only for a durable profile/design document that benefits from its structure; omit inapplicable sections.

## Core Workflow

1. Reuse relevant information already present in the conversation, source material, course context, or an existing design. Do not ask the teacher to repeat it. When materials are available, register their type, teaching context, authorization status, and usable locator before extracting claims.
2. Establish the teacher's relevant teaching contexts and any existing profile. Use a representative incident as an entry, not a mandatory single-course anchor or persona questionnaire.
3. Recover a teaching episode: learner expression or behavior, teacher interpretation, actual teaching moves and language, reason, learner response, and next adjustment. Use contrast or a failed usual method when helpful; ask one high-value question per turn, not a fixed field checklist.
4. Synthesize teacher-level patterns from episodes. State learning purpose, concrete method, when the teacher changes support or stance, boundaries, and implications for course design. Present this profile first for correction; do not stop merely because one local rule is complete.
5. If a course is in scope, map the relevant profile patterns to its learning bottlenecks and real learner signals. Differentiate teaching process as well as content or task choice. Produce concrete optimization guidance without writing course prompts.
6. Show representative contrasting teaching moves or short illustrative dialogue when it helps the teacher recognize the method. Label reconstructed examples and AI interpretations; never pass them off as recorded teacher speech.
7. Before final delivery, check fidelity, scope, and confirmation using the applicable validation sections. During elicitation, retain these boundaries without loading a complete audit per turn. Teacher-profile approval does not approve its application to every course.
8. Match the requested deliverable: use concise natural language for interview turns and ordinary summaries; return a structured handoff plus readable summary only when requested or required by the agreed receiving interface. For a durable profile/design document, use the applicable parts of [the template](assets/personalization-design-template.md) when useful. Present teacher-level methods before any course application.

## Non-Negotiable Rules

- A learner attribute enters the design only when it can change teaching. Background, level, goal, preference, and current response are flexible lenses, not required profile fields.
- Distinguish subject-matter procedure (how to do the task) from pedagogy (how the teacher helps this learner learn to do it). Preserve useful task adaptations, but do not present them alone as the teacher's full approach.
- Prefer current performance evidence and explicit goals or constraints over stereotypes inferred from identity or background.
- Treat a teaching hypothesis as a hypothesis. Never rewrite it as a learner fact.
- Preferences may shape delivery where pedagogically appropriate, but they do not override the learning objective, factual accuracy, safety, accessibility, or common professional standard.
- Preserve rich teacher experience independently of delivery capability. State required observable teaching behavior and information use; the receiver assesses feasibility and reports gaps without silently changing the method.
- Avoid combinatorial learner-type catalogs. Use a primary observable signal, limited modifiers, and explicit conflict priorities.
- Every approved rule has an invariant, a verification signal, and behavior for insufficient information. Unknown is a teaching state, not a required runtime sentinel.
- Remove or anonymize unnecessary personal details from teacher examples.
- Recommend one to three high-signal materials before asking for a broad upload. Prefer comparable versions, real learner interaction, annotated work, Q&A, or teacher reflection over polished promotional content.
- Source material may demonstrate what the teacher did, but it does not prove why the teacher did it or that it worked. Keep rationale and effectiveness as unconfirmed until supported or confirmed by the teacher.
- Trace source-derived claims to locators and interview-derived claims to cases or identifiable teacher statements. Generalizing across courses needs evidence across contexts or explicit teacher confirmation of intended scope; confirmation is not measured effectiveness.
- Analyze only materials the user is authorized to provide. Minimize or anonymize learner names, faces, voices, contact details, performance records, and personal stories not required for the teaching decision.
- Use the user's requested language for questions, summaries, and human-readable values while preserving contract keys and enum values exactly.

## Output

Use concise natural language by default; an ongoing interview may end with one question rather than a completed design. For a requested structured handoff, produce one `personalization_design` object under contract `3.0` in `references/handoff-contract.md`, plus a readable summary. A conversational summary may use plain language with the same evidence and scope boundaries; do not require JSON for ordinary elicitation. Cover:

- reusable teacher characteristics, teaching decision patterns, and their scope/evidence limits;
- how the teacher's way of teaching changes with learner signals, illustrated where useful;
- for a course design: selected patterns, specific teaching changes, preserved standards, and observable acceptance criteria;
- scope-specific approvals, unresolved hypotheses, and any required learner-time information.

Do not claim that course content, platform configuration, or learner-time personalization has been implemented. Report the actual draft or approved state; a profile-only handoff is not authorization to modify a course. Contract migration and consumer responsibilities are defined in `references/handoff-contract.md`. Keep delivery mappings in the receiving workflow, not this skill. The contract version is independent of every engine, platform, or course-creation skill version.
