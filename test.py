from moviepy import VideoFileClip, CompositeVideoClip, ImageClip
from PIL import Image, ImageDraw, ImageFont

# Function to create an image with text for subtitles
from PIL import Image, ImageDraw, ImageFont

def create_text_image(text, font_path, font_size):
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    
    # Get font metrics
    ascent, descent = font.getmetrics()  # Ascender and descender of the font
    
    # Calculate text size using textbbox
    temp_image = Image.new('RGBA', (1, 1))
    draw = ImageDraw.Draw(temp_image)
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    
    # Adjust height to account for font metrics
    text_width = right - left
    text_height = bottom - top + descent  # Add descent for characters like 'g', 'y'
    
    # Create the final image with calculated dimensions
    image = Image.new('RGBA', (text_width, text_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw the text on the image
    draw.text((0, -top), text, font=font, fill=(255, 255, 255, 255))  # Offset by -top to ensure full text is visible
    return image


# Function to create an ImageClip for a subtitle
def create_subtitle_clip(text, start_time, end_time, video_width, video_height, font_path, font_size):
    # Create text image
    text_image = create_text_image(text, font_path, font_size)
    
    # Save the text image as a temporary file (optional)
    text_image_path = "temp_text_image.png"
    text_image.save(text_image_path)
    
    # Create an ImageClip from the text image
    text_clip = ImageClip(text_image_path).with_duration(end_time - start_time)
    
    # Position the text at the bottom center of the video
    text_clip = text_clip.with_position(("center", "center"))
    
    # Set the start and end time of the subtitle
    text_clip = text_clip.with_start(start_time).with_end(end_time)
    return text_clip

# Main function to add subtitles
def add_subtitles_to_video(video_path, output_path, subtitles, font_path, font_size=24):
    # Load the video
    video = VideoFileClip(video_path)
    
    # Generate subtitle clips
    subtitle_clips = [
        create_subtitle_clip(
            subtitle["text"], 
            subtitle["start"], 
            subtitle["end"], 
            video.w, 
            video.h, 
            font_path, 
            font_size
        )
        for subtitle in subtitles
    ]
    
    # Combine the video with subtitle clips
    final_video = CompositeVideoClip([video, *subtitle_clips])
    
    # Write the output video file
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

# Example usage
if __name__ == "__main__":
    video_path = "assets/video1.mp4"
    output_path = "output_with_subtitles.mp4"
    # font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Update with the path to your font file
    # font_path = "assets/fonts/Rain Night.ttf"
    # font_path = "assets/fonts/Grownup.ttf"
    # font_path = "assets/fonts/BeachyLagoon.ttf"
    # font_path = "assets/fonts/Blonden-ExtrudeRight.otf"
    font_path = "assets/fonts/Agiven-Drawn.otf"
    subtitles = [
        {"text": "Hello, welcome to the video!", "start": 0, "end": 5},
        {"text": "This is the second subtitle.", "start": 6, "end": 10},
        {"text": "Enjoy the video!", "start": 11, "end": 15},
    ]
    
    add_subtitles_to_video(video_path, output_path, subtitles, font_path, font_size=24)
