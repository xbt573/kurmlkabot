from pyrogram import Client
import animeface
from PIL import Image
import os
import cv2

bot = Client("noanime")

with open("num", "w") as f:
	f.write("0")
os.system("rm temp/*")

def incCounter():
	with open("num", "r") as f:
		nextnum = int(f.read())

	with open("num", "w") as f:
		f.write(str(nextnum + 1))

	return nextnum

@bot.on_message()
def onMessage(_, msg):
	with open("num", "r") as f:
		nextnum = int(f.read())

	with open("num", "w") as f:
		f.write(str(nextnum + 1))

	file = bot.download_media(msg, f"temp/{str(nextnum)}")
	print("downloaded")

	if msg.photo:
		result = processImage(file)
	if msg.video or msg.animation:
		result = processVideo(file)
	if msg.sticker:
		result = processSticker(file, msg.sticker.is_animated, msg.sticker.is_video)

	# bot.send_message(msg.chat.id, str(result))
	# bot.delete_messages(msg.chat.id, msg.message_id)
	if result:
		bot.send_animation(msg.chat.id, "noanime.mp4", reply_to_message_id=msg.message_id)

	os.system(f"rm temp/{nextnum}")

def processImage(img):
	image = Image.open(img)
	faces = animeface.detect(image)

	if faces:
		return True

	return False

def processVideo(vid):
	cam = cv2.VideoCapture(vid)
	for i in range(0, 10):
		ret, frame = cam.read()

		if ret:
			counter = incCounter()
			cv2.imwrite(f"temp/{str(counter)}.png", frame)
			
			if processImage(f"temp/{str(counter)}.png"):
				os.system(f"rm temp/{str(counter)}.png")
				return True
		else:
			break

	# os.system(f"rm temp/{str(counter)}.png")
	return False

# def processGif(gif):
# 	pass

def processSticker(sticker, animated, is_video):
	print(str(animated))
	if animated or is_video:
		return processVideo(sticker)

	image = Image.open(sticker).convert("RGB")
	image.save(sticker, "png")
	
	return processImage(sticker)

bot.run()