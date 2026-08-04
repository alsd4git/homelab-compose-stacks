# TNT Village Database — verified manual archive

Verified on 2026-07-31.

The site exposes a historic TNT Village dump. Search is a GET request using
`?search=<term>` and result rows contain a title, size, and a `.torrent` URL
derived from the infohash. The accompanying Cardigann definition passed
Prowlarr's test and returned releases.

It must remain **manual/recovery only**:

- the archive has no trustworthy seed, leech, or release-date data;
- its catalogue mixes films, TV, music, books, software, and incomplete
  metadata, so categories are not safe for *arr automation;
- historic torrents can have zero seeders and create stalled download queues.

Use the `manual-only` Prowlarr sync profile and do not synchronize it to Sonarr
or Radarr. A manual grab is appropriate only after checking swarm availability.
