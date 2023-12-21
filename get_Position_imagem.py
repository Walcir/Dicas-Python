#verificar se uma imagem está aparecendo
def find_image_on_screen(image_path, timeout=10):
  start_time = time.time()
  while time.time() - start_time < timeout:
      # Take a screenshot of the entire screen
      screenshot = pygui.screenshot()
      # Try to locate the image on the screen
      location = pygui.locateOnScreen(image_path, confidence=0.8)
      
      if location:
          # Image found, return the coordinates
          return location.left, location.top
      time.sleep(1)  # Adjust the sleep time based on your needs
  # Image not found within the timeout
  return None

# Example usage
#?image_path = "path/to/your/image.png"
#?#oordinates = find_image_on_screen(image_path)
#?
#?if coordinates:
#?    print(f"Image found at coordinates: {coordinates}")
#?else:
#?    print("Image not found.")
#****************************************************************


# Find window coordinates/pega as coodernadas xy da imagem pelo caminho e o titulo
#?import cv2
#?import pygetwindow as gw
def find_window_coordinates(window_title, template_path, threshold=0.8):
    # Get the target window
    window = gw.getWindowsWithTitle(window_title)[0]

    # Get the screenshot of the entire screen
    screen = gw.screenshot(region=(0, 0, gw.size()[0], gw.size()[1]))

    # Load the template image
    template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)

    # Convert the screenshot to grayscale
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    # Match the template in the screenshot
    result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # If the matching score is above the threshold, consider it a match
    if max_val > threshold:
        # Extract the coordinates of the top-left corner of the matched region
        x, y = max_loc
        return (window.left + x, window.top + y)
    else:
        return None

# Example usage
#?window_title = "Your Window Title"
#?template_path = "path/to/your/template.png"
#?coordinates = find_window_coordinates(window_title, template_path)
#?
#?if coordinates:
#?    print(f"The window is found at coordinates: {coordinates}")
#?else:
#?    print("Window not found.")
#****************************************************************

#pegar por imagem png um objeto elementar (botao,campo e etc...) para ser interativo
def getclickscreen(descri_png):
  print("...Localiza o botao pela imagem ")
  escreve_processo("...Localiza o botao pela imagem ")
  x,y = pygui.locateAllOnScreen(descri_png,confidence=0.9)
  print("..pegou as cordenadas xy ->",str(x)+","+str(y))
  escreve_processo("...pegou as coordenadas xy-> ",str(x)+","+str(y))
  print("...movendo para o botao pela imagem ")
  escreve_processo("...movendo para o botao pela imagem ")
  pygui.moveTo(x,y,3)  
  print("...clicando no botao pela imagem ")
  escreve_processo("...clicando no botao pela imagem ")
  pygui.click()