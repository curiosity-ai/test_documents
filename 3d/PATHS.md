# Path mapping

Dataset (`XRay.3D/dataset/<path>`) to this repository. Everything is identical except these prefixes:

| Dataset prefix | Here |
|---|---|
| `synthetic/` | `3d-synthetic/` |
| `zip/` | `zip-packages/` |
| `khronos/` | `gltf/khronos/` |
| any other `<folder>/` | `<folder>/` (unchanged) |

Per file, see `3d/manifest.json` (`datasetPath` to `file`).

The 32 point cloud, OFF, AMF, DXF, FBX, 3DS, COLLADA, VRML, X3D, USD, compound-file and LAZ fixtures added to the dataset manifest later
(`synthetic/cloud-*.pcd`, `cloud*.las`, `laz-f0..3.laz`, `scene*.{fbx,3ds,dae,wrl,x3d,x3dv,usd*}`, `rich.usd*`, `part.ipt`, `model.rvt`, ...) follow the
same `synthetic/` to `3d-synthetic/` rule and are in `3d/manifest.json` with their generator script and regeneration command in `source`.
