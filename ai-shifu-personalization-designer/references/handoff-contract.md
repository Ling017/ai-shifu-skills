# Personalization Design Handoff Contract

This platform-neutral teaching contract carries a reusable teacher profile and, when requested, its course application. Version `3.0` describes teaching decisions and required learning behavior without choosing runtime syntax, tools, prompt artifacts, storage, or a delivery platform. Its version is independent of platform and engine versions. Any model, human teacher, or course authoring workflow can consume it.

This reference defines structured output, not a mandatory format for conversational elicitation or plain-language summaries.

## Top-Level Shape

```yaml
personalization_design:
  contract_version: "3.0"
  design_scope: teacher_profile | course_design
  status: draft | approved

  teacher_profile:
    profile_id: teacher_001
    version: "1.0"
    status: draft | approved
    teaching_contexts: []
    characteristic_summary: "How this teacher helps people learn, not a subject outline"
    applicability: "Contexts supported or explicitly intended, and boundaries"
    generalization_basis: observed_across_contexts | teacher_confirmed_scope | provisional_single_context | unknown

  course_context:
    topic: ""
    intended_audience: ""
    learning_objective: ""
    fixed_constraints: []

  relevant_dimensions: []
  source_manifest: []
  source_evidence: []
  teacher_style_baseline: []
  teacher_evidence: []
  decision_rules: []
  course_optimization_brief: []
  information_collection_plan: []
  unresolved_hypotheses: []

  teacher_confirmation:
    confirmed_style_ids: []
    rejected_style_ids: []
    confirmed_rule_ids: []
    rejected_rule_ids: []
    confirmed_profile_version: ""
    confirmed_optimization_ids: []
    profile_confirmation_note: ""
    confirmation_note: ""
```

Use `status: approved` only for the explicitly confirmed requested scope, following `validation.md`. Profile approval and course approval are distinct; neither implies measured learning effectiveness.

## Scope and Reuse

- In `teacher_profile` scope, use `course_context: null` and empty `relevant_dimensions`, `decision_rules`, `course_optimization_brief`, and `information_collection_plan`. Do not invent a course just to fill the object. The teacher profile is a legitimate final deliverable.
- In `course_design` scope, require a real course context and profile snapshot/version. Derive and confirm the applicable course rules and optimization brief separately; profile approval alone cannot approve a course design.
- The reusable profile consists of `teacher_profile`, `teacher_style_baseline`, their referenced teacher/source evidence, and their scoped confirmation records. Reuse this bounded snapshot in later courses; do not re-interview or silently change its scope.
- Preserve profile id and version on unchanged reuse. Changes to its methods or intended scope create a new version in `draft` until explicitly confirmed. Do not update previous courses automatically.
- A course design may use a confirmed subset of a larger profile. Retain ids and source version, state the subset in the confirmation note, and carry unused/unconfirmed patterns as unresolved or omit them; do not claim the original full profile was approved.

## Relevant Dimensions

Each item contains:

```yaml
- dimension: background_context | prior_level | goal_outcome | misconception_performance | preference_motivation | constraints_accessibility | learning_response
  relevance: "How this dimension may change a teaching decision in this course"
  evidence_sources: []
```

Include only dimensions relevant to the current design. Do not include an empty universal checklist.

## Source Manifest

When materials are used, register each source without copying its full content:

```yaml
- source_id: source_001
  source_type: video | audio | transcript | lesson_plan | article | slides | qa | annotated_work | feedback | other
  title: ""
  teaching_context: ""
  audience_context: ""
  locator_scheme: timecode | page | slide | section | paragraph | item_id | other
  authorization_status: confirmed | public | unclear
```

Do not include source-derived evidence from a source whose authorization remains `unclear` in an approved design.

## Source Evidence

Each atomic source-backed observation contains:

```yaml
- evidence_id: se_001
  source_id: source_001
  locator: "Timecode, page, slide, section, paragraph, or item id"
  observed_content: "Minimum description needed to understand the teaching evidence"
  extraction_type: stable_style | adaptive_strategy | learner_response
  evidence_boundary: source_explicit | source_observed | cross_source_pattern | teacher_confirmed | ai_inference | unavailable
  confidence: low | medium | high
```

The locator must let a reviewer find the evidence in the supplied source. Do not store unnecessary learner identity or long source excerpts.

## Teacher Style Baseline

Despite the retained key name, this is the teacher's reusable pattern library, not merely a neutral tone when no trigger applies. Include stable priorities, concrete teaching methods, and conditional changes of stance. Each pattern contains:

