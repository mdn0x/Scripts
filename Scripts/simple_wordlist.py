#!/usr/bin/env python3
#  GU + 4 (0000-9999) + 3 (001-999)

outfile = "Id_long.txt"
with open(outfile, "w") as f:
    for a in range(0, 10000):           # 0..9999
        a_str = f"{a:04d}"
        for b in range(1, 1000):      # 001..999
                f.write(f"GU{a_str}{b:03d}\n")
print(f"Wrote {outfile}")
