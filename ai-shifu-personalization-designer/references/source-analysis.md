# Source-Assisted Elicitation

Use uploaded or linked teaching materials to reduce recall burden, surface tacit teacher methods, and find candidate personalization decisions. Materials supply evidence and prompts for teacher reflection; they never replace teacher confirmation.

## Offer a Focused Upload

Do not ask the teacher to upload everything. Recommend one to three high-signal materials and explain the tradeoff:

> 你可以先提供 1～3 份最能体现你教学方法的材料。若要萃取个性化教学经验，优先选择同一内容面向不同学员的版本、包含学员提问和现场反馈的视频、有批注或课后反思的教案，以及能体现你如何处理典型错误的答疑或作业讲评。只有一份代表性课程也可以，我们会先提取基础教学风格，再用少量追问补足个性化判断。

For a reusable teacher profile, comparable moments across different courses or teaching contexts can reveal what persists and what is subject-specific. Offer this as a high-value option, not an upload prerequisite. Repeated material from one course supports a within-course pattern, not automatic cross-course generalization.

Reuse materials already available in context instead of asking for another upload.

## Source Priority

Rank sources by their ability to show a learner signal, teacher decision, and observable response:

1. the same concept taught to different audiences or learners;
2. one-to-one coaching, live Q&A, tutoring, feedback, or correction with learner responses;
3. annotated assignments, review records, revised lesson plans, or post-lesson reflections;
4. interactive course recordings with learner questions and teacher adjustments;
5. lesson plans, transcripts, case libraries, and articles that explicitly explain teaching choices;
6. one-way course videos or polished articles;
7. promotional or heavily edited materials.

Lower-priority sources may show tone or presentation habits but rarely justify a personalization rule by themselves.

## Supported Material Handling

- For video or audio, prefer a transcript with timecodes. Use visual evidence only when slide treatment, demonstration, gesture, or learner-visible behavior materially affects the teaching method.
- For lesson plans, documents, slides, or PDFs, retain page, section, paragraph, slide, comment, or revision locators.
- For articles, retain headings and paragraph or quote locations. An article may show stated philosophy but not actual classroom behavior.
- For Q&A, feedback, or annotated work, separate learner input, teacher response, and later learner performance.
- When the environment cannot read a format, ask for a transcript, export, or readable excerpt rather than pretending it was analyzed.

Use available format-specific reading or transcription capabilities only as needed. Do not copy whole source materials into the handoff.

## Authorization and Privacy

Before analysis, confirm or reasonably establish that the user is authorized to provide the material. Ask for clarification only when authorization is genuinely uncertain.

- Exclude or anonymize learner identity unless it is necessary for a legitimate teaching distinction.
- Avoid retaining faces, voices, contact details, grades, diagnoses, or personal stories when an abstract teaching signal is sufficient.
- Do not infer ability, motivation, personality, disability, or diagnosis from appearance or voice.
- Preserve only the minimum source excerpt or locator needed for traceability.

## Two Extraction Layers

### Reusable Teacher Approach and Style

Extract recurring or teacher-confirmed baseline patterns such as:

- explanation and reasoning pattern;
- example and analogy preference;
- scaffolding and hint pattern;
- practice and transfer pattern;
- feedback and correction style;
- language density and tone; and
- professional standards or non-negotiable boundaries.

A single occurrence remains a case or draft hypothesis until supported or confirmed. The profile is more than a neutral tone: extract recurring learning priorities, concrete teaching moves, judgment logic, and conditional changes in support. Identify what would guide course design. Keep repeated wording, content topics, subject-specific procedures, and reusable teaching methods distinct.

### Course-Specific Adaptive Teaching Strategy

Extract a candidate strategy only when the source contains or strongly suggests:

- a learner difference, question, error, goal, constraint, or response;
- a corresponding change in the teacher's explanation, example, scaffold, practice, feedback, deliverable, or path; and
- an observable or teacher-stated reason, effect, or intended outcome.

If only the teaching change is visible, preserve it as a candidate and ask why and when it applies. If only a learner difference is visible, do not invent a teaching response.

Retain learner expression → teacher move → learner response → next adjustment when present. Avoid compressing a rich exchange into “老师擅长鼓励” or an operational checklist. Link the course strategy to the relevant teacher pattern; a useful local technique need not be generalized to all courses.

## Analysis Workflow

1. Record source type, teaching context, audience, authorization status and usable locators. In conversational summaries this can be brief prose; use `source_manifest` only for a structured handoff.
2. Capture atomic observations with their source locators before interpreting them. Use `source_evidence` records when structured output is requested.
3. Classify each record as `stable_style`, `adaptive_strategy`, or `learner_response`.
4. Compare evidence across sources, audiences, versions, and moments. Look for repeated patterns, deliberate contrasts, exceptions, and changes after feedback.
5. Build a candidate teacher profile with concrete methods, scope, and course-design implications; use `teacher_style_baseline` for a structured handoff. Present this synthesis before course rules. Single-context interpretations stay provisional unless the teacher confirms their intended transfer scope.
6. For a requested course, convert relevant adaptive candidates through `references/abstraction-rules.md` and produce the course optimization brief. If no course is selected, finish the profile without inventing an application.
7. Ask only questions the materials cannot answer, especially rationale, applicability boundary, invariant, effectiveness, and exception.
8. Show the teacher the source-backed interpretation in plain language and allow confirmation, correction, rejection, or reclassification.

## Evidence Boundaries

Use these source-specific boundaries:

- `source_explicit`: the teacher states the rationale, method, or boundary in the material;
- `source_observed`: the behavior is directly visible but its rationale is not stated;
- `cross_source_pattern`: the pattern appears across relevant sources;
- `teacher_confirmed`: the teacher confirms the extracted interpretation;
- `ai_inference`: the interpretation is plausible but unconfirmed; or
- `unavailable`: the source cannot support the claim.

Do not upgrade `source_observed` to `teacher_confirmed` or `cross_source_pattern` without evidence.

## Follow-Up Selection

Ask one question per turn using the highest-value unresolved gap:

- visible teaching change but no trigger → ask what the teacher noticed;
- visible trigger and change but no rationale → ask what learning problem the change was meant to solve;
- repeated style pattern but uncertain stability → ask whether it is deliberate and generally applicable;
- stated method but no observed use → ask for a concrete case or keep it as stated philosophy;
- apparent outcome but no comparison or teacher confirmation → ask how the teacher judged effectiveness;
- multiple conflicting patterns → ask what condition determines which method takes priority.

Stop source-assisted questioning when additional source interpretation would not change a teaching decision or when the remaining claim requires learner-time evidence.
