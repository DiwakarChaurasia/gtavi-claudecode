# Top 3 clips: "ITS GANG WARS TIME | NO PROMOTIONS"

Source: https://www.youtube.com/live/CNsD2wIlzwM (CarryMinati, GTA 6 story stream in Hindi, about 4 h 07 min)
Full English translation: [transcript_en.md](transcript_en.md)

Picked from the whole transcript for a clear setup and payoff, the streamer's personality, and an English hook that works without knowing Hindi. Dark or offensive stretches were skipped (for example the airport/terrorism bit at 1:33–1:35 and the "slapped mom" rant at 3:03). Timestamps come from the auto-captions, so they can be 1–2 s off. Adjust `start`/`end` in `clips.json` after a first watch if needed.

| # | Clip | Source time | Length | Watch |
|---|------|-------------|--------|-------|
| 1 | "I'm a DROPOUT, not 12th-fail" | 3:09:22 – 3:10:20 | 58 s | [open](https://www.youtube.com/watch?v=CNsD2wIlzwM&t=11362s) |
| 2 | Mansion heist goes wrong → Ruby Lambo escape | 0:57:58 – 0:58:57 | 59 s | [open](https://www.youtube.com/watch?v=CNsD2wIlzwM&t=3478s) |
| 3 | Chat votes SELL, then regrets it: "this is literally politics" | 1:20:19 – 1:21:17 | 58 s | [open](https://www.youtube.com/watch?v=CNsD2wIlzwM&t=4819s) |

---

## 1. "I'm a DROPOUT, not 12th-fail" (3:09:22 – 3:10:20)

**Why it's #1:** this is the best personality moment of the stream. Chat trolls him with "12th fail", he gets genuinely triggered and argues the point, and he quotes the "emotional" fan video about himself. It has a clear setup and payoff, it's quotable, and his fans will recognise it straight away. Chat kept the joke going for the next 10 minutes ("PhD holder", "principal's son"), which shows it landed.

**Hook (on screen for 0–3 s):** `Chat called him "12th FAIL"…`
**Alt hooks:** `He is NOT 12th fail. Here's why 😤` · `Never call him 12th fail`

**English captions (burned in):**
> Chat: "Does your girlfriend know you're 12th-fail?"
> First of all — I am NOT 12th-fail. OK? There's a difference.
> I left 12th myself. By my own choice. That's called a DROPOUT — not "fail"!
> Second thing — do you even know? She knows, bro.
> I saw some emotional video someone made about me: "Carry Minati — you must have heard the name… famous across the country and the world… found success early — despite being 12th-fail."
> I got SO angry. I said I'll smack you — wind up and SMACK you. "12th fail."
> Bro, dropout and fail are VERY different.

**Post caption:** `Dropout ≠ fail 😤 (via CarryMinati's GTA 6 stream) #GTA6 #CarryMinati #GTAVI #gaming`

## 2. Mansion heist goes wrong → Ruby Lambo escape (0:57:58 – 0:58:57)

**Why:** the best pure-gameplay moment. He's looting a Vice City mansion for the Ruby Lamborghini, alarms go off ("we're SCREWED, get out!"), and he floors it, stunned at how fast the car is. It works muted (the action carries it) and it shows GTA 6 heist and supercar content, which is trending.

**Hook:** `Stealing a Lambo from a mansion in GTA 6…`
**Alt hooks:** `This GTA 6 car is TOO fast` · `GTA 6 heist went wrong 💀`

**English captions:**
> Wait. I don't want to leave ANYTHING behind here.
> Oh (bleep), bro — now we have to RUN! If I don't run now, I lose it all!
> We're SCREWED! We're screwed — GET OUT, get out, get out! Get out of here!
> Oh bro — this car is FAST! This car is really fast — move, move, MOVE!
> WOW. This car is SO fast, bro! Bro, DRIVE!
> Are you kidding me?! Way TOO fast! I don't even know how it's driving.

**Post caption:** `Stole a Lambo from a Vice City mansion and it's WAY too fast 🏎️ (via CarryMinati) #GTA6 #ViceCity #GTAVI`

## 3. Chat votes SELL, then regrets it (1:20:19 – 1:21:17)

**Why:** a relatable streamer-vs-chat moment with a funny real-world comparison. He ran a YouTube poll on selling the Lambo, chat voted SELL, then flooded in with "don't sell!", and he compares it to voters who regret their own vote: "Were you sitting at home?!" (At 1:20:36 an NPC also starts a fight with him, which adds to the chaos.)

**Hook:** `Chat voted to SELL his Lambo… then changed its mind`
**Alt hooks:** `GTA 6 chat = Indian politics 😭` · `Why did you VOTE then?!`

**English captions:**
> "Don't sell it"? Then why'd you say SELL before?! Why'd you say it before?!
> Why are you being such clowns, bro?
> What? This guy came to fight me, bro — I didn't even say anything to him!
> Bro, it's LITERALLY become politics. Just like in politics — you vote for one guy, then "we never wanted him! Shouldn't have voted for him — why did he win?"
> That's literally what you guys are doing.
> Then why did you VOTE? Weren't you at the polling booth? Were you sitting at home?!

**Post caption:** `Chat voted, then regretted it 😭 "Were you sitting at home?!" (via CarryMinati) #GTA6 #CarryMinati`

---

## Runners-up

| Time | Moment |
|------|--------|
| 2:16:44 – 2:17:20 | Chat: "Paytm me ₹500 for a party." He asks what liquor ₹500 even buys, then answers "how did you get taller?" with "people look up to you." A short roast. |
| 2:44:09 – 2:45:45 | NPCs steal his car mid-mission: "They took our car!", then a chase. |
| 3:14:15 – 3:14:50 | Chat roast: "I'm the son of the principal who expelled you" (follows on from clip 1). |
| 2:24:47 – 2:25:08 | First time on nitro: a long string of screamed swears. |
| 0:22:17 – 0:22:40 | Finally reaching the King of Hearts club after trying since the first stream. |

## Make the clips

YouTube can't be reached from the cloud session that prepared this, so run this on your own machine (needs `ffmpeg` with libass, `python3`, `yt-dlp`):

```bash
cd clips/CNsD2wIlzwM
./make_clips.sh                  # downloads only the 3 sections, ~1 min each
# or, if you already have the full VOD:
./make_clips.sh ~/Downloads/CNsD2wIlzwM.mp4
```

Output goes in `out/`:
- `<clip>.mp4`: 1080×1920 vertical. The full frame is centred over a blurred fill, with the hook box at the top, English captions under the video and audio at −14 LUFS.
- `<clip>_wide.mp4`: the original 16:9 cut with no captions. Upload it with `captions/<clip>.srt` if you'd rather have selectable subtitles.

To change timing or wording, edit `clips.json` and run `python3 make_captions.py` (`make_clips.sh` does this for you).

Credit the creator in every post caption.
