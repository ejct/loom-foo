# Source Evidence Profiles

## INTERNAL_PROJECT
Strong for authority, history, audits, failures, implementation context. Risks: stale proposals, contradictory docs, selective retrieval. Check current authority and supersession.

## PUBLIC_IMPLEMENTATION
Strong for observed mechanisms/interfaces/tests/config. Weak for hidden rationale/generalizability. Separate `OBSERVED_MECHANISM`, `AUTHOR_CLAIM`, `INFERRED_RATIONALE`, `TRANSFER_HYPOTHESIS`.

## RESEARCH
Strong for hypothesis/method/population/result. Check external validity, uncertainty, limitations, replication/systematic-review status, and benchmark-to-production gap.

## STANDARD_SPEC
Strong for normative contracts/interoperability. Compliance does not prove local product fit.

## VENDOR_PRACTICE
Strong for platform constraints/supported APIs. Risk: provider-specific optimization mistaken for general principle.

## POSTMORTEM
Strong for concrete failure paths and latent assumptions. Transfer failure lessons before copying local remediation.

## PRODUCT_OBSERVATION
Strong for observable behavior/UX/packaging. Internals/rationale are inferred unless independently evidenced.

## USER_EVIDENCE
Strong for problems, behaviors, constraints. Individual evidence does not automatically generalize to broad requirements.
