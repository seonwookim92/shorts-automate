from navertts import NaverTTS



text = "복치는 보기엔 귀엽지만 사실 난폭해요. 건드리면 물기도 하거든요."

tts = NaverTTS(text)
tts.save("scarybokchee.mp3")