# DeckHub Decky Plugin 1.0.1

**Made for gamers. By a gamer.**

This source package includes the DeckHub splash artwork (`src/splash.png`) and displays it in the DeckHub plugin panel. The Rollup URL plugin embeds the PNG into the compiled bundle, so the artwork does not need a separate runtime file.

## Features
- Decky Quick Access plugin panel for Steam Gaming Mode
- DeckHub splash branding
- Search and category filtering
- Add/remove launcher shortcuts
- Python backend launches configured commands
- Persists shortcuts in `~/.config/deckhub/launchers.json`

## Build on Steam Deck or compatible Linux
Install Node.js and pnpm, then from this directory run:

```bash
pnpm install
pnpm run build
```

The build should produce `dist/index.js`. This archive is the updated source package; it is not a precompiled installable Decky release. Build and test it on the Deck before installing. Decky plugin APIs and dependencies can change, so treat the first build as a local test.

## Security
Launcher commands execute as your SteamOS user. Only add commands you trust.
