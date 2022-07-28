from queue import Empty
import win32com.client as win

serviceApi = "SAPI.SpVoice"
speaker_Api = win.Dispatch(serviceApi)
while True:
    inputText = str(input("Input word : "))
    if inputText != "exit":
        speaker = inputText
        speaker_Api.Speak(speaker)
    else:
        break