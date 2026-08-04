# ilCorSaRo — blocked Cardigann login

Verified on 2026-08-01 with a Prowlarr indexer form populated by the account
owner. Credentials were not read or stored in the repository.

## Result

The search endpoint is reachable, but Prowlarr cannot establish an authenticated
SMF session. Its login POST to `index.php?action=login2` includes the dynamic
hidden fields scraped from the form, but the forum returns HTTP 403 with
`Sessione di verifica fallita`. Subsequent searches return the unauthenticated
login page, so Cardigann correctly finds zero releases.

Changing the session duration to a value offered by the form and using a known
search term (`Evangelion`) did not change the result. This rules out an empty
test query and ordinary credential failure as the observed cause.

## Decision

Do not add or sync `ilcorsaro.yml`. A cookie-based definition would require
manual cookie renewal and is not a reliable automation solution.

## If revisited

Reproduce the login request with a browser-backed client and compare its cookie,
origin, and session behavior with Prowlarr. If the forum cannot accept a
non-browser session, keep the source manual instead of adding a fragile indexer.
