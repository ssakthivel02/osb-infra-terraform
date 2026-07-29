import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
terraform = json.loads((root / 'config/terraform-policy.json').read_text())
cloud = json.loads((root / 'config/cloud-security-policy.json').read_text())

assert terraform['remoteStateRequired'] is True
assert terraform['stateEncryptionRequired'] is True
assert terraform['stateLockingRequired'] is True
assert terraform['providerVersionPinningRequired'] is True
assert terraform['planBeforeApply'] is True
assert terraform['manualProductionApproval'] is True
assert terraform['driftDetectionRequired'] is True
assert terraform['publicAccessDeniedByDefault'] is True
assert cloud['secretManagerRequired'] is True
assert cloud['defaultDenyIngress'] is True
assert cloud['auditLoggingRequired'] is True
assert cloud['productionDeletionProtection'] is True
print('Terraform security baseline validation passed')
