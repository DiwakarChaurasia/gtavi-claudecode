#!/usr/bin/env bash
# Cut the 3 picked moments from the stream into 1080x1920 vertical clips with
# burned-in English captions and a hook title.
#
#   ./make_clips.sh                 # downloads only the 3 sections from YouTube (needs yt-dlp)
#   ./make_clips.sh /path/vod.mp4   # cuts from a VOD you already downloaded
#
# Needs: ffmpeg (with libass), python3; yt-dlp unless you pass a local file.
# Output: out/<clip>.mp4 (vertical, captions burned in) and out/<clip>_wide.mp4 (original framing, no captions).
set -euo pipefail
cd "$(dirname "$0")"

URL="https://www.youtube.com/watch?v=CNsD2wIlzwM"
LOCAL="${1:-}"
mkdir -p raw out
python3 make_captions.py

python3 - <<'PY' > /tmp/clips_list.$$
import json
for c in json.load(open("clips.json", encoding="utf-8")):
    print(c["id"], c["start"], c["end"])
PY

while read -r ID START END; do
  RAW="raw/$ID.mp4"
  if [[ ! -s "$RAW" ]]; then
    if [[ -n "$LOCAL" ]]; then
      ffmpeg -nostdin -hide_banner -loglevel error -y -ss "$START" -to "$END" -i "$LOCAL" \
        -c:v libx264 -preset veryfast -crf 18 -c:a aac -b:a 192k "$RAW"
    else
      yt-dlp -f "bv*[height<=1080]+ba/b[height<=1080]" --merge-output-format mp4 \
        --download-sections "*$START-$END" --force-keyframes-at-cuts -o "$RAW" "$URL" < /dev/null
    fi
  fi
  cp "$RAW" "out/${ID}_wide.mp4"

  # Vertical: full 16:9 frame centred over a blurred, zoomed copy of itself,
  # hook box on top, captions under the video. Audio normalised to -14 LUFS.
  ffmpeg -nostdin -hide_banner -loglevel error -y -i "$RAW" -filter_complex \
    "[0:v]split=2[bg][fg];\
     [bg]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=30,eq=brightness=-0.12[bgb];\
     [fg]scale=1080:-2[fgs];\
     [bgb][fgs]overlay=(W-w)/2:(H-h)/2,ass=captions/$ID.ass,format=yuv420p[v];\
     [0:a]loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
    -map "[v]" -map "[a]" -c:v libx264 -preset medium -crf 20 -r 30 \
    -c:a aac -b:a 160k -movflags +faststart "out/$ID.mp4"
  echo "done: out/$ID.mp4"
done < /tmp/clips_list.$$
rm -f /tmp/clips_list.$$
