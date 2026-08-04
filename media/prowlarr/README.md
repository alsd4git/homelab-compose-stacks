# Prowlarr custom-indexer research

This directory records custom Cardigann-definition experiments for Italian
sources. It is deliberately versioned so that a future maintainer has the
evidence, limitations, and next steps rather than having to rediscover them.

## Deployment policy

- Definitions in [`custom-definitions`](custom-definitions/README.md) are
  **not a supported automatic-indexer set**. Copying a file into Prowlarr's
  `Definitions/Custom` directory is a manual action and must follow the status
  shown here.
- Never commit credentials, browser cookies, API keys, private tracker passkeys,
  or host-specific paths. Configure credentials only in Prowlarr.
- An indexer that has not passed the documented test must not be saved or
  synchronized to Sonarr/Radarr.

## Current status

| Source | Status | Intended use | Evidence |
| --- | --- | --- | --- |
| TNT Village Database | working | Manual/recovery search only | [note](research/tntvillage-db.md) |
| ilCorSaRo | blocked | None | [note](research/ilcorsaro.md) |
| iCV-CreW | blocked | None | [note](research/icv-crew.md) |
| EXT.to | not implemented | Manual only | [note](research/ext-to.md) |
| ilDraGoNeRo 2 | not implemented | Manual only | [note](research/ildragonero2.md) |
| MIRCrew multi-release topics | known limitation | Avoid automatic episodic grabs | [note](research/mircrew-multi-release.md) |

`blocked` means the failure was reproduced in Prowlarr and the definition must
not be enabled. `not implemented` means there is no safe Cardigann definition
yet. “Manual” means using the source in a browser, not enabling it in Sonarr or
Radarr.

## General limitation

Cardigann maps one search result to one download. Forum topics that contain
multiple independent magnets cannot be expanded into one Torznab release per
episode. Solving that correctly requires a dedicated adapter which parses the
topic and publishes individual Torznab results.
