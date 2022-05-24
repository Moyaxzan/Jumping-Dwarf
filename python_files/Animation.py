# Allows to animate every elements of the game that has animations.
class Animation:
    def __init__(self):
        self.frames = []
        self.actual_frame = 0
        self.frame = 0
        self.switch_time = 0
        self.count_thing = 0

    # Receives every frames of "gif_name" in a list for other functions to use them.
    def collect_frames(self, gif_name, gif_folder, frames_nb):
        self.frames = []
        for each_frame in range(frames_nb):
            with open(r"../assets/"+gif_folder+"/"+gif_name+str(each_frame+1)+".png") as pose:
                self.frames.append(pose.name)

    # Returns which frame is to display to the class that calls animation (Player or scenery).
    def next_frame(self,nb_frames, velocity):
        self.actual_frame += velocity
        self.frame = (int(self.actual_frame)) % nb_frames
        return self.frames[self.frame]

    # Coordinates every functions in order to optimize the process.
    def launch_gif(self, gif_name, gif_path, frames_nb, velocity):
        self.collect_frames(gif_name, gif_path, frames_nb)
        return self.next_frame(frames_nb, velocity)
