# Mini Duplicate Line Finder

A small Python command-line utility that reports repeated non-empty lines in a UTF-8 text file and shows their occurrence counts.

**Independent demonstration project** · Python 3.10+ · Standard library only · MIT license

## Features

- Reads UTF-8 text, including files with a UTF-8 BOM.
- Ignores whitespace-only lines by default.
- Reports each duplicated line and its count.
- Does not modify the input file.

## Quick start

```bash
python main.py --help
python main.py notes.txt
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Scope and limitations

Lines are compared as text; the tool does not normalize case, punctuation, or internal whitespace. It is intended for simple text review, not semantic duplicate detection. Review any reported match in context before deleting content.

## Related Quantix projects

- [Mini CSV Cleaner](https://github.com/000MAK/mini-csv-cleaner)
- [Mini Text Toolkit](https://github.com/000MAK/mini-text-toolkit)
- [Quantix — 100 Mini Python Projects](https://github.com/000MAK/quantix-100-new-mini-projects)

## Safety

Use synthetic examples in public demonstrations. Do not commit private notes, credentials, or customer material.

## License

MIT. See [LICENSE](LICENSE).
