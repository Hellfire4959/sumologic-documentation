# Sumo Logic documentation — personal fork

This is **Hellfire4959's fork** of [SumoLogic/sumologic-documentation](https://github.com/SumoLogic/sumologic-documentation). It contains the inherited Docusaurus documentation source. The official published documentation is [help.sumologic.com](https://help.sumologic.com/); changes in this fork do not publish to that site.

## Find your way around

| Path | Contents |
| --- | --- |
| [docs/](docs/) | Product and contributor documentation |
| [docs/contributing/index.md](docs/contributing/index.md) | Contributor guide in this snapshot |
| [i18n/](i18n/) | Translated documentation |
| [src/](src/) | Docusaurus components and styling |
| [static/](static/) | Static site assets |
| [package.json](package.json) | Build and development commands |
| [FORK_NOTES.md](FORK_NOTES.md) | Fork workflow, validation scope and synchronization notes |
| [UPSTREAM_README.md](UPSTREAM_README.md) | Original upstream overview retained for attribution and historical context |

## Local preview

Use the Node version recorded in [.nvmrc](.nvmrc) and the Yarn lockfile. This is a legacy snapshot; the recorded Node version is not a recommendation for a new production deployment.

```bash
git clone https://github.com/Hellfire4959/sumologic-documentation.git
cd sumologic-documentation
nvm install
nvm use
yarn install --frozen-lockfile
yarn start
```

For a production-style local build and preview:

```bash
yarn build
yarn serve
```

The preview normally listens at `http://localhost:3000/`. The complete repository includes many assets and translations, so installation and a full build can be substantial. A complete Docusaurus build was not part of the README/navigation cleanup.

## Contribute

Follow [CONTRIBUTING.md](CONTRIBUTING.md) and the [official contributor guide](https://help.sumologic.com/docs/contributing/). Use a branch and pull request for fork-specific changes. Submit changes intended for the official documentation to the upstream repository under its contribution process.

## License

The inherited [MIT license](LICENSE) and original copyrights remain in place. Fork-specific automation checks documentation links without running the upstream deployment workflow; see [FORK_NOTES.md](FORK_NOTES.md).
