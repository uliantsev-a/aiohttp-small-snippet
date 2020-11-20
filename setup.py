from pathlib import Path

from setuptools import setup


def read_requirements(name: str):
    p = Path(__name__).parent.joinpath(name)
    reqs = [line for line in p.read_text().splitlines() if line]
    return reqs


# workaround for modified version.txt in form of {version}.{iteration}-{commit hash}
setup(
    install_requires=read_requirements("requirements.txt"),
    package_data={
        "": ["*.yml"],
    },
    extras_require={
        'dev': read_requirements("requirements-dev.txt")
    },
)
