# Video Creation & Enhancement App

## Overview

This app enables users to create professional-grade videos by adding text-to-speech, subtitles, background music, and visual effects to a base video. Simply upload a video, provide your text, and optionally add background music to produce a polished final video with synchronized audio, subtitles, and effects.

## Features

- **Text-to-Speech (TTS):** Convert text into speech and sync it with the video.
- **Subtitles:** Automatically generate and synchronize subtitles from the provided text.
- **Visual Effects:** Add enhancements like fade-in, snowfall, and zoom effects.
- **Background Music:** Integrate optional background audio seamlessly.
- **Multi-format Support:** Supports popular video formats like `.mp4`.

## Requirements

To run the app, you’ll need the following dependencies:

- **Python 3.x**
- **FFmpeg** (for video processing)
- **Google Text-to-Speech (gTTS)** or any other TTS service
- Required Python libraries:
  - `moviepy`
  - `gTTS`
  - `pydub`
  - `numpy`

## Input

The app requires the following input from the user:

1. **Video File:** Base video (e.g., `video.mp4`) for enhancement.
2. **Text:** Content to convert into speech and use as subtitles.
3. **Background Music (Optional):** An audio file (e.g., `audio.mp3`) for background.
4. **Customization Options (Optional):** 
   - Subtitle font size and color
   - Visual effects (e.g., fade-in, snowfall, zoom-in)

## Example Configuration
```ini
[assets]
video1 = "assets/video1.mp4"
audio1 = "assets/music.mp3"

[video-settings]
clip1.video = "video1"
clip1.effects = "snowfall"
clip1.duration = 5
clip1.script = "Welcome to the world of anime!"

[script-settings]
script-time-exceed-video-increase = True
script-printing-style = "typing"
clip1.subtitles.font-size = 30
clip1.subtitles.color = "white"

[video-creation]
video-size-aspect-ratio = "16:9"
background_audio = [audio1]
sequence = [clip1]

[output-settings]
format = "mp4"
name = "demo_video"
```

## Usage
### Prepare Inputs:
- Upload a base video file.
- Provide the text for text-to-speech and subtitles.
- Optionally, include background music and select visual effects.

### Run the App:
- Use the main function to generate the video based on your configuration.
- The app processes inputs, applies effects, creates speech, and syncs subtitles.

### Download Output:
- The final video will be available in the specified format (e.g., .mp4).

## Future Enhancements
- **User Interface**: Add a GUI for easier input and effect selection.
- **Language Support**: Support multiple languages for text-to-speech.
- **Advanced Effects**: Introduce animations, transitions, and more.