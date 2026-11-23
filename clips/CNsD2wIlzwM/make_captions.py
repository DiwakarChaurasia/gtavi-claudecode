"""Build burn-in .ass (hook + captions, 1080x1920) and plain .srt files from clips.json."""
import json, sys
from pathlib import Path

here = Path(__file__).resolve().parent
clips = json.loads((here / "clips.json").read_text(encoding="utf-8"))
out = here / "captions"
out.mkdir(exist_ok=True)

def secs(ts):
    h, m, s = ts.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)

def ass_t(t):
    cs = round(t * 100)
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"

def srt_t(t):
    ms = round(t * 1000)
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"

HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Hook,DejaVu Sans,70,&H00FFFFFF,&H00FFFFFF,&H007F45E8,&H007F45E8,1,0,0,0,100,100,0,0,3,18,0,8,70,70,330,1
Style: Cap,DejaVu Sans,62,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,1,0,0,0,100,100,0,0,1,6,2,8,60,60,1310,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

for c in clips:
    t0, t1 = secs(c["start"]), secs(c["end"])
    dur = t1 - t0
    lines = [(secs(ts) - t0, txt) for ts, txt in c["lines"]]
    ass = [HEAD.rstrip("\n")]
    # Hook stays on screen for the first 3 seconds.
    ass.append(f"Dialogue: 1,{ass_t(0)},{ass_t(3)},Hook,,0,0,0,,{c['hook']}")
    srt = []
    for i, (s, txt) in enumerate(lines):
        nxt = lines[i + 1][0] if i + 1 < len(lines) else dur
        e = min(nxt, s + 4.5, dur)
        ass.append(f"Dialogue: 0,{ass_t(s)},{ass_t(e)},Cap,,0,0,0,,{txt}")
        srt.append(f"{i + 1}\n{srt_t(s)} --> {srt_t(e)}\n{txt}\n")
    (out / f"{c['id']}.ass").write_text("\n".join(ass) + "\n", encoding="utf-8")
    (out / f"{c['id']}.srt").write_text("\n".join(srt), encoding="utf-8")
    print(f"{c['id']}: {c['start']}-{c['end']} ({dur:.0f}s), {len(lines)} captions")
