# extracted from https://www.codegrepper.com/code-examples/python/python+convert+image+to+icon
from PIL import Image
filename = r'logo.png'
img = Image.open(r'C:\Users\David\Desktop\micro-bit-logo.png')

# ====================

# Optionally, you may specify the icon sizes you want:

icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
img.save('micro-bit-logo.ico', sizes=icon_sizes)