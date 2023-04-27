import os
import moviepy.editor as mpy
from navertts import NaverTTS
from gtts import gTTS

class ShortsGen:
    def __init__(self):

        self.background_path = f"assets/img/background.png"
        self.title_path = f"assets/img/title.png"
        self.outro_path = f"assets/img/outro.png"

        self.font = 'BM-Jua'

        self.acc_time = 0

    def make_title_clip(self, day):
        title = mpy.ImageClip(self.title_path).set_duration(1.5)
        w, h = title.size
        
        # Auduo when it starts
        audio = mpy.AudioFileClip("assets/sound/치링.wav").set_duration(1.3)

        # Day text
        day = mpy.TextClip(str(day), fontsize=180, color='black', font=self.font).set_duration(1.5)
        day = day.set_position((w/2 * 1.4, h * 0.63))

        clip = mpy.CompositeVideoClip([title, day])
        clip.audio = mpy.CompositeAudioClip([audio])


        return clip

    def parse_string(self, sentence, thres):
        count = 0
        idx = 0
        d_ko = ""
        while idx != len(sentence):
            if count < thres and sentence[idx] != ' ':
                d_ko += sentence[idx]
                count += 1
            elif count > thres and sentence[idx] == ' ':
                d_ko += '\n'
                d_ko += sentence[idx]
                count = 0
            else:
                d_ko += sentence[idx]
                count += 1
            idx += 1

        n_newline = d_ko.count('\n')
        return d_ko, n_newline

    def make_word_clip(self, d):

        tts = NaverTTS(d['ko'])
        tts.save("tmp/tts_ko.mp3")
        tts = gTTS(d['en'], lang='en')
        tts.save("tmp/tts_en.mp3")

        # Get the length of the mp3 file
        tts_ko = mpy.AudioFileClip("tmp/tts_ko.mp3")
        tts_ko_dur = tts_ko.duration
        tts_en = mpy.AudioFileClip("tmp/tts_en.mp3")
        tts_en_dur = tts_en.duration

        # Audio when page changes
        aef_tr = mpy.AudioFileClip("assets/sound/훅.mp3")

        # Decrease the volume
        aef_tr = aef_tr.volumex(0.5)

        a_tts_ko = mpy.AudioFileClip("tmp/tts_ko.mp3").fx(mpy.vfx.speedx, 1.2)
        a_tts_ko2 = mpy.AudioFileClip("tmp/tts_ko.mp3").fx(mpy.vfx.speedx, 1)
        a_tts_en = mpy.AudioFileClip("tmp/tts_en.mp3").fx(mpy.vfx.speedx, 1.3)

        a_silence = mpy.AudioFileClip("assets/sound/silence.mp3").set_duration(1)

        audio = mpy.concatenate_audioclips([aef_tr, a_tts_ko, a_silence, a_tts_ko2, a_silence, a_tts_en, a_silence])
        # Get the audio's duration
        duration = audio.duration

        fontsize1 = 140
        fontsize2 = 100
        background = mpy.ImageClip(self.background_path).set_duration(duration)


        d_ko, ko_nl = self.parse_string(d['ko'], 12)

        d_pr, pr_nl = self.parse_string(d['pr'], 15)

        d_en, en_nl = self.parse_string(d['en'], 20)

        w, h = background.size
        ko = mpy.TextClip(d_ko, fontsize=fontsize1, color='black', font=self.font).set_duration(duration)
        ko = ko.set_position(('center', h * 0.25 - ko_nl * 30))

        if fontsize2 != 0:
            pr = mpy.TextClip(d_pr, fontsize=fontsize2, color='black', font=self.font).set_duration(duration)
            pr = pr.set_position(('center', h * 0.3))

        en = mpy.TextClip(d_en, fontsize=fontsize1, color='black', font=self.font).set_duration(a_tts_en.duration+1)
        en = en.set_start(duration - a_tts_en.duration - 2)
        en = en.set_position(('center', h * 0.55 - en_nl * 10))

        if fontsize2 != 0:
            clip = mpy.CompositeVideoClip([background, ko, pr, en])
        else:
            clip = mpy.CompositeVideoClip([background, ko, en])

        clip = clip.set_audio(audio)

        # Delete mp3 files
        os.remove("tmp/tts_ko.mp3")
        os.remove("tmp/tts_en.mp3")

        return clip
    
    def make_phrase_clip(self, d):

        tts = NaverTTS(d['ko'])
        tts.save("tmp/tts_ko.mp3")
        tts = gTTS(d['en'], lang='en')
        tts.save("tmp/tts_en.mp3")

        # Get the length of the mp3 file
        tts_ko = mpy.AudioFileClip("tmp/tts_ko.mp3")
        tts_ko_dur = tts_ko.duration
        tts_en = mpy.AudioFileClip("tmp/tts_en.mp3")
        tts_en_dur = tts_en.duration

        # Audio when page changes
        aef_tr = mpy.AudioFileClip("assets/sound/훅.mp3")

        # Decrease the volume
        aef_tr = aef_tr.volumex(0.5)

        a_tts_ko = mpy.AudioFileClip("tmp/tts_ko.mp3").fx(mpy.vfx.speedx, 1.3)
        a_tts_ko2 = mpy.AudioFileClip("tmp/tts_ko.mp3").fx(mpy.vfx.speedx, 1)

        a_silence = mpy.AudioFileClip("assets/sound/silence.mp3").set_duration(1)

        audio = mpy.concatenate_audioclips([aef_tr, a_tts_ko, a_silence, a_tts_ko2, a_silence])
        # Get the audio's duration
        duration = audio.duration

        fontsize1 = 90
        fontsize2 = 0
        background = mpy.ImageClip(self.background_path).set_duration(duration)


        d_ko, ko_nl = self.parse_string(d['ko'], 12)

        d_pr, pr_nl = self.parse_string(d['pr'], 15)

        d_en, en_nl = self.parse_string(d['en'], 20)

        w, h = background.size
        ko = mpy.TextClip(d_ko, fontsize=fontsize1, color='black', font=self.font).set_duration(duration)
        ko = ko.set_position(('center', h * 0.25 - ko_nl * 30))

        if fontsize2 != 0:
            pr = mpy.TextClip(d_pr, fontsize=fontsize2, color='black', font=self.font).set_duration(duration)
            pr = pr.set_position(('center', h * 0.3))

        en = mpy.TextClip(d_en, fontsize=fontsize1, color='black', font=self.font).set_duration(duration)
        en = en.set_position(('center', h * 0.55 - en_nl * 10))

        if fontsize2 != 0:
            clip = mpy.CompositeVideoClip([background, ko, pr, en])
        else:
            clip = mpy.CompositeVideoClip([background, ko, en])

        clip = clip.set_audio(audio)

        # Delete mp3 files
        os.remove("tmp/tts_ko.mp3")
        os.remove("tmp/tts_en.mp3")

        return clip

    def make_outro(self):
        outro_music_start = 1
        outro_music_end = 7
        outro_music = mpy.AudioFileClip('assets/sound/outro.mp3').subclip(outro_music_start, outro_music_end)
        outro_music = outro_music.volumex(0.5)
        # Fade out
        outro_music = outro_music.audio_fadeout(1)

        outro_background = mpy.ImageClip(self.outro_path).set_duration(outro_music_end - outro_music_start)
        outro_background = outro_background.set_audio(outro_music)

        return outro_background

    def make_video(self, day, data):
        clips = []

        intro = self.make_title_clip(int(day))
        outro = self.make_outro()

        clips.append(intro)
        self.acc_time += intro.duration

        n_phrase = len(data) - 1

        clip_word = self.make_word_clip(data['0'])
        clips.append(clip_word)
        self.acc_time += clip_word.duration

        for i in range(n_phrase):
            print(f"Making phrase {i+1}/{n_phrase}")
            clip = self.make_phrase_clip(data[str(i+1)])
            # clip.write_videofile(f"output/day{day}_{i+1}.mp4", fps=24, codec='libx264')
            print(f"{self.acc_time} + {clip.duration} = {self.acc_time + clip.duration}")
            if self.acc_time + clip.duration > 58 - outro.duration:
                print("Too long, the rest are ignored")
                break

            clips.append(clip)
            self.acc_time += clip.duration

        clips.append(outro)

        final_clip = mpy.concatenate_videoclips(clips)

        final_clip.write_videofile(f"output/day{day}.mp4", fps=24, codec='libx264')