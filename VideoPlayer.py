import tkinter as tk
#import threading
#import imageio
#from PIL import Image, ImageTk
import pygame

FPS = 60

pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie('video/sample.mp4')
screen = pygame.display.set_mode(movie.get_size())
movie_screen = pygame.Surface(movie.get_size()).convert()

movie.set_display(movie_screen)
movie.play()


playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False

    screen.blit(movie_screen,(0,0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

'''
video_name = "video/sample.mp4" #This is your video file path
video = imageio.get_reader(video_name)

def stream(label):
    frame = 0
    #for i, im in enumerate(vid):
    #print('Mean of frame %i is %1.1f' % (i, im.mean()))
    for image in video.iter_data():
        frame += 1                                    #counter to save new frame number
        image_frame = Image.fromarray(image)          
        #image_frame.save('FRAMES/frame_%d.png' % frame)      #if you need the frame you can save each frame to hd
        frame_image = ImageTk.PhotoImage(image_frame)
        label.config(image=frame_image)
        label.image = frame_image
        #if frame == 40: break                         #after 40 frames stop, or remove this line for the entire video

if __name__ == "__main__":

    root = tk.Tk()
    my_label = tk.Label(root)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()
    root.mainloop()

from skvideo.io import VideoCapture

cap = VideoCapture(filename)
cap.open()

while True:
    retval, image = cap.read()
    # image is a numpy array containing the next frame
    # do something with image here
    if not retval:
        break
'''
