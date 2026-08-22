# Recyclarr policy

Recyclarr keeps the shared Sonarr/Radarr quality policy declarative. It runs a
daily sync at 04:17 Europe/Rome. Run `recyclarr sync --preview` after policy
changes before deploying them.

`recyclarr.yml`, `settings.yml`, and `secrets.yml` must remain directly in the
mounted `/config` directory. `secrets.yml` is runtime-only and ignored by Git.

The policy defines three profiles, each accepting SD, 480p, 576p, 720p, and
1080p releases for older titles and upgrading up to 1080p when available:

Quality groups are declared in descending preference (1080p through SD).
Recyclarr preserves this order in Arr, so reversing it would make a 720p file
outrank a 1080p file and prevent the intended upgrades.

- `Italian strict SD-1080p` rejects every release without Italian audio.
- `Italian preferred SD-1080p` accepts Italian first, then original-language
  or English releases when Italian is unavailable. Italian receives the higher
  custom-format score at the same quality; Arr quality ordering still takes
  priority over custom-format scores.
- `Anime original/hardsub SD-1080p` accepts Italian, original-language, or
  English releases and is intended for externally acquired anime/hardsub
  material whose language metadata may not be reliable.
- `Original SD-1080p` is reserved for intentional original-language TV
  exceptions. It accepts Italian where present but considers an original or
  English 1080p release complete, avoiding repeated language-upgrade searches.

The first two profiles are deliberately separate: use the strict profile where
Italian is a requirement, and the preferred profile where a higher-quality
original/English fallback is acceptable.

Quality-size floors are intentionally relaxed for compact encodes: Sonarr and
Radarr accept 6 MB/min for 720p WEB/WEBRip/HDTV, 10 MB/min for 720p Blu-ray,
8 MB/min for 1080p WEB/WEBRip/HDTV, and 14 MB/min for 1080p Blu-ray. Remux
limits remain managed by the guide and are not overridden.

Sonarr Italian profiles stop custom-format upgrades at score `71`: Italian has
score `21`, the Italian preference has score `10`, and Italian 1080p has score
`40`. Radarr has no resolution custom formats, so its language target is `31`
(`21 + 10`). Anime stops custom-format upgrades at score `0`; its profile
still upgrades by video quality up to 1080p.

`Subtitles: Italian or English Declared` is an advisory score only. Arr does
not expose a subtitle-media specification, so release-title words cannot prove
embedded subtitles. Keep external anime/hardsub releases out of language-based
remediation; their audio metadata is not authoritative.
