# Recyclarr policy

Recyclarr keeps the shared Sonarr/Radarr quality policy declarative. It runs a
daily sync at 04:17 Europe/Rome. Run `recyclarr sync --preview` after policy
changes before deploying them.

`recyclarr.yml`, `settings.yml`, and `secrets.yml` must remain directly in the
mounted `/config` directory. `secrets.yml` is runtime-only and ignored by Git.

The policy defines three profiles, each accepting SD, 480p, 576p, 720p, and
1080p releases for older titles and upgrading up to 1080p when available:

- `Italian strict SD-1080p` rejects every release without Italian audio.
- `Italian preferred SD-1080p` accepts Italian first, then original-language
  or English releases when Italian is unavailable. Italian receives the higher
  custom-format score at the same quality; Arr quality ordering still takes
  priority over custom-format scores.
- `Anime original/hardsub SD-1080p` accepts Italian, original-language, or
  English releases and is intended for externally acquired anime/hardsub
  material whose language metadata may not be reliable.

The first two profiles are deliberately separate: use the strict profile where
Italian is a requirement, and the preferred profile where a higher-quality
original/English fallback is acceptable.

`Subtitles: Italian or English Declared` is an advisory score only. Arr does
not expose a subtitle-media specification, so release-title words cannot prove
embedded subtitles. Keep external anime/hardsub releases out of language-based
remediation; their audio metadata is not authoritative.
