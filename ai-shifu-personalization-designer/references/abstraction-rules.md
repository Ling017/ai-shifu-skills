# Abstraction Rules

Convert concrete teacher cases into reusable teaching decisions without erasing context, overgeneralizing, or building rigid learner types.

## Unit of Abstraction

Use two linked units, neither of which is a persona or content summary.

**Teacher pattern:** learning purpose → characteristic teaching moves → judgment for changing approach → scope and invariants → implications for course design.

**Course decision:**

`observable signal → teaching hypothesis → teaching adjustment → invariant → verification signal → insufficient-information fallback`

A course rule also records its relationship to the teacher profile and may include modifiers, exceptions, rationale, and teaching response or stopping conditions when relevant.

## Synthesize the Teacher's Approach

Cluster episodes by teaching purpose or decision logic, not just by course topic. Preserve the teacher's distinctive judgments without claiming they are unique among teachers. A useful description makes a design choice possible:

- Weak: “温暖、实用、善于启发。”
- Actionable illustrative pattern: “先让学员说明判断依据，再根据卡点给最少必要支持；能解释依据后撤去提示，让其独立迁移。纠错时指出具体推理缺口，不替学员完成整题。”

The illustration is not a default philosophy to impose on every teacher. Different teachers may deliberately demonstrate first or use direct correction. Capture the supplied method and its purpose.

Distinguish three things: stable priorities, conditional teaching stances, and course-specific techniques. For example, using a prototype is a subject-specific technique; shifting from verbal explanation to a concrete artifact when a learner can recognize but cannot articulate a goal may be a reusable teaching pattern. The generalization needs teacher review; do not infer it automatically.

For each substantial pattern, make clear what a course designer should do differently. “鼓励学员” is insufficient; a supported pattern might imply feedback that names a valid attempt, isolates one correctable error, and offers a bounded retry. Reconstructed dialogue is illustrative, not observed speech or proof of learning effects.

## From Case to Rule

1. Preserve the teacher's original case as evidence, removing unnecessary identifying details. When the case comes from uploaded material, retain its `source_evidence_ids` rather than copying the full source.
2. Separate what was directly observed from what the teacher or AI inferred.
3. Identify the smallest learner difference that actually caused a different teaching decision.
4. Express the teacher's adjustment as a concrete action: what changes in example, terminology, scaffolding, emphasis, depth, practice, feedback, deliverable, or path.
5. Record why the teacher believes the adjustment helps.
6. State the knowledge, quality standard, safety boundary, or required outcome that remains fixed.
7. Define an observable sign that the adjustment has worked.
8. Test the rule against an exception, counterexample, or missing-information case.
9. Ask the teacher to approve, revise, reject, or leave the rule unresolved.

Source-observed behavior shows what happened, not necessarily why it happened. Keep an unstated trigger, rationale, or effectiveness claim unresolved until supported or confirmed. Put reusable teaching logic, including conditional stance changes, in `teacher_style_baseline`; express its specific course application in `decision_rules`. Link them, rather than copying identical descriptions at both levels. A course-specific rule can have no profile link if it is genuinely local; explain why instead of fabricating a teacher trait.

## Course Optimization Synthesis

After deriving rules, summarize the meaningful teaching changes, grouped by learning bottleneck rather than rule count. Each recommendation should say which teacher pattern it applies, which learner evidence changes the teaching move, what learners do themselves, when support changes, and what remains constant.

If a course exists, point to the relevant learning moment and distinguish an observed issue from an inferred opportunity. Without course material, supply proposed design guidance, not a claim that a lesson is deficient. Do not turn the brief into rewritten course prompts.

Preserve contrast through the full teaching sequence: a branch that initially gives different support must not be silently flattened by a later universal template or full answer. Respect author constraints on interaction and sequence. Describe the intended teaching change and any conflict; leave concrete authoring and runtime choices to the receiver.

## Relevance Gate

Do not include a learner attribute merely because it is available. It must change at least one legitimate teaching decision.

Reject or defer rules such as:

- “Young learners prefer visual content” when no evidence or teaching decision is supplied.
- “Beginners need more examples” when beginner status, example selection, and intended effect are undefined.
- “The learner likes short answers, so omit the required reasoning.”

Retain rules such as:

- “When the learner can perform the operation but cannot explain the decision boundary, use a counterexample and require a reasoned classification before advancing.”

## Multi-Dimensional Decisions

Avoid a Cartesian product of learner types. Represent a complex case as:

- one `primary_signal` that triggers the teaching change;
- zero to two `modifiers` that tune expression or task context; and
- zero or more `hard_constraints` that cannot be ignored.

Default evidence priority, unless the case justifies another order:

1. current performance evidence;
2. explicit learner goal, constraint, or accessibility need;
3. relevant prior experience and context;
4. preference, interest, or self-reported confidence;
5. neutral course-appropriate default.

Accessibility, safety, and regulated requirements may override this default priority.

## Adaptation Classes

Classify each change under one or more of:

- `example`
- `terminology`
- `prerequisite_scaffolding`
- `emphasis`
- `explanation_depth`
- `explanation_sequence`
- `questioning`
- `support_fading`
- `practice`
- `feedback`
- `deliverable`
- `authored_path`
- `course_structure`

Do not label a generic intention such as “personalize more” as an adaptation. Classify actual teaching moves by their function; do not put every adjustment into `practice`. Not every rule needs several categories: a valid task-only adaptation can remain, but cannot stand in for a full teacher-method profile.

## Delivery-Independent Requirements

Describe what teaching must accomplish and how the learner participates. Where relevant, specify the signal, teacher action, required learner response, when support changes, completion evidence and behavior after an incomplete attempt. Use the optional teaching-response shape in the handoff contract when it helps.

Describe information by its meaning, availability and later learning use. For example, "Later practice uses the learner's confirmed goal; distinguish the first attempt from revisions when assessing improvement." The receiving workflow selects how to collect and retain it.

Keep platform syntax, tool names, variable keys, artifact placement and capability labels out of the design. A method can remain valuable even if a receiver cannot implement it; the receiver reports the gap and a possible teaching alternative.

## Conflict Handling

When two rules conflict:

1. preserve hard professional, safety, accessibility, and factual constraints;
2. prefer current observed performance over a static profile assumption;
3. prefer the rule more directly connected to the current learning objective;
4. use the teacher-defined priority when supplied; and
5. otherwise use the neutral fallback and record the conflict as unresolved.

## Approval Standard

A rule may be approved only when the teacher has seen a plain-language rendering of:

- trigger signal and information source;
- teaching hypothesis and its evidence boundary;
- actual adjustment and rationale;
- invariant;
- verification signal;
- exception or fallback for insufficient information; and
- required teaching response, input waiting, completion and incomplete-outcome behavior where relevant.
- source locators and whether the interpretation is explicit, observed, cross-source, teacher-confirmed, or inferred when materials were used.

Approval confirms the design faithfully represents the teacher's intended method. It does not prove educational effectiveness or platform implementation.