```yaml
- style_id: style_001
  dimension: teaching_judgment | learning_sequence | explanation | example | scaffolding | practice | feedback | language_tone | professional_invariant
  pattern: "A teacher characteristic stated as an actionable teaching pattern"
  learning_purpose: "Learning need this method serves"
  teaching_moves: []
  conditional_variations:
    - learner_signal: ""
      teaching_interpretation: "Teacher judgment, not an asserted learner fact"
      changed_move: ""
      adjustment_or_fading_signal: "When to deepen, change, or withdraw support"
      evidence_boundary: teacher_explicit | source_observed | teacher_confirmed | ai_inference
  expression_examples:
    - situation: ""
      teacher_response: "Short example of an actual teaching move, not merely tone"
      provenance: source_quote | teacher_recollection | illustrative_reconstruction
      evidence_ids: []
  invariants: []
  applicability: "Where this is useful and where not to transfer it"
  generalization_basis: observed_across_contexts | teacher_confirmed_scope | provisional_single_context | unknown
  course_design_implications: []
  source_case_ids: []
  source_evidence_ids: []
  evidence_boundary: cross_source_pattern | teacher_confirmed | teacher_explicit | ai_inference
  confidence: low | medium | high
  confirmation: draft | confirmed | rejected
```

A single source occurrence cannot use `cross_source_pattern`. Repeated clips from one course do not by themselves establish transfer across courses. `teacher_explicit` records a teacher statement but is not blanket approval of the synthesized profile. A general principle can be explicitly confirmed as intended across contexts without claiming observed success across them.

Omit empty `conditional_variations` and `expression_examples` when they do not help; do not manufacture adaptations for an invariant. Every confirmed pattern needs a learning purpose, concrete moves, applicability, evidence trace, and at least one actionable course-design implication. Keep rationale/effectiveness uncertainties explicit.

## Teacher Evidence

Each anonymized evidence item contains:

```yaml
- case_id: case_001
  teaching_context: ""
  observed_signals: []
  teacher_actions: []
  teaching_exchange:
    learner_expression: ""
    teacher_response: ""
    learner_response: ""
    next_teacher_move: ""
    provenance: source_quote | teacher_recollection | illustrative_reconstruction | unavailable
  teacher_rationale: ""
  observed_outcome: ""
  evidence_boundary: observed | teacher_recollection | proposed_example | unknown
  source_evidence_ids: []
```

An empty or unverified `observed_outcome` is allowed. `teaching_exchange` may be partial or omitted when unavailable; do not invent dialogue to fill it. Illustrative reconstruction never counts as independently observed effectiveness or teacher evidence unless separately reviewed for intended-method fidelity.

## Decision Rule

Each rule contains:

```yaml
- rule_id: pd_001
  teacher_pattern_ids: []
  local_rule_reason: "Explain only when no teacher pattern applies"
  applicable_scope: "course, module, lesson, concept, task, or condition"

  primary_signal:
    description: "Observable trigger"
    source: learner_explicit | teacher_observation | performance_evidence | teacher_experience_pattern | ai_inference | unavailable

  modifiers: []
  hard_constraints: []

  teaching_hypothesis:
    statement: "Provisional teaching interpretation"
    evidence_boundary: observed | teacher_inference | ai_inference

  adaptations:
    example: []
    terminology: []
    prerequisite_scaffolding: []
    emphasis: []
    explanation_depth: []
    explanation_sequence: []
    questioning: []
    support_fading: []
    practice: []
    feedback: []
    deliverable: []
    authored_path: []
    course_structure: []

  rationale: "Why this adjustment should address the learning need"
  learner_agency: "What the learner still judges or does, rather than AI completing it"
  adjustment_or_fading_signal: "When support should change; state if not applicable"
  invariants: []
  verification_signals: []
  exceptions: []
  unknown_fallback: "Neutral behavior when the signal is unavailable or unreliable"
  teaching_response: # Optional rule-local object; see Teaching Response and Completion
    initial_move: "What to do first, when a response sequence is needed"

  source_case_ids: []
  source_evidence_ids: []
  confidence: low | medium | high
  confirmation: draft | confirmed | rejected
```

Remove empty adaptation keys when rendering the final object. Every approved rule requires at least one non-empty adaptation, invariant, verification signal, unknown fallback, and source case, source evidence, or explicit teacher statement.

## Course Optimization Brief

For `course_design`, group recommendations by teaching purpose, not one row per rule:

```yaml
- optimization_id: opt_001
  learning_moment: "Module, concept, task, or interaction; no invented lesson numbers"
  current_evidence_or_gap: "Observed issue, inferred opportunity, or proposed new design"
  basis: observed_course | teacher_report | proposed_design
  teacher_pattern_ids: []
  rule_ids: []
  intended_teaching_change: "What the course should teach differently, not just what content to add"
  learner_contrast: "Same objective, differing signals → differing teacher and learner actions"
  preserved_standard: ""
  acceptance_check: "Observable teaching contrast or support change in a sample lesson/dialogue"
  confirmation: draft | confirmed | rejected
```

