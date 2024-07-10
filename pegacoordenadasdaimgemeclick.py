def testlocateimg_click(fileimg):#recebe o caminho da imagem png
  import pyautogui as pygui
  imgloc= pygui.locateOnScreen(fileimg)#localiza a imagem na tela
  if imgloc!=None:# se a imagem existir
    coord=[] #aponta as coordenadas 
    coord =pygui.center(imgloc)
    x=0
    y=0
    if coord!=[] and coord!=None:
      print('coord->',coord)
      for i in range(len(coord)):
        #print('pos coord->',str(coord[i]))
        x=coord[0]
        y=coord[1]#clica na imagem com duração de 3 segundos
        pygui.click(x,y,duration=3.0)
  else:
    print('imagem não encontrada!')  
