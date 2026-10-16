# Working with this fork

Upstream: [SumoLogic/sumologic-documentation](https://github.com/SumoLogic/sumologic-documentation).

## What is specific to this fork

- The root README identifies ownership, points to the official documentation, and maps the local source tree.
- [UPSTREAM_README.md](UPSTREAM_README.md) preserves the original overview and credits.
- Inherited build, publishing and branch-environment deletion jobs are gated to the upstream repository. They do not run against cloud resources from this fork.
- [Fork documentation checks](.github/workflows/fork-checks.yml) verify the links in the root README and this guide without requiring deployment credentials or building the full site.

## Updating from upstream

Review upstream changes on a separate branch before merging them. Preserve local ownership notes and fork guards when resolving workflow changes. Upstream source, lockfile and license are otherwise retained by this cleanup.

A documentation-link check is not a full Docusaurus build or a dependency-security assessment. Run the project's build in a suitable environment before proposing changes to the site implementation or content rendering.
