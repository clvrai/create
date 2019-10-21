# Register all the tasks


from .levels.lvl_config import setup_json_lvls, setup_class_lvls
import create_game.defs
from .settings import CreateGameSettings

#def save_mp4(frames, vid_dir, name, fps=60.0, no_frame_drop=False):
#    frames = np.array(frames)
#    if len(frames[0].shape) == 4:
#        new_frames = frames[0]
#        for i in range(len(frames) - 1):
#            new_frames = np.concatenate([new_frames, frames[i + 1]])
#        frames = new_frames
#
#    if no_frame_drop:
#        def f(t):
#            idx = min(int(t * fps), len(frames)-1)
#            return frames[idx]
#
#        if not osp.exists(vid_dir):
#            os.makedirs(vid_dir)
#
#
#        vid_file = osp.join(vid_dir, name + '.mp4')
#        if osp.exists(vid_file):
#            os.remove(vid_file)
#
#        video = mpy.VideoClip(f, duration=len(frames)/fps)
#        video.write_videofile(vid_file, fps, verbose=False,
#                progress_bar=False)
#
#    else:
#        drop_frame = 1.5
#        def f(t):
#            frame_length = len(frames)
#            new_fps = 1./(1./fps + 1./frame_length)
#            idx = min(int(t*new_fps), frame_length-1)
#            return frames[int(drop_frame*idx)]
#
#        if not osp.exists(vid_dir):
#            os.makedirs(vid_dir)
#
#
#        vid_file = osp.join(vid_dir, name + '.mp4')
#        if osp.exists(vid_file):
#            os.remove(vid_file)
#
#        video = mpy.VideoClip(f, duration=len(frames)/fps/drop_frame)
#        video.write_videofile(vid_file, fps, verbose=False)
