import wave

# Explain
# - wave file structure
# - number of channels
# - sample width
# - framerate/sample_rate
# - number of frames
# - values of a frame

# open wave file
obj = wave.open("output.wav",'rb')

print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate.", obj.getframerate())
print("Number of frames", obj.getnframes())
print("parameters:", obj.getparams())
frames = obj.readframes(obj.getnframes())

print(len(frames) / obj.getsampwidth(), frames[0], type(frames[0]))
obj.close()

# write wave file
sample_rate = 16000.0 # hertz
obj = wave.open("new_file.wav",'wb')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sample_rate)
obj.writeframes(frames)
obj.close()