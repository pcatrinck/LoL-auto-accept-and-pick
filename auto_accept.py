# Import necessary libraries
import pyautogui as pg
from python_imagesearch.imagesearch import imagesearch

# Champion to select
selectChampion = 'fizz'

# Image paths for buttons and elements in the game
acceptButtonImg = 'imgs\sample.png'
acceptedButtonImg = 'imgs\sample-accepted.png'
playButtonImg = 'imgs\play-button.png'
searchIcon = 'imgs\search-icon.png'
winLogo = 'imgs\winLogo.png'

# Similarity threshold for image matching
IMAGE_THRESHOLD = 0.8

# Disable PyAutoGUI failsafe and set a pause after each PyAutoGUI call
pg.FAILSAFE = False
pg.PAUSE = 0.5

# Function to check if the game has been cancelled
def is_game_cancelled():
    accepted, play = imagesearch(acceptedButtonImg, IMAGE_THRESHOLD), imagesearch(playButtonImg, IMAGE_THRESHOLD)
    return accepted[0] == -1 and not play[0] == -1

# Main function that runs the automation script
def run():
    # Enter a loop to continuously check for game availability
    while True:
        if is_game_cancelled():
            print("Game has been cancelled")
            break
        checkGameAvailableLoop()

# Function to continuously check for the availability of the game and click the accept button if found
def checkGameAvailableLoop():
    while True:
        pos = imagesearch(acceptButtonImg, 0.8)
        if not pos[0] == -1:
            pg.click(pos[0], pos[1])
            print("Game accepted")
            select()  # Call the select function after accepting the game
            break

# Function to select the champion by searching for the searchIcon image, clicking on it, typing the champion name, and pressing enter
def select():
    search_sch = imagesearch(searchIcon, IMAGE_THRESHOLD)
    search_win = imagesearch(winLogo, IMAGE_THRESHOLD)
    if not search_sch[0] == -1:
        print('Searching for search icon')
        pg.click(search_sch[0], search_sch[1])
        pg.typewrite(selectChampion)
        pg.press('enter')
    if not search_win[0] == -1:
        print('Game has been cancelled')
        run()

# Entry point of the script
if __name__ == '__main__':
    # Print a message indicating the script has started
    print("Started Searching")

    # Attempt to run the main function in a try-except block to catch any exceptions
    try:
        run()
    except Exception as e:
        # Print an error message if an exception occurs
        print(f"An error occurred: {str(e)}")