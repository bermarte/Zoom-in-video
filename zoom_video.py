"""Module providing Function to concatenate and zoom-in a sequence of images."""
import os
from moviepy.editor import sys, ImageClip, concatenate_videoclips


def create_zoom_video(images, output_file, zoom_factor=0.05, duration_per_image=1):
    '''It takes a list of input image files, zooms them in progressively to create a clip'''
    clips = []
    # Calculate the zoom values
    zoom_values = [1.0, zoom_factor]
    for _i, image in enumerate(images):
        # Load the image as a VideoClip
        clip = ImageClip(image)
        # Set the duration for the video clip
        clip = clip.set_duration(duration_per_image)
        # Apply the zoom-in effect using the 'resize' method
        clip = clip.resize(lambda t: zoom_values[0] + len(zoom_values) + t)
        clips.append(clip)

    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_file, fps=24, codec="libx264")


def main():
    '''The main function'''
    if len(sys.argv) < 2:
        print("Usage: python3 zoom_video.py output_video.mp4")
        sys.exit(1)

    output_video = sys.argv[-1]

    # Get all image files from the 'images' directory
    image_files = [filename for filename in os.listdir(
        'images') if filename.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        print("No image files found in the 'images' directory.")
        sys.exit(1)

    input_files = [os.path.join('images', filename)
                   for filename in image_files]

    create_zoom_video(input_files, output_video, duration_per_image=1)


if __name__ == "__main__":
    main()
