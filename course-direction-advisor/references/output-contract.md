# Output contract v2

Human reports use natural language. Include decision, reasons, actual analysis mode and coverage, target market, source boundaries, evidence, uncertainty, and next useful step.

## Outcomes
- Recommended: supported primary; meaningful alternatives only if available.
- Pending validation: provisional primary or none, missing evidence, and what resolves the decision.
- Not recommended: primary optional, rejection scope/reasons, narrower alternatives only if supported.

No quotas for backups, competitors, or risks. Scores, price, growth forecasts, MVP, and seven-day plans are optional. A plan is not execution evidence.

## Structured delivery
Use [v2 schema](course-direction-advisor.schema.v2.json) only for requested/needed machine output. Canonical required keys are schema_version, analysis_mode, report_language, target_markets, research_status, result_status, decision_status, decision_reason, directions, evidence, claims, missing_info, risks, next_steps.

Evidence IDs have source type, locator, summary; market observations also need URL, observation date, and market. Claim refs must resolve to evidence IDs. Missing evidence goes in missing_info, not fabricated refs. Validate cross-reference resolution and factual support in addition to JSON structure.

## Migration
v2 intentionally changes the old v1 field layout. The preserved v1 schema is historical, not the active contract. Existing consumers must explicitly migrate; never silently label v1 payloads v2. Human outputs do not require fixed filenames or JSON.

For a full readable memo, adapt decision-report-template.md. Explain objective, promise, teacher advantage, and teaching sufficiency without expanding into course authoring.
