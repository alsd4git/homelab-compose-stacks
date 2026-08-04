# MIRCrew — multi-release topic limitation

Verified on 2026-07-31 with the Silo topic `t=226850`.

Sonarr can identify a requested episode, but a Cardigann definition returns one
forum topic and its `download` block selects the first magnet after the
`Grazie` action. When the topic contains several episodes, the first magnet
(often E01) can be returned even when Sonarr requested a later episode.

Sonarr cannot correct this: it receives one Torznab release and one magnet, not
the complete list contained in the forum topic.

## Required solution

A correct implementation needs a dedicated Torznab adapter that searches the
topic, performs the required access step, associates every magnet with its
episode or season-pack metadata, and publishes each as a separate release.

Until then, avoid automatic episodic grabs from multi-release MIRCrew topics.
Existing indexer reliability is also affected by intermittent login,
rate-limit, and Cloudflare/solver failures; do not broaden its automation
scope based on a generic magnet selector.
