# Terraform Quality Evaluation

Required evidence:
- Formatting, validation and policy checks pass.
- Provider and module versions are pinned and reviewed.
- Remote state is encrypted, locked, access-controlled and recoverable.
- IAM and network policies follow least privilege and default deny.
- Secrets are absent from source, plans, state and logs.
- Production plans receive independent review and approval.
- Drift, backup, restore, failover and rollback exercises pass.
- Cost, quota, capacity and data-classification impacts are approved.

A green static validator is necessary but is not production infrastructure evidence.
