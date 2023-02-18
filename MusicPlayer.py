import pygame
import PySimpleGUI as sg

# Initialize Pygame
pygame.init()

# Define the UI layout
layout = [
    [sg.Text("Music Player")],
    [sg.Text("Choose Music File:")],
    [sg.Input(key="-FILE-", enable_events=True), sg.FileBrowse(file_types=(("Music Files", "*.mp3 *.wav"),))],
    [sg.Button("Play"), sg.Button("Stop")]
]

# Create the PySimpleGUI window
window = sg.Window("Music Player", layout)

# Initialize music file path and playback status
music_file = ""
is_playing = False

# Event loop
while True:
    event, values = window.read()

    # Handle window closed event
    if event == sg.WIN_CLOSED:
        break

    # Handle file selection event
    if event == "-FILE-":
        music_file = values["-FILE-"]

    # Handle play button click event
    if event == "Play":
        # Check if music file is selected
        if not music_file:
            sg.popup_error("Please choose a music file first!")
            continue

        # Load music file
        pygame.mixer.music.load(music_file)

        # Play music
        pygame.mixer.music.play()

        # Set playback status to True
        is_playing = True

    # Handle stop button click event
    if event == "Stop":
        # Stop music playback
        pygame.mixer.music.stop()

        # Set playback status to False
        is_playing = False

    # Disable play button during playback
    if is_playing:
        window["Play"].update(disabled=True)
    else:
        window["Play"].update(disabled=False)

# Clean up Pygame
pygame.quit()

# Close the PySimpleGUI window
window.close()