"""Check the built artifact independently of the developer's bench path."""
from email.parser import BytesParser
from pathlib import Path
from zipfile import ZipFile

wheel, = Path("dist").glob("*.whl")
with ZipFile(wheel) as archive:
    metadata_name, = [n for n in archive.namelist() if n.endswith(".dist-info/METADATA")]
    metadata = BytesParser().parsebytes(archive.read(metadata_name))
    assert metadata["Name"].replace("_", "-") == "frappe-better-select-control", metadata["Name"]
    assert metadata["Version"], "Missing version"
    for requirement in metadata.get_all("Requires-Dist", []):
        assert "file:" not in requirement.lower(), requirement
        assert "/home/" not in requirement, requirement
    assert "frappe_better_select_control/public/js/better_select.bundle.js" in archive.namelist(), "Runtime bundle missing"
print("Built wheel is portable and contains the runtime bundle")