Every approved recommendation needs valid profile/rule references (at least one), an actionable change, and an acceptance check. Recommend rather than execute. Without course material, use `proposed_design`; do not pretend to audit unseen lessons. Reconstructed examples illustrate intended behavior, not runtime test results.

## Information Collection Plan

Specify information required by approved rules and how it could become available:

```yaml
- information: ""
  used_by_rule_ids: []
  availability: already_available | learner_self_report | lesson_performance | teacher_provided | unavailable
  collection_timing: before_learning | early_learning | at_relevant_activity | later_activity | not_collected
  reuse_scope: current_activity | later_activities
  consumed_at: [] # Named learning moments that need this information
  record_distinctions: [] # e.g. learner first attempt vs revised answer vs teacher demonstration
  reason: "Why this information is necessary"
```

Do not recommend collection when the information does not change a decision. `later_activities` needs named consumers in `consumed_at`; retain only what those activities need. Describe whether the latest corrected value suffices or distinct attempts are pedagogically necessary. Do not prescribe variables, keys, tools, storage scopes, or technical persistence. Collection timing describes learning moments, not a required platform workflow.

## Unresolved Hypotheses

Record useful but unconfirmed ideas instead of silently converting them into rules:

```yaml
- hypothesis_id: ph_001
  statement: ""
  missing_evidence: []
  risk_if_assumed: ""
  next_validation: ""
```

## Teaching Response and Completion

When a rule needs repeated teaching or new learner input, put the following optional object at `personalization_design.decision_rules[i].teaching_response`, inside the rule it describes. Do not place it at the top level, on the whole design, or in the teacher profile. The inline Decision Rule example above abbreviates this object; this section defines its fields. Omit it for a genuine invariant or simple non-interactive adaptation.

```yaml
# Inside one item of decision_rules:
teaching_response:
  initial_move: "What the teacher first explains, demonstrates, or asks"
  response_branches:
    - learner_signal: ""
      teacher_move: ""
      learner_action: "What the learner still does"
      continue_when: "Evidence needed to move on"
  input_requirement: "When an actual new learner answer must be received before continuing"
  support_adjustment: "When to add, change, or withdraw help"
  retry_or_exit_policy: "If relevant: bounded retry or another teacher-chosen stopping rule"
  completion_evidence: []
  incomplete_outcome: "What remains unobserved or incomplete after exit"
```

These are teaching requirements, not tool calls or executable syntax. No universal retry count, questioning sequence, or technical memory requirement applies. Unknown stopping rules remain unresolved; never invent teacher practice to fill the shape. Distinguish receiving an explanation, assisted completion, independent performance, and transfer.

## Receiver Responsibilities

A handoff is usable without installing this skill. Carry the profile id/version, selected patterns, evidence boundaries, confirmation state, required teaching actions, information consumers, and behavioral acceptance criteria with the design.

The receiver:
- chooses its own authoring format, runtime controls, artifacts, tools, storage and deployment workflow;
- maps only selected, applicable methods into the requested course scope;
- preserves required learning goals, facts, learner agency, teaching contrasts, and uncertainty;
- checks whether it can wait for new input, retain required information, and support the intended feedback or exit behavior;
- reports implemented, adjusted, unsupported and unverified parts, with affected rule/pattern ids;
- explains a capability gap and offers an equivalent teaching alternative where possible; material changes to learning purpose or method require resolution with the author under the current task authority.

The receiver does not need to invoke this skill for ordinary course work. This skill does not need a receiver to complete a profile. Profile `course_design_implications` are selection guidance, not mandatory global instructions. Publishing and other external operations remain governed by the receiving workflow and the user's scope.

## Version Compatibility

Accept `1.0`, `1.1` and `2.0` inputs as source material. Preserve teacher/profile ids, evidence, scoped confirmations and unknowns. Reformatting alone does not reconfirm a profile or broaden its approved scope.

For a `2.0` design:
- move legacy `implementation_classes` and platform mappings out of the teaching contract into optional receiver-owned implementation notes;
- translate `persistence_need` into pedagogical `reuse_scope`, named consumers and necessary record distinctions;
- treat `UNKNOWN` as insufficient information, without assuming any engine's substitution value;
- preserve existing method content without manufacturing response loops or broader applicability;
- list unmapped or ambiguous fields explicitly instead of discarding them.

Emit `3.0` for new structured designs. A receiving workflow may use the accompanying readable teaching brief without a schema parser. Do not force a schema migration or a separate profile interview on every course task. Structural compatibility is not proof of executed teaching or learning effectiveness.
