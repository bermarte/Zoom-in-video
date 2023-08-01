from moviepy.editor import *

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
    if len(sys.argv) < 3:
        print("Usage: python image_zoom.py input_file1 [input_file2 ...] output_video.mp4")
        sys.exit(1)

    input_files = sys.argv[1:-1]
    output_video = sys.argv[-1]

    create_zoom_video(input_files, output_video, duration_per_image=1)

if __name__ == "__main__":
    main()
