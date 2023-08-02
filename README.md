# Zoom-in-video

A script to make a quick video using a sequence of images. It takes a list of input image files, zooms them in progressively, and combines them to create a zoom-in animation. The resulting animation is saved as a video file specified by the **output_file** parameter.
I have used this script to make [this clip](https://www.youtube.com/watch?v=q6yLdfUr8As) 


https://github.com/bermarte/Zoom-in-video/assets/979362/d2a39442-fd79-4462-a0cc-4a118aff0c09


## in detail

- Import necessary modules:

```Python
from moviepy.editor import *
```

This line imports the required functions and classes from the MoviePy library, which is a Python module for video editing and manipulation.

---

- Define the **create_zoom_video** function:

```Python
def create_zoom_video(images, output_file, zoom_factor=0.05, duration_per_image=1):
```

This function takes four parameters:

- **images**: A list of input image file paths.
- **output_file**: The path where the output video file will be saved.
- z**oom_factor**: The factor by which the images will be zoomed in each frame.
- **duration_per_image**: The duration (in seconds) for which each image will be displayed in the final video.

---

- Create an empty list to store video clips:

```Python
clips = []
```

---

- Iterate over the input images and create video clips for each image:

```Python
for i, image in enumerate(images):
```

The **enumerate** function is used here to loop through the list of input images while also keeping track of the index.

---

- Load the image as a VideoClip:

```Python
clip = ImageClip(image)
```

This line loads each image file as a VideoClip object. A VideoClip is a representation of a video file, and in this case, each image is treated as a single-frame video.

---

- Set the duration for the video clip:

```Python
clip = clip.set_duration(duration_per_image)
```

The **set_duration** method is used to set the duration of the video clip. Each image will be displayed for the specified **duration_per_image** seconds.

---

- Calculate the zoom values:

```Python
zoom_values = [1.0, zoom_factor]
```

The **zoom_values** list contains two values: 1.0 (no zoom) and **zoom_factor** (the factor by which the image will be zoomed in).

---

- Apply the zoom-in effect using the 'resize' method:

```Python
clip = clip.resize(lambda t: zoom_values[0] + len(zoom_values) + t)
```

In this line, the resize method is used to apply the zoom effect to the video clip. The lambda function takes a time value t and calculates the zoom value based on the current time. The **zoom_values[0]** represents the initial zoom value (1.0), and **zoom_values[1]** represents the final zoom value (**zoom_factor**). The **len(zoom_values)** is used to determine the number of frames for the zoom animation, and t is used to progress through these frames.

---

- Append the clip to the list of clips:

```Python
clips.append(clip)
```

The zoomed-in video clip is added to the **clips** list.

---

- Concatenate the video clips to create the final animation:

```Python
final_clip = concatenate_videoclips(clips, method="compose")
```

The concatenate_videoclips function is used to concatenate the video clips in the **clips** list. The **method="compose"** argument means that the clips will be overlaid on top of each other.

---

- Write the final animation to a video file:

```Python
final_clip.write_videofile(output_file, fps=24, codec="libx264")
```

Finally, the **final_clip** is written to a video file with the specified output file path, frame rate (**fps**), and video codec (**codec**).

---

- Define the main function and execute the script if run as the main program:

```Python
def main():
    # ...

if __name__ == "__main__":
    main()

```

This is a common Python pattern where the main function is defined to handle command-line arguments and then executed when the script is run as the main program.

---

Source: [link](https://github.com/Zulko/moviepy/issues/1402)
