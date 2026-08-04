# ilDraGoNeRo 2 — preliminary manual-only assessment

Verified on 2026-07-31 with an account-owner browser session.

- The site is phpBB and title searches use `search.php?keywords=...&sf=titleonly`.
- Downloads require the releaser's `Grazie` action. A post can then expose one
  or more links.
- The tested historical Evangelion release exposed an `mgnet.me` short-link,
  not a magnet or `.torrent` file. A non-downloading HTTP check resolved that
  historical link to an unrelated destination.

Do not create a Prowlarr definition around opaque short-links: Prowlarr and a
download client would not receive a verifiable torrent payload.

To revisit, test a recent release whose post-`Grazie` link resolves directly to
a magnet or `.torrent`, then determine whether JavaScript, cookies, or CAPTCHA
are required before considering automated indexing.
