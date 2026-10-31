# Security policy

## Reporting a vulnerability

Use [GitHub private vulnerability reporting](https://github.com/alsd4git/homelab-compose-stacks/security/advisories/new).
Do not disclose exploit details or sensitive data in public issues or pull requests.

Include the affected commit or version, expected impact and minimal reproduction
steps. Use synthetic examples and redact screenshots and logs. If a credential
has been exposed, revoke or rotate it before sharing details.

## Versions and maintenance

Check the current default branch, `main`, and, if using a release,
the latest release published by this repository before reporting an issue.
Fixes, when provided, target the default branch. Older versions do not receive
separate backports. Reports are handled on a best-effort basis without guaranteed
response or remediation times.

## Safe reproduction

Reports should concern the configuration and scripts maintained here. Use example environments; never attach .env files, live credentials, private hostnames or unredacted service logs. Vulnerabilities in container images or third-party services belong with their upstream maintainers.
