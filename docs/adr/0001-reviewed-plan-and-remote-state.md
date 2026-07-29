# ADR 0001: Reviewed plans and trusted remote state

## Decision
All environments use encrypted, access-controlled and locked remote state. Production applies must use a fresh reviewed plan and short-lived workload identity. Local state, direct console changes and unreviewed applies are not authoritative.

## Consequences
Drift is detected and reconciled through code. Destructive changes require explicit approval. State access, plans, applies and recovery actions are auditable.
