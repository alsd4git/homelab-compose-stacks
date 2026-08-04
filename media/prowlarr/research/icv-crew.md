# iCV-CreW — blocked by Cloudflare

Verified on 2026-08-01 with a Prowlarr indexer form populated by the account
owner. Credentials were not read or stored in the repository.

## Result

The forum search request receives Cloudflare's `Just a moment…` response
(HTTP 403) before forum authentication is reached. Prowlarr detects this and
forwards the request to ByParr. ByParr's browser session waits for `networkidle`
while resolving the challenge, times out, and returns HTTP 500 to Prowlarr.

This is not a category, parser, or credential issue. Direct requests are
blocked before the SMF forum can process them.

## Additional parsing limitation

A forum topic can contain several magnets, one per episode or episode group.
Cardigann can return one download per result only, so even a working definition
would be suitable for films, individual releases, and complete season packs;
it would not be safe for automatic episodic searches.

## Decision

Do not add or sync `icv-crew.yml`. Revisit only if the site no longer presents
the Cloudflare challenge to the automation client, or if a stable browser-backed
Torznab adapter is available.
