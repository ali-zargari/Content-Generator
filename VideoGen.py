from moviepy.editor import ImageClip, TextClip, CompositeVideoClip, concatenate_videoclips

# List of images and corresponding subtitles
images = ["1.jpg", "2.jpg", "3.jpg"]
subtitles = ["Subtitle 1", "Subtitle 2", "Subtitle 3"]

# Duration of each image in the video
image_duration = 2  # seconds

clips = []
for img, subtitle in zip(images, subtitles):
    # Create an image clip
    image_clip = ImageClip(img).set_duration(image_duration)

    # Create a text clip for the subtitle
    text_clip = TextClip(subtitle, fontsize=24, color='white', bg_color='black').set_duration(image_duration)

    # Position the text clip at the bottom of the image
    text_clip = text_clip.set_position(('center', 'bottom'))

    # Composite the image and text clips
    composite_clip = CompositeVideoClip([image_clip, text_clip])

    clips.append(composite_clip)

# Concatenate all the clips into a final video
final_video = concatenate_videoclips(clips, method="compose")

# Write the result to a file
final_video.write_videofile("output_video.mp4", fps=24)

print("Video generation complete.")
