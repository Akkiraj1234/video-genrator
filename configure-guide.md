# Video Configuration Guide

## [assets]
Defines paths for assets like videos and images. 

### Syntax:
```ini
[assets]
asset_name = "path/to/asset"
```
## [video-settings]

Controls individual clip settings.
### Options:

- `clipX.video`: Asset name (e.g., video1).
- `clipX.effects-begin` / `clipX.effects-end`: Effects at the start/end (fadeup, fadeout).
- `clipX.effects`: Persistent effects (snowfall, black and white).
- `clipX.duration`: Duration in seconds or trim range (e.g., 5 or 5:10).
- `clipX.speed`: Playback speed (e.g., 1.5).
- `clipX.transition`: Transition type (wipe, fade).
- `clipX.script`: Text displayed or spoken in the clip.
- `transition` = global transition to use
- `duration` = global duration

### Syntax:

```ini
[video-settings]
clip1.video = "video1"
clip1.effects-begin = "fadeup"
clip1.duration = 5
clip1.script = "Welcome!"
```

## [script-settings]

Configures how scripts are displayed.
### Options:

- `script-time-exceed-video-increase`: Auto-adjust video duration if the script exceeds time (True/False).
- `script-printing-style`: Style of script display (fading, typing).
- `clipX.subtitles.font-size`: Font size of subtitles.
- `clipX.subtitles.color`: Subtitle color.
- `subtitles.font-size` : universal size for all subtitles
- `subtitles.color` : universal color for all color.
### Syntax:

```ini
[script-settings]
script-time-exceed-video-increase = True
script-printing-style = "typing"
clip1.subtitles.font-size = 16
clip1.subtitles.color = "white"
```

## [video-creation]

Defines global settings and video sequence.
Options:

- `video-size-aspect-ratio`: Aspect ratio (16:9, 9:16).
- `sequence`: Order of clips, transitions, or countdowns (e.g., **[clip1, countdown.3, clip2]**).
- background_audio = *audio
### Syntax:

```ini
[video-creation]
video-size-aspect-ratio = "16:9"
sequence = [clip1, countdown.3, clip2]
```

### [output-settings] (Optional)

Specifies the output format and location.
Options:

- `format`: File format (mp4, avi).
- `output-path`: Path to save the video. if not given use default
- `name` : name of file

### Syntax:

```ini
[output-settings]
format = "mp4"
output-path = "output/videos"
name = "output"
```

# Detailed Configuration Options with Examples

### script-printing-style
Defines how the text appears on the screen during playback.
#### Options:
- `typing`: The text appears letter by letter, mimicking typing. Great for dramatic or conversational effects.
- `normal`: Displays the entire text instantly without animation. Ideal for static displays like titles or simple subtitles.
- `flow`: The text fades in word by word, giving a smooth reading experience. Useful for longer text or narratives.
- `fade`: The text gradually fades in and out.
- `wave`: The text appears in a wavy motion, creating a dynamic and playful effect.
- `sentence` : print in sentence

### clipX.effects-begin and clipX.effects-end
Adds visual effects at the start or end of a clip.
#### Options:
- `fadeup`: Gradual fade-in effect.
- `fadeout`: Gradual fade-out effect.
- `zoom-in`: The video zooms in from a smaller scale.
- `zoom-out`: The video zooms out to disappear.
- `spin`: The video spins into or out of the frame.

### clipX.effects
Applies persistent effects throughout the video.
#### Options:
- `black-and-white`: Converts the video to grayscale.
- `vignette`: Adds a dark border around the video edges for a classic look.
- `snowfall`: Creates a falling snow animation over the video.
- `blur`: Blurs the video slightly for a soft, dreamlike effect.
- `sepia`: Adds a warm, vintage tone to the video.

### clipX.transition
Defines the transition effect used between clips.
#### Options:
- `wipe`: The next clip slides in, replacing the current one.
- `fade`: The current clip fades out, and the next fades in.
- `zoom`: The next clip zooms into view.
- `slide`: The next clip slides in from a specific direction (left, right, top, bottom).
- `cut`: A simple, instant switch to the next clip.

### subtitles.font-size and subtitles.color
Controls the size and color of subtitles.
- Options for subtitles.color:
    - **Standard colors** like white, yellow, red, blue, green, etc.
    - **Hex** codes for custom colors (e.g., #FF5733 for orange).
- Options for subtitles.font-size:
    - Any numeric value, typically between 12 (small) and 32 (large).

### video-size-aspect-ratio
Defines the overall aspect ratio of the video.
#### Options:
- `16:9`: Standard widescreen (e.g., YouTube).
- `9:16`: Portrait format (e.g., Instagram Reels, TikTok).
- `4:3`: Traditional TV format.
- `1:1`: Square format (e.g., Instagram posts).

### clipX.speed
Controls the playback speed of the video.
#### Options:
- 1: Normal speed.
- 0.5: Half speed (slow-motion).
- 2: Double speed (fast-forward).