from src.utils import now_ist, yyyymmdd, iso_local
import pandas as pd

ts = now_ist()
print("✅ Python & packages are good.")
print("IST datetime:", ts)
print("IST ISO string:", iso_local(ts))
print("YYYYMMDD (for filenames):", yyyymmdd(ts))

# Quick pandas check
df = pd.DataFrame([{"ok": True, "time": iso_local(ts)}])
print("Pandas says rows:", len(df))
