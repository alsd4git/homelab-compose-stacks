# qBittorrent desired state

`qBittorrent.conf.example` records the reviewed, non-secret preferences from
the running qBittorrent instance. It is deliberately **not** bind-mounted by
Compose: the real `qBittorrent.conf` contains the Web UI credential hash and
mutable state, while `BT_backup/`, categories, RSS feeds, and logs are runtime
data.

Use the file as the source of truth when configuring a new instance or when
reviewing drift through the Web UI/API. Apply individual settings through the
qBittorrent Web API or UI; never overwrite the live configuration wholesale.

## Upload policy

The normal global upload limit is 400 KiB/s. Alternate limits are enabled and
are the live home-safe defaults: 2,000 KiB/s download and 200 KiB/s upload.
`qbit_manage` applies stricter aggregate group caps afterwards: 125 KiB/s for
each private tracker group and 13 KiB/s for the `Public` group. This leaves
headroom on the ADSL uplink while keeping private-tracker policy independent
from the global UI toggle.

## Queueing policy

qBittorrent does not provide active-torrent pools by tracker tag. Its active
upload and active-torrent limits are global, so a public torrent could occupy a
slot needed by a private tracker. Keep `MaxActiveTorrents` and
`MaxActiveUploads` at `0` (unlimited), while retaining `MaxActiveDownloads=10`.
This preserves download queueing without ever queueing a completed private
torrent behind public seeding. Per-tracker upload bandwidth and completion
rules remain enforced by qbit_manage.
