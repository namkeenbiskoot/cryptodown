from stegano import lsb

image = input("enter image name: ")
msg = input("enter message: ")

secret = lsb.hide(image, msg)
secret.save("stego.png")
print("Message hidden")

print("Extracted message:", lsb.reveal("stego.png"))