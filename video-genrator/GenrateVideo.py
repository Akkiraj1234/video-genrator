from moviepy import (
    VideoFileClip,
    CompositeVideoClip,
    ImageClip,
    AudioFileClip,
    CompositeAudioClip
)

from PIL import Image, ImageDraw, ImageFont
from .assets import font_byname, Temporary_File_Path, os


def get_text_size(text: str, font: ImageFont) -> tuple[int, int]:
    """
    Calculates the dimensions of the text using the provided font.
    """
    ascent, descent = font.getmetrics()

    with Image.new("RGBA", (1, 1)) as temp_image:
        draw = ImageDraw.Draw(temp_image)
        bbox = draw.textbbox((0, 0), text, font=font)
        return (bbox[2] - bbox[0], bbox[3] - bbox[1] + descent + ascent)


def create_text_image(text: str, font: ImageFont, fill=(255, 255, 255, 255)) -> Image:
    """
    Creates an image containing the given text.

    Args:
        text (str): The text to render.
        font (ImageFont): The font to use for rendering.
        fill (tuple): The RGBA color to use for the text. Default is white.

    Returns:
        Image: An image object with the rendered text.
    """
    text_width, text_height = get_text_size(text, font)

    image = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))
    ImageDraw.Draw(image).text((0, 0), text, font=font, fill=fill)
    return image


def create_subtitle_clip(text_image: Image, s_time: float, e_time: float):
    """
    Creates a subtitle clip from the given text image and time range.

    Args:
        text_image (Image): The image containing the subtitle text.
        s_time (float): Start time of the subtitle.
        e_time (float): End time of the subtitle.

    Returns:
        ImageClip: The subtitle clip.
    """
    temp_path = os.path.join(Temporary_File_Path, "image.png")
    text_image.save(temp_path)
    text_clip = ImageClip(temp_path).with_duration(e_time - s_time)
    text_clip = text_clip.with_position(("center", "center"))
    text_clip = text_clip.with_start(s_time).with_end(e_time)
    return text_clip


class GenerateVideo:
    def __init__(self, FONTS_INFO: dict):
        self.fonts_info = FONTS_INFO
        self.font_path = FONTS_INFO["default"]
        self.font_size = FONTS_INFO["size"]
        self.font = ImageFont.truetype(
            font=self.font_path,
            size=self.font_size
        )

    def create_final_video(
        self,
        video_path: str,
        subtitles: list[tuple[str, float, float]],
        audio_path: str,
        background_audio_path: str,
        output_path: str
    ) -> None:
        """
        Combines video, subtitles, and audio into the final video.

        Args:
            video_path (str): Path to the video file.
            subtitles (list): List of subtitle data (text, start time, end time).
            audio_path (str): Path to the main audio file.
            background_audio_path (str): Path to the background audio file.
            output_path (str): Path to save the output video.
        """
        # loading the assets
        video = VideoFileClip(video_path)
        main_audio = AudioFileClip(audio_path)
        background_audio = AudioFileClip(background_audio_path).set_duration(video.duration)
        
        subtitle_clips = [
            create_subtitle_clip(
                create_text_image(subtitle[0], self.font),
                subtitle[1],
                subtitle[2]
            )
            for subtitle in subtitles
        ]
        
        final_video = CompositeVideoClip([video, *subtitle_clips])
        mixed_audio = CompositeAudioClip([main_audio.volumex(0.7), background_audio.volumex(0.3)])
        final_video = final_video.set_audio(mixed_audio)
        final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

