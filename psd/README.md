# PSD and PSB fixtures

Test files for [X-Ray.Psd](https://github.com/curiosity-ai/x-ray-others/tree/main/XRay.Psd), the
PSD/PSB reader and compositor of the [X-Ray](https://github.com/curiosity-ai/x-ray) family.

## This folder

Photoshop-saved documents (`photoshop-*.psd`, `photoshop-*.psb`, `arrows.psd`,
`qual_rca_pinout.psd`), documents written by Patchy itself (`patchy-*`), and the Photoshop
reference captures of their renders (`*.bmp`, one beside each document it belongs to;
`photoshop-blend-if-4b-render.bmp` is the capture of `photoshop-blend-if-4b-roundtrip.psd`).

They come from the PSD test fixtures of Patchy, the C++ image editor X-Ray.Psd was ported from:
[`.reference/test-fixtures/psd`](https://github.com/theolivenbaum/Patchy/tree/main/.reference/test-fixtures/psd)
in [theolivenbaum/Patchy](https://github.com/theolivenbaum/Patchy). They are covered by Patchy's
MIT License, copyright (c) 2026 Seth A. Robinson; the full text is in `LICENSE` here.

## `psd-tools/`

Small single-feature files (16 and 32-bit depths, grayscale, indexed, Lab, duotone, multichannel
and bitmap modes, an embedded PSB smart object, layer comps, guides, slices) from
[psd-tools](https://github.com/psd-tools/psd-tools), commit
`605ee1284952c18c649ba60ebe73df4dabca9fbb`, `tests/psd_files/`. Their paths are kept relative to
that folder. Copyright (c) 2019 Kota Yamaguchi, MIT License; the full text is in
`psd-tools/LICENSE` and the attribution in `psd-tools/NOTICE`.

## `ag-psd/`

`text-path.psd` is `test/read/text-path/src.psd` from
[ag-psd](https://github.com/Agamnentzar/ag-psd), version 31.0.3: the one Photoshop file in the
corpus with type on a path. Copyright (c) 2016 Agamnentzar, MIT License; the full text is in
`ag-psd/LICENSE`.
