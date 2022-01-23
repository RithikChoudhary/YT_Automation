import moviepy.editor 
import grab_files  as gf

    

def make_compilation(videos):
    all_videos = []
    for i in videos:
        
        clip = moviepy.editor.VideoFileClip(i)
        all_videos.append(clip)
    
    Mearged_video=moviepy.editor.concatenate_videoclips(all_videos,method="compose")
    
    Mearged_video.write_videofile("Output.mp4",threads=8, remove_temp=True, codec="libx264", audio_codec="aac")
    
    print("Done")
    
make_compilation(gf.stack)
