# EXT.to — no safe Cardigann download flow

Verified on 2026-07-31.

The previously examined custom definition is obsolete: search results no longer
contain a magnet or infohash directly in the markup, and direct HTTP requests
receive HTTP 403. ByParr can render the search page, but it does not solve the
download flow.

Each result exposes `a.search-magnet-btn[data-id]`. The browser obtains the
magnet through `POST /ajax/getSearchMagnet.php`, sending `torrent_id`,
`timestamp`, `searchPageToken`, a session cookie, and an HMAC-SHA256 signature
of `torrent_id|timestamp|searchPageToken`.

Cardigann cannot execute that JavaScript or create the signed,
session-bound request. Do not implement a partial definition that returns an
unusable download link.

If needed in the future, build a dedicated browser-backed Torznab adapter that
returns both results and valid magnets; otherwise keep EXT.to manual.
