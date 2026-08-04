# Experimental Cardigann definitions

These files are research artifacts, not a blanket deployment directory.

| Definition | Status | Deployment rule |
| --- | --- | --- |
| `tntvillage-db.yml` | verified | Add to Prowlarr with a `manual-only` sync profile only. |
| `ilcorsaro.yml` | blocked | Do not add: SMF session verification rejects Prowlarr's login flow. |
| `icv-crew.yml` | blocked | Do not add: Cloudflare blocks requests and ByParr times out. |

The corresponding evidence and follow-up work are in the parent
[research notes](../README.md#current-status). Credentials belong solely in
Prowlarr and must never be added to these files.
