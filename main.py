import os

LINE = "I survived fourteen hours, three drops, and one swim in the toilet \u2014 and what finally kills me is a weather app checking whether it might rain."

out = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
