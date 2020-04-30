import librosa
import sys
y, sr = librosa.load(sys.argv[1])
librosa.output.write_wav(sys.argv[2], y, sr)