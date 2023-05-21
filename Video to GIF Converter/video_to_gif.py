from moviepy.editor import *

video = VideoFileClip("Enter the path of your video").subclip(00, 5) 
#(00, 5) implies starting 5 seconds. 
#if you want any other part just change the timming accordingly 
#in the bracket specified above
video.write_gif("test.gif")

#if you want to rotate your gif 
video = VideoFileClip("Enter the path of your video").subclip(00, 5).rotate(180) 
video.write_gif("test_one.gif")











