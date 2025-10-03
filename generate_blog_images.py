# generate_blog_images.py
import os
import matplotlib.pyplot as plt
import numpy as np

os.makedirs("blog_images", exist_ok=True)

# 1) SQL: OFFSET vs Keyset latency
pages = [1, 5, 10, 20, 30, 40, 50]
offset_ms = [120, 260, 520, 1350, 2300, 3050, 3800]
keyset_ms = [130, 135, 140, 145, 150, 155, 160]

plt.figure(figsize=(8, 4.5))
plt.plot(pages, offset_ms, marker="o", label="OFFSET pagination")
plt.plot(pages, keyset_ms, marker="o", label="Keyset (cursor) pagination")
plt.title("SQL: Page Latency vs Page Number")
plt.xlabel("Page number")
plt.ylabel("Latency (ms)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("blog_images/sql-pagination-latency.png", dpi=160)
plt.close()

# 2) Postgres bloat/autovacuum trend (example data)
days = list(range(1, 15))
dead_tuples_millions = [1.1, 1.3, 1.6, 2.1, 2.5, 2.9, 3.2, 1.4, 1.6, 1.9, 2.2, 2.6, 3.0, 1.3]  # dips after VACUUM
index_bloat_pct =        [6,   7,   9,  12,  14,  15,  17,   8,   9,  10,  12,  14,  16,   7]   # dips after REINDEX

fig, ax1 = plt.subplots(figsize=(8, 4.5))
ax1.plot(days, dead_tuples_millions, color="#1f77b4", marker="o", label="Dead tuples (M)")
ax1.set_xlabel("Day")
ax1.set_ylabel("Dead tuples (millions)", color="#1f77b4")
ax1.tick_params(axis='y', labelcolor="#1f77b4")
ax1.grid(True, alpha=0.3)

ax2 = ax1.twinx()
ax2.plot(days, index_bloat_pct, color="#ff7f0e", marker="s", label="Index bloat (%)")
ax2.set_ylabel("Index bloat (%)", color="#ff7f0e")
ax2.tick_params(axis='y', labelcolor="#ff7f0e")

plt.title("Postgres: Bloat and Autovacuum Impact Over Time")
fig.tight_layout()
plt.savefig("blog_images/postgres-bloat-trend.png", dpi=160)
plt.close()

# 3) MongoDB execution stats (before vs after) - grouped bars
labels = ["docsExamined", "keysExamined", "p95 latency (ms)"]
before = [6200, 6500, 1200]
after  = [110,  120,  180]

x = np.arange(len(labels))
width = 0.35

plt.figure(figsize=(8, 4.5))
plt.bar(x - width/2, before, width, label="Before (skip/offset)")
plt.bar(x + width/2, after,  width, label="After (cursor + compound index)")
plt.xticks(x, labels)
plt.title("MongoDB: Execution Stats Before vs After")
plt.grid(axis="y", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("blog_images/mongo-execstats.png", dpi=160)
plt.close()

print("Saved images to ./blog_images:")
print("- sql-pagination-latency.png")
print("- postgres-bloat-trend.png")
print("- mongo-execstats.png")
