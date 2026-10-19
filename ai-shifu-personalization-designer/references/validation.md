# Validation

Apply only the checks relevant to the requested completed deliverable. An interview turn does not require a full report or completed design. Use teacher/source checks for a profile, add rule/course checks for a course design, and use approval checks only when recording approval. Report material gaps and keep unconfirmed designs in `draft`.

## Teacher-Profile Checks

- **Method, not adjectives:** substantial patterns state learning purpose, concrete moves, applicability, and usable course-design implications. Merely “温暖、实用、启发式” does not pass.
- **Pedagogy, not content inventory:** distinguish how to perform the subject task from how this teacher helps learners understand, judge, practice, or transfer it. Task procedures alone are insufficient for a full profile.
- **Conditional style:** when evidence supports differentiated methods, show what the teacher notices and how support, challenge, explanation, or feedback changes. Do not require variation for a genuine invariant or invent missing episodes.
- **Transfer scope:** distinguish within-course recurrence, observed patterns across contexts, and teacher-confirmed intended applicability. One course does not automatically prove generality.
- **Evidence fidelity:** the synthesis and sample language distinguish observed material, teacher recollection, and AI reconstruction. Unknown motivations and outcomes stay unknown.
- **Recognizable teaching:** the teacher can recognize or correct the characteristic choices in a concrete episode; do not claim the method is unique to this teacher.
- **Reusable identity:** profile id/version, applicability, evidence links, and profile confirmation are preserved on reuse. New generalizations require review.

A profile-only deliverable needs no invented course or learner information plan. If evidence is insufficient for a complete profile, return the useful bounded draft and the highest-value gap rather than filling categories.

## Rule-Level Checks

For every decision rule, verify:

- **Decision relevance:** the learner information changes at least one legitimate teaching decision.
- **Observable trigger:** the primary signal can be stated without relying only on a stereotype or broad persona label.
- **Evidence boundary:** explicit statements, observations, performance, teacher pattern, and AI inference remain distinguishable.
- **Teacher traceability:** the rule points to a teacher case or explicit teacher statement.
- **Concrete adaptation:** the rule says what changes and for what teaching purpose.
- **Profile relationship:** valid teacher-pattern links or a clear reason why the rule is course-local.
- **Teaching agency:** the teacher and learner roles are explicit; where relevant, specify what changes or removes support instead of only producing a more complete answer.
- **Professional invariant:** factual, quality, safety, accessibility, and required-outcome boundaries remain explicit.
- **Effectiveness evidence:** at least one observable verification signal exists; unobserved effectiveness is not claimed as proven.
- **Boundary:** exceptions or non-applicable conditions are represented when material.
- **Unknown behavior:** a neutral fallback for insufficient information prevents unsupported inference.
- **Structured response placement:** when present, `teaching_response` belongs to its item in `decision_rules`, not the whole design or teacher profile. This is relevant only to structured course designs.
- **Delivery independence:** requirements describe observable teacher/learner behavior, not syntax, storage or platform capability. Necessary new input is actually awaited; completion and incomplete outcomes are explicit when relevant.
- **Teacher confirmation:** the teacher approved the rendered meaning, not merely a learner label.

## Independence Checks

- The profile or teaching design can be understood and completed with no course-creation skill installed.
- No runtime syntax, engine version, platform tool or storage key is required to interpret new design fields.
- Structured contract versions refer only to this handoff, never to a similarly numbered delivery engine.
- A receiver may use plain-language evidence and behavior criteria; structured output is not a prerequisite for unrelated course work.
- Legacy implementation fields are preserved in receiver-owned migration notes when needed, not mistaken for teaching requirements.

## Source-Level Checks

When materials were used, verify:

- every source has a type, teaching context, locator scheme, and non-unclear authorization before contributing to an approved design;
- every source-derived claim points to a valid `source_evidence` record and usable locator;
- `observed_content` describes only the minimum evidence needed and excludes unnecessary learner identity;
- stable style and adaptive strategy are not conflated;
- a single occurrence is not called a stable style unless the teacher confirms it;
- source-observed behavior does not silently acquire an invented trigger, rationale, or effectiveness result;
- cross-source claims actually use more than one relevant source or comparison;
- articles and stated philosophy are distinguished from observed teaching behavior;
- edited or promotional material is not treated as complete evidence of teaching sequence or learner response; and
- unreadable or unavailable material is reported as unassessed rather than analyzed by assumption.

## Design-Level Checks

Verify:

- only relevant information dimensions are included;
- the design does not attempt to complete a universal learner profile;
- current performance and explicit goals normally outrank static profile assumptions;
- preference does not override learning objectives or professional standards;
- multi-dimensional rules use primary signals and limited modifiers instead of a combinatorial persona catalog;
- conflicts have a priority, neutral fallback, or unresolved record;
- information collection is proportional to its teaching use;
- every request to reuse information later names an actual learning consumer and any necessary distinction between attempts;
- unnecessary identifying details are removed from teacher cases;
- source materials are minimized in the handoff and remain traceable through locators rather than copied wholesale;
- every approved teacher pattern has traceable evidence and explicitly confirmed meaning and applicability; draft generalizations are not misrepresented as approved;
- unresolved or weakly supported ideas remain in `unresolved_hypotheses`;
- every included rule has a unique id and retains traceable teaching meaning without platform-specific implementation fields; and
- the top-level status matches the confirmation records.

## Course Optimization Checks

For `course_design`, verify that the optimization brief:

- applies selected teacher methods to real objectives and learning moments, without claiming to inspect unavailable course text;
- distinguishes content/task customization from changes to teaching process, and includes the latter when supported by the teacher's evidence;
- explains the different teacher/learner actions for a meaningful contrast under a common objective;
- preserves that contrast through later steps instead of undoing it with a universal full answer, template, or interaction;
- gives an observable acceptance check, not only a rule-to-lesson mapping or syntax check;
- marks interaction/sequence changes requiring separate approval, rather than adding unauthorized runtime questions; and
- does not treat a static design review, illustrative dialogue, or teacher approval as a real learner experiment.

Do not impose a category quota. If all adaptations are task-only, explicitly report that teaching-process personalization is still under-extracted or unsupported rather than claiming comprehensive teacher-method capture.

## Approval Gate

Approve the teacher profile only when profile/source/design checks pass, there is at least one supported actionable pattern, every included pattern is `confirmed` and listed in `confirmed_style_ids`, and the teacher explicitly confirms the profile's meaning and scope. Record the exact version in `confirmed_profile_version` and the approval in `profile_confirmation_note`. No approved source evidence may depend on unclear authorization.

For `design_scope: teacher_profile`, top-level approval covers only this profile. Course context must be null and course-only collections empty.

For `design_scope: course_design`, top-level approval additionally requires:

1. an approved applicable profile snapshot or explicitly confirmed subset, with correct version and evidence;
2. real course context and at least one relevant rule and actionable optimization recommendation;
3. all rule and course optimization checks pass;
4. all included rules and recommendations are `confirmed`, with their ids in `confirmed_rule_ids` and `confirmed_optimization_ids`; and
5. the teacher explicitly confirms this course application after seeing the teacher-to-course mapping and teaching contrasts.

A previously approved profile may remain approved while a new course application is draft. Conversely, old course approval cannot approve new teacher-level generalizations. Rejected or unresolved candidates do not participate in approved pattern/rule/recommendation lists.

Rejected rules remain out of the approved `decision_rules` list and may be recorded in `rejected_rule_ids`. Unresolved rules remain under `unresolved_hypotheses`.

## Handoff Report

Scale the report to the task. For an ordinary summary, state the useful teaching methods, their source/scope, important unknowns, and the next useful action if any. Do not attach counts, a full audit checklist, or protocol bookkeeping to every interview turn.

For a formal profile or course handoff, include its status and profile id/version, evidence/confirmation boundaries, required information reuse, applicable acceptance checks, and any material gaps. Counts of sources, rules or hypotheses are optional when they help the recipient. Course optimization and receiving-workflow details apply only when a course is in scope.

A report describes the work actually completed. Never report "personalization implemented" from this Skill alone.
