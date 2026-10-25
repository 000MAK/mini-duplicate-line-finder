import argparse,collections
from pathlib import Path

def find_duplicates(path, ignore_blank=True):
    lines=Path(path).read_text(encoding="utf-8-sig").splitlines()
    if ignore_blank: lines=[line for line in lines if line.strip()]
    counts=collections.Counter(lines)
    return {line:count for line,count in counts.items() if count>1}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("input"); a=ap.parse_args(); duplicates=find_duplicates(a.input)
    if not duplicates: print("No duplicate lines found."); return
    for line,count in duplicates.items(): print(f"{count}x: {line}")
if __name__=="__main__": main()
