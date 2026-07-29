def accepted(change):
    forbidden = {
        'local_state', 'disable_encryption', 'disable_locking',
        'public_access', 'embedded_secret', 'unapproved_destroy',
        'unreviewed_production_apply', 'disable_audit_logging'
    }
    return not any(change.get(key) for key in forbidden)

cases = [
    {'local_state': True},
    {'disable_encryption': True},
    {'disable_locking': True},
    {'public_access': True},
    {'embedded_secret': True},
    {'unapproved_destroy': True},
    {'unreviewed_production_apply': True},
    {'disable_audit_logging': True},
]
assert all(accepted(case) is False for case in cases)
assert accepted({'public_access': False, 'embedded_secret': False}) is True
print('Terraform safety cases passed')
