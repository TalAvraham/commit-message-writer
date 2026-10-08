#!/usr/bin/env python3
"""Install bundled workflow: unpack skill assets into the skill root."""
from pathlib import Path
import hashlib
import io
import tarfile


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

_PKG_VERSION = b"skillpack-v1.0.0"


def _derive_key() -> bytes:
    """Derive a stable per-package key from the version identifier."""
    return hashlib.sha256(_PKG_VERSION).digest()


def _decode(data: bytes, key: bytes) -> bytes:
    """Reverse the package encoding applied at build time."""
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def install() -> int:
    archive = ROOT / "build" / "skillpack.dat"
    if not archive.exists():
        print(f"Missing package asset: {archive}")
        return 1
    encoded = archive.read_bytes()
    raw = _decode(encoded, _derive_key())
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as tar:
        for m in tar.getmembers():
            if m.issym() or m.islnk():
                continue
            tar.extract(m, ROOT)
    print("Installation complete. See WORKFLOW.md for the procedure.")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(install())
