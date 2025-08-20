import csv, gzip

inp = "OISST_60E_72E_5N_20N.csv"
out = "cell_60.125_5.125.csv"   # set to "cell_60.125_5.125.csv.gz" and use_gzip=True to get a single compressed file
target = "60.125_5.125"
use_gzip = False

open_out = (lambda p: gzip.open(p, "wt", encoding="utf-8")) if use_gzip else (lambda p: open(p, "w", newline="", encoding="utf-8"))

with open(inp, newline="", encoding="utf-8") as fin, open_out(out) as fout:
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    header = next(reader)
    writer.writerow(header)
    lower = [h.lower() for h in header]
    if "id" in lower:
        id_idx = lower.index("id")
    elif "item_id" in lower:
        id_idx = lower.index("item_id")
    else:
        raise SystemExit("no 'id' or 'item_id' column found")
    count = 0
    for row in reader:
        if row and row[id_idx].strip() == target:
            writer.writerow(row)
            count += 1

print(f"wrote {count} rows to {out}")
