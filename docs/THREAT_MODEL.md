# Infrastructure Threat Model

## Protected assets
Cloud accounts, state files, credentials, networks, workloads, logs, backups and tenant data.

## Principal threats
- State-file disclosure or tampering
- Privilege escalation through over-broad IAM
- Public exposure of private services
- Secret leakage in code, plans or logs
- Unreviewed destructive changes
- Supply-chain compromise in providers or modules
- Drift from approved configuration
- Backup failure or unrecoverable regional outage

## Required controls
Encrypted and locked remote state, least privilege, private networking, version pinning, signed and reviewed changes, secret management, policy scanning, drift detection, immutable audit, deletion protection, backups and recovery exercises.
