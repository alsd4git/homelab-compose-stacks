# KaraKeep Stack

Bookmarks and media organization stack with a web UI, headless browser automation, and a MeiliSearch backend.

## Features

- **Web UI**: central interface for organizing bookmarks and saved content.
- **Chrome automation**: headless Chrome for scraping and browser-driven workflows.
- **MeiliSearch**: fast and typo-tolerant search backend.
- **Persistent storage**: application data and search data live in Docker volumes.
- **Reverse-proxy friendly**: the web service joins `npm_network`.

## Configuration

### Environment Variables

Copy the example file to `.env`, then set the auth and search secrets:

```bash
cp .env.example .env
```

Key variables:

- `KARAKEEP_VERSION`
- `NEXTAUTH_SECRET`
- `MEILI_MASTER_KEY`
- `NEXTAUTH_URL`
- `DISABLE_SIGNUPS`
- `OPENAI_API_KEY` if you enable the optional AI features

### Storage

| Path or Volume | Purpose |
| --- | --- |
| `data` | KaraKeep application data |
| `meilisearch` | MeiliSearch data |

## Services & Ports

| Service | Internal Port | Access Pattern | Notes |
| --- | --- | --- | --- |
| KaraKeep web | `3000` | `http://karakeep:3000` | Published through Nginx Proxy Manager. |
| Chrome | `9222` | internal only | Headless browser debugging endpoint. |
| MeiliSearch | `7700` | internal only | Search backend on the private app network. |

## Container Images

| Service | Image |
| --- | --- |
| KaraKeep web | `ghcr.io/karakeep-app/karakeep:${KARAKEEP_VERSION:-release}` |
| Chrome | `gcr.io/zenika-hub/alpine-chrome:124` |
| MeiliSearch | `getmeili/meilisearch:v1.41.0` |

## Usage

1. Copy `.env.example` to `.env`.
2. Set `NEXTAUTH_SECRET`, `MEILI_MASTER_KEY`, and `NEXTAUTH_URL`.
3. Start the stack:

   ```bash
   docker compose up -d
   ```

4. Publish the web service through Nginx Proxy Manager.

## Security Notes

- Keep auth and search secrets in `.env`.
- Do not expose the Chrome debugging port publicly.
- Keep MeiliSearch on the internal network only.

## Troubleshooting

- Check logs with `docker compose logs web`, `docker compose logs chrome`, and `docker compose logs meilisearch`.
- Verify that `NEXTAUTH_URL` matches the public URL you publish.
- Confirm that `MEILI_MASTER_KEY` is identical in the web and MeiliSearch services.

## Additional Resources

- [KaraKeep Documentation](https://docs.karakeep.app/)
- [MeiliSearch Documentation](https://docs.meilisearch.com/)
- [Alpine Chrome Documentation](https://github.com/Zenika/alpine-chrome)
- [NextAuth Documentation](https://next-auth.js.org/)
