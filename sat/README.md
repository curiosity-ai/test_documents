# sat

Test files for the 3D / CAD readers of X-Ray.3D (curiosity-ai/x-ray-others, `XRay.3D/`). Every file is listed in the dataset
manifest, which is copied machine-readable to `3d/manifest.json` (paths relative to this repository root). The files are third-party
data (or generated fixtures) used as published: their bytes and sha256 must not be changed. Mapping from the dataset layout: `3d/PATHS.md`.

Licences in this folder: Public domain (US government work, NIST).

| File | Title | Licence | Source | Bytes | sha256 |
|---|---|---|---|---|---|
| `nist-arm-blank.sat` | NIST arm blank, ACIS 1.5 save (105) | Public domain (US government work, NIST) | NIST engineering design models (via the public cq-acis test corpus) | 4709 | `d3477a71195fc5650975314551bf621def89fdbd1752602d9bc6e12a279a0d2d` |
