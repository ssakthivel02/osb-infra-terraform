# Terraform Operations Runbook

1. Confirm repository, workspace, account, region, environment and change owner.
2. Run formatting, validation, security, policy and dependency checks.
3. Generate a fresh plan against locked remote state.
4. Review IAM, networking, encryption, public access, deletion and cost impact.
5. Require independent approval for production or destructive changes.
6. Apply only the reviewed plan using short-lived workload identity.
7. Verify resources, health, audit logs, backups and monitoring after apply.
8. Record plan, approvals, apply result, drift status and rollback evidence.

Never place credentials, tokens, private keys or sensitive data in Terraform variables, state, plans, logs or comments.
