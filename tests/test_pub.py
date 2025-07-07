from pathlib import Path

from daml import pub
from daml.publications import city_10_weeks


def test_city_10_weeks(tmp_path: Path) -> None:
    pub_dir = tmp_path / "pub"
    pub_dir.mkdir()

    for _, v in city_10_weeks.BUILD.items():
        print(f"BUILD: {v}")
        pub.build_lecture(v, pub_dir=str(pub_dir))
