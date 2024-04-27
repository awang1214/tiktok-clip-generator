import os
from moviepy.editor import *
from moviepy.video import *

input_folder = 'videos/'
output_folder = 'clips/'
os.makedirs(output_folder, exist_ok=True)

# Process each video file in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith('.mp4'):  # Adjust if videos have a different extension
        video_path = os.path.join(input_folder, file_name)
        
        # Load the input video
        clip = VideoFileClip(video_path)
        
        # Calculate the duration of the video in seconds
        video_duration = clip.duration
        
        # Define the duration for each segment (1 minute)
        segment_duration = 60  # 60 seconds = 1 minute
        
        # Calculate the number of segments
        num_segments = int(video_duration // segment_duration)
        
        # Process each segment of the video
        for i in range(num_segments):
            start_time = i * segment_duration
            end_time = min((i + 1) * segment_duration, video_duration)
            
            # Extract the segment
            segment = clip.subclip(start_time, end_time)
            txt = TextClip('Part' + str(i), fontsize=75, color='white').set_position(('bottom')).set_duration(segment.duration)
            
            # Composite the text clip with the final segment
            final_segment = CompositeVideoClip([segment, txt])
            
            # Output path for the processed segment
            output_path = os.path.join(output_folder, f'{os.path.splitext(file_name)[0]}_segment_{i + 1}_portrait_with_text.mp4')
            
            # Write the processed segment to the output folder
            segment.write_videofile(output_path, codec='libx264', fps=24)  # Adjust codec and fps as needed
