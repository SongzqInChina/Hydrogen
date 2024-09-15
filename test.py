from src import HydrogenLib

toml_text = '''
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "HydrogenLib"
dynamic = ["version"]
description = ''
readme = "README.md"
requires-python = ">=3.12.0"
license = "MIT"
keywords = []
authors = [
  { "name" : "SongzqInChina", "email" : "142714722+SongzqInChina@users.noreply.github.com" },
]
classifiers = [
  "Development Status :: 4 - Beta",
  "Programming Language :: Python",
  "Programming Language :: Python :: 3.12",
  "Programming Language :: Python :: Implementation :: CPython",
  "Programming Language :: Python :: Implementation :: PyPy",
]
dependencies = [
  "jsonpickle >= 3.3.0",
  "pywin32 >= 306",
  "pyaes >= 1.6.0",
  "rsa >= 4.9",
  "psutil >= 6.0.0"
]

[project.urls]
Documentation = "https://github.com/SongzqInChina/HydrogenLib#readme"
Issues = "https://github.com/SongzqInChina/HydrogenLib/issues"
Source = "https://github.com/SongzqInChina/HydrogenLib"


[tool.hatch.version]
path = "src/HydrogenLib/__about__.py"

[tool.hatch.envs.types]
extra-dependencies = [
  "mypy>=1.0.0",
]
[tool.hatch.envs.types.scripts]
check = "mypy --install-types --non-interactive {args:src/HydrogenLib tests}"

[tool.coverage.run]
source_pkgs = ["HydrogenLib", "tests"]
branch = True
parallel = True
omit = [
  "src/HydrogenLib/__about__.py",
]

[tool.coverage.paths]
HydrogenLib = ["src/HydrogenLib", "*/HydrogenLib/src/HydrogenLib"]
tests = ["tests", "*/HydrogenLib/tests"]

[tool.coverage.report]
exclude_lines = [
  "no cov",
  "if __name__ == .__main__.:",
  "if TYPE_CHECKING:",
]
[tool.hatch.build]
target="wheel"
'''
# print(
#     HydrogenLib.EnhanceToml.parser.find_tables(toml_text)
# )

res = HydrogenLib.EnhanceToml.parser.decode(
    toml_text
)
print(res)
