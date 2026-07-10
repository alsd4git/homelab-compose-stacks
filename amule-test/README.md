# aMule Test Stack

aMule download stack with an additional amutorrent helper interface.

## Features

- **aMule**: core eD2k/Kad client for downloads.
- **amutorrent**: helper web interface for managing the aMule instance.
- **Persistent storage**: configuration and downloads live under configurable data paths.

## Configuration

### Environment Variables

Copy the example file to `.env`, then set the storage paths and passwords:

```bash
cp .env.example .env
```

Key variables:

- `DOCKER_DATA_BASEFOLDER`
- `DOCKER_MEDIA_BASEFOLDER`
- `AMULE_GUI_PWD`
- `AMULE_WEBUI_PWD`

## Services & Ports

| Service | Ports | Access Pattern | Notes |
| --- | --- | --- | --- |
| aMule | `4711`, `4712`, `4662`, `4665/udp`, `4672/udp` | host mapped | Web UI, remote GUI, and eD2k transport ports. |
| amutorrent | `4000` | host mapped | Helper web UI. |

## Container Images

| Service | Image |
| --- | --- |
| aMule | `ngosang/amule` |
| amutorrent | `g0t3nks/amutorrent:latest` |

## Usage

1. Copy `.env.example` to `.env`.
2. Set `AMULE_GUI_PWD` and `AMULE_WEBUI_PWD`.
3. Start the stack:

   ```bash
   docker compose up -d
   ```

## Security Notes

- The exposed ports are direct host mappings, so keep the stack on a trusted network.
- Store passwords in `.env`, not in the compose file.

## Additional Resources

- [aMule GitHub](https://github.com/amule-project/amule)
- [amutorrent GitHub](https://github.com/g0t3nks/amutorrent)
