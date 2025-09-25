#!/usr/bin/env python3
#  GU +3 (000-500) + 4 (2020-2025)
# 2500 words

outfile = "ID.txt"
with open(outfile, "w") as f:
    for a in range(0, 500):           # 000..499
        a_str = f"{a:03d}"
        for b in range(2020, 2025):      # 001..999
                f.write(f"GU{a_str}{b:04d}\n")
print(f"Wrote {outfile}")
