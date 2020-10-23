# pedep

[![image](https://img.shields.io/pypi/v/pedep.svg)](https://pypi.org/project/pedep/) [![image](https://img.shields.io/pypi/pyversions/pedep.svg)](https://pypi.org/project/pedep/) [![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

List PE file dependencies.

## Installation

You can simply use `pip` to install `pedep`:

```
$ pip install pedep
```

## Usage

List PE file dependencies:

```
$ pedep pdftopng.cp38-win_amd64.pyd
Imports for pdftopng.cp38-win_amd64.pyd:
  - MSVCP140.dll
  - python38.dll
  - KERNEL32.dll
  - VCRUNTIME140_1.dll
  - VCRUNTIME140.dll
  - api-ms-win-crt-runtime-l1-1-0.dll
  - api-ms-win-crt-stdio-l1-1-0.dll
  - api-ms-win-crt-string-l1-1-0.dll
  - api-ms-win-crt-heap-l1-1-0.dll
  - api-ms-win-crt-convert-l1-1-0.dll
  - api-ms-win-crt-time-l1-1-0.dll
  - api-ms-win-crt-math-l1-1-0.dll
  - api-ms-win-crt-multibyte-l1-1-0.dll
  - api-ms-win-crt-locale-l1-1-0.dll
  - api-ms-win-crt-filesystem-l1-1-0.dll
  - freetype.dll
  - libpng16.dll
  - jpeg62.dll
  - ADVAPI32.dll
```

List PE file dependencies in JSON format:

```
$ pedep --json file.dll
{
    "pdftopng.cp38-win_amd64.pyd": [
        "MSVCP140.dll",
        "python38.dll",
        "KERNEL32.dll",
        "VCRUNTIME140_1.dll",
        "VCRUNTIME140.dll",
        "api-ms-win-crt-runtime-l1-1-0.dll",
        "api-ms-win-crt-stdio-l1-1-0.dll",
        "api-ms-win-crt-string-l1-1-0.dll",
        "api-ms-win-crt-heap-l1-1-0.dll",
        "api-ms-win-crt-convert-l1-1-0.dll",
        "api-ms-win-crt-time-l1-1-0.dll",
        "api-ms-win-crt-math-l1-1-0.dll",
        "api-ms-win-crt-multibyte-l1-1-0.dll",
        "api-ms-win-crt-locale-l1-1-0.dll",
        "api-ms-win-crt-filesystem-l1-1-0.dll",
        "freetype.dll",
        "libpng16.dll",
        "jpeg62.dll",
        "ADVAPI32.dll"
    ]
}
```

List PE file dependencies recursively by providing a DLL directory for dependency lookups:

```
$ pedep --dll-dir C:\path\to\dll\directory file.dll
Imports for pdftopng.cp38-win_amd64.pyd:
  - MSVCP140.dll
  - python38.dll
  - KERNEL32.dll
  - VCRUNTIME140_1.dll
  - VCRUNTIME140.dll
  - api-ms-win-crt-runtime-l1-1-0.dll
  - api-ms-win-crt-stdio-l1-1-0.dll
  - api-ms-win-crt-string-l1-1-0.dll
  - api-ms-win-crt-heap-l1-1-0.dll
  - api-ms-win-crt-convert-l1-1-0.dll
  - api-ms-win-crt-time-l1-1-0.dll
  - api-ms-win-crt-math-l1-1-0.dll
  - api-ms-win-crt-multibyte-l1-1-0.dll
  - api-ms-win-crt-locale-l1-1-0.dll
  - api-ms-win-crt-filesystem-l1-1-0.dll
  - freetype.dll
  - libpng16.dll
  - jpeg62.dll
  - ADVAPI32.dll

Imports for freetype.dll:
  - zlib1.dll
  - bz2.dll
  - libpng16.dll
  - brotlidec.dll
  - VCRUNTIME140.dll
  - api-ms-win-crt-convert-l1-1-0.dll
  - api-ms-win-crt-string-l1-1-0.dll
  - api-ms-win-crt-utility-l1-1-0.dll
  - api-ms-win-crt-environment-l1-1-0.dll
  - api-ms-win-crt-stdio-l1-1-0.dll
  - api-ms-win-crt-heap-l1-1-0.dll
  - api-ms-win-crt-runtime-l1-1-0.dll
  - KERNEL32.dll

Imports for zlib1.dll:
  - VCRUNTIME140.dll
  - api-ms-win-crt-stdio-l1-1-0.dll
  - api-ms-win-crt-heap-l1-1-0.dll
  - api-ms-win-crt-convert-l1-1-0.dll
  - api-ms-win-crt-runtime-l1-1-0.dll
  - KERNEL32.dll

Imports for bz2.dll:
  - VCRUNTIME140.dll
  - api-ms-win-crt-stdio-l1-1-0.dll
  - api-ms-win-crt-heap-l1-1-0.dll
  - api-ms-win-crt-runtime-l1-1-0.dll
  - api-ms-win-crt-string-l1-1-0.dll
  - api-ms-win-crt-math-l1-1-0.dll
  - KERNEL32.dll

Imports for libpng16.dll:
  - zlib1.dll
  - VCRUNTIME140.dll
  - api-ms-win-crt-heap-l1-1-0.dll
  - api-ms-win-crt-stdio-l1-1-0.dll
  - api-ms-win-crt-math-l1-1-0.dll
  - api-ms-win-crt-runtime-l1-1-0.dll
  - api-ms-win-crt-convert-l1-1-0.dll
  - api-ms-win-crt-filesystem-l1-1-0.dll
  - api-ms-win-crt-time-l1-1-0.dll
  - KERNEL32.dll

Imports for brotlidec.dll:
  - brotlicommon.dll
  - VCRUNTIME140.dll
  - api-ms-win-crt-heap-l1-1-0.dll
  - api-ms-win-crt-runtime-l1-1-0.dll
  - KERNEL32.dll

Imports for brotlicommon.dll:
  - VCRUNTIME140.dll
  - api-ms-win-crt-heap-l1-1-0.dll
  - api-ms-win-crt-runtime-l1-1-0.dll
  - KERNEL32.dll

Imports for jpeg62.dll:
  - VCRUNTIME140.dll
  - api-ms-win-crt-environment-l1-1-0.dll
  - api-ms-win-crt-heap-l1-1-0.dll
  - api-ms-win-crt-stdio-l1-1-0.dll
  - api-ms-win-crt-runtime-l1-1-0.dll
  - KERNEL32.dll
```

## Versioning

`pedep` uses [Calendar Versioning](https://calver.org/). For the available versions, see the tags on the GitHub repository.

## License

This project is licensed under the Apache License, see the [LICENSE](https://github.com/vinayak-mehta/pedep/blob/master/LICENSE) file for details.
