from moviepy.editor import CompositeVideoClip, ImageClip, VideoFileClip




def add_ratings(video_clip):
    # Load rating image
    rating = input("Which TV Rating would you like to add, TV-Y, TV-Y7, TV-G, TV-PG, TV-14, or TV-MA?")
    if rating == "TV-G":
        rating_image = ImageClip('TV-G.png')
    if rating == "TV-14":
        rating_image = ImageClip('TV-14.png') 
    if rating == "TV-MA":
        rating_image = ImageClip('TV-MA.png') 
    if rating == "TV-PG":
        rating_image = ImageClip('TV-PG.png') 
    if rating == "TV-Y":
        rating_image = ImageClip('TV-Y.png') 
    if rating == "TV-Y7":
        rating_image = ImageClip('TV-Y7.png') 

    closed_captions = input("Do you want to add a closed captions symbol? Answer 'Yes' or 'No'")
    if closed_captions == "Yes":
        cc_image = ImageClip('CC.png') 
    if closed_captions == "No":
        cc_image = None

    if cc_image is not None: 
        clips_to_composite = [video_clip, rating_image.set_start(0.5).set_duration(15).crossfadein(0.2).crossfadeout(0.2)]
    else:
        clips_to_composite = [video_clip, rating_image.set_start(0.5).set_duration(15)]
    
    

    if cc_image:
        clips_to_composite.append(cc_image.set_start(0.5).set_duration(5).crossfadein(0.2).crossfadeout(0.2))
    video_with_ratings = CompositeVideoClip(clips_to_composite)

    return video_with_ratings

def add_ratings_small(video_clip):
    # Load rating image
    rating = input("Which TV Rating would you like to add, TV-Y, TV-Y7, TV-G, TV-PG, TV-14, or TV-MA?")
    if rating == "TV-G":
        rating_image = ImageClip('TV-G SMALL.png')
    if rating == "TV-14":
        rating_image = ImageClip('TV-14 SMALL.png') 
    if rating == "TV-MA":
        rating_image = ImageClip('TV-MA SMALL.png') 
    if rating == "TV-PG":
        rating_image = ImageClip('TV-PG SMALL.png') 
    if rating == "TV-Y":
        rating_image = ImageClip('TV-Y SMALL.png') 
    if rating == "TV-Y7":
        rating_image = ImageClip('TV-Y7 SMALL.png') 



    # Composite the rating image over the video clip
    clips_to_composite = [video_clip, rating_image.set_start(0.5).set_duration(15)]

    video_with_ratings = CompositeVideoClip(clips_to_composite)

    return video_with_ratings

def optional_add_logo(video_clip):
  
    logo_image = ImageClip('logo.png')  

    clips_to_composite = [video_clip, logo_image.set_duration(video_clip.duration)]

    video_with_logo = CompositeVideoClip(clips_to_composite)

    return video_with_logo



def main():
    print("Welcome to the TV Rating Adder!")
    print("Inputs are case-sensitive.")
    print("Before using this tool, make sure your video is 1920x1080, titled 'video.mp4', and located in the same location as this script.")
    print("If you wish to add a custom logo as well, make sure the image is 1920x1080, titled 'logo.png', and located in the same location as this script.")
    video_path = 'video.mp4'
    video_clip = VideoFileClip(video_path)

    # Add ratings to the video
    rating_type_choice = input("Do you want to add a big size rating for the beginning of a show or a small one for returning from commericals? Answer 'Big' or 'Small'")
    if rating_type_choice == "Big":
        video_with_ratings = add_ratings(video_clip)
    if rating_type_choice == "Small":
       video_with_ratings = add_ratings_small(video_clip) 

    

    channel_logo_choice = input("Do you want to add a channel logo over the video? Answer 'Yes' or 'No'")
    if channel_logo_choice == "Yes":
        video_with_logo = optional_add_logo(video_with_ratings)
    else:
        video_with_logo = video_with_ratings


    # Export the final video
    video_with_logo.write_videofile('video_with_ratings.mp4', codec='libx264', fps=30)

if __name__ == "__main__":
    main()