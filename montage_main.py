# Mix multiples audio one after another with video :
#ffmpeg -f concat -safe 0 -i playlist.txt -c copy output.wav

# Mix one audio with video :
#ffmpeg -i .mkv -i '.mp3' -map 0:v -map 1:a -c copy -shortest .mp4

# Open, read and execute the core system.
exec(open("montage_core.py").read())

# TODO : add WAOU effects
# TODO : format list of text at timestamp in video
# TODO : add GUI

# Displays a nice little logo
ADD_MUSIC = False
input_video_path = "input/"
input_audio_path = "audio_library/"
description_template = open("montage_description_temp.txt").read()
music_description_template = open("montage_music_description_temp.txt").read()

# We can load the differents arguments from the title of each video files
# inside of the input folder so that each section will be edited
# depending of what the goal is.

# Title is split by ";" character
# Syntax : "[order];silence=[true/false];volume=[];speed=[];title=[]".mkv
# [order] for the order of concat of the video
# silence=[true/false] to silence the sound of the video
# volume=[] to change the volume of the background music
# speed=[] to speed up or slow down the video (will silence the video)
# title=[] to add a title text in the begining of this section


class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		input_videos = len(getListFile(input_video_path))
		input_musics = len(getListFile(input_audio_path))

		self.text = tk.Label(self)
		self.text["text"] = str(input_videos)+" video files detected\n"+str(input_musics)+" music files detected"
		self.text.pack(fill="both",expand=1)

		self.music_list_updater("create")

		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "Raffraîchir"
		self.hi_there["command"] = self.music_list_updater("update")
		self.hi_there.pack(fill="both",expand=1)

		self.quit = tk.Button(self, text="Fermer", fg="red",
							  command=self.master.destroy)
		self.quit.pack(fill="both",expand=1)

	def say_hi(self):
		print("hi there, everyone!")

	def music_list_updater(self, command):
		if(command == "update"):
			longest_music_name_count = 0
			audio_files = getListFile(input_audio_path)
			if(len(audio_files)>0):
				for music_file in audio_files:
					if(len(music_file)>longest_music_name_count):
						longest_music_name_count = len(music_file)

			self.music_list = tk.Listbox(self, selectmode="BROWSE", width=longest_music_name_count)
			listbox_index = 0
			audio_files = getListFile(input_audio_path)
			if(len(audio_files)>0):
				for music_file in audio_files:
					self.music_list.insert(listbox_index, music_file)
					listbox_index += 1
			self.music_list.pack(fill="both",expand=1)
		if(command == "" or command == "create"):
			longest_music_name_count = 0
			audio_files = getListFile(input_audio_path)
			if(len(audio_files)>0):
				for music_file in audio_files:
					if(len(music_file)>longest_music_name_count):
						longest_music_name_count = len(music_file)

			self.music_list = tk.Listbox(self, selectmode="BROWSE", width=longest_music_name_count)
			listbox_index = 0
			audio_files = getListFile(input_audio_path)
			if(len(audio_files)>0):
				for music_file in audio_files:
					self.music_list.insert(listbox_index, music_file)
					listbox_index += 1
			self.music_list.pack(fill="both",expand=1)

#root = tk.Tk()
#root.geometry("500x500")
#root.pack_propagate(0)
#root.title("Montage")
#app = Application(master=root)
#app.mainloop()
#terminate()

# Clear the temp file folder
clearTemp()



namesWithRanks = [
	["Accropolis", ["Modérateur", "Personnalité importante", "Divin random"]],
	["Constantino1st", ["Modérateur", "Maire de Scranton"]],
	["BASTIENGAMES", ["Président de l'Assemblée"]],
	["Azothyx", ["Assistant du Président de l'Assemblée", "Maire d'Accrocity"]],
	["Sorbioux_", ["Premier Ministre"]],
	["Ludoclem974", ["Juge Fédéral"]],
	["Ssotark", ["Ministre", "Bienfaiteur de Moukaté"]],
	["__veto__", ["Ministre"]],
	["pingouin_frileux", ["Ministre"]],
	["mininyne", ["Ministre"]],
	["lechatdegoutiere", ["Maire de Coalgate"]],
	["ValSlender", []],
	["Aurom69", []],
	["miquel", ["Intervenant", "Consultant Business Intelligence", "Chez Next Decision"], "Jean MIQUEL"],
	["pernelle", ["Intervenant", "Product Owner Mobile", "Chez WebGeoServices"], "Leo PERNELLE"],
	["thevenon", ["Intervenant", "Chef de projet adjoint", "Responsable technique", "Chez Sopra Steria"], "Romain THEVENON"],
	["champion", ["Intervenant", "Adjointe au DSI", "Cheffe de service", "Au Conseil départemental de l'Héraut"], "Helene CHAMPION"],
	["leo", ["Organisateur", "Etudiant en IG4"], "Leo BRUNET"],
	["alyzee", ["Organisatrice", "Etudiante en IG4"], "Alizee GOUGET"],
	["clement", ["Organisateur", "Etudiant en IG4"], "Clément CANTERO"],
	["nicolas", ["Organisateur", "Etudiant en IG4"], "Nicolas BOFI"]
]

for nameWithRank in namesWithRanks:
	# nameWithRank[1].insert(0, "Citoyen Accrocraftien")
	for i in range(0, len(nameWithRank[1])):
		nameWithRank[1][i] = nameWithRank[1][i].replace("'", "-quote-")
	# print("[REGISTER] <" + nameWithRank[0] + ">   [" + "][".join(nameWithRank[1]).replace('-quote-', '\'') + "]")

# Making the intro if does not exists
intro_filename = "input/0.mkv"
intro_filename_temp = "input/0b.mkv"
if (os.path.isfile(intro_filename)):
	os.remove(intro_filename)
if (os.path.isfile(intro_filename_temp)):
	os.remove(intro_filename_temp)


credit_filename = "input/99999999999999.mkv"
credit_filename_temp = "input/99999999999999b.mkv"
if (os.path.isfile(credit_filename)):
	os.remove(credit_filename)
if (os.path.isfile(credit_filename_temp)):
	os.remove(credit_filename_temp)

from shutil import copyfile
copyfile("fond_video_polytech.mp4", intro_filename_temp)
copyfile("fond_video_polytech.mp4", credit_filename_temp)
logo_filename = "logo_polytech.png"
from PIL import Image
im = Image.open(logo_filename)
logo_width, logo_height = im.size

while(logo_width > 180 or logo_height > 180):
	logo_width = logo_width*0.9
	logo_height = logo_height*0.9

logo_width = str(logo_width)
logo_height = str(logo_height)
logo_scaling = logo_width+':'+logo_height

doPrint("Generating cover video...")
# copyfile(intro_filename_temp, intro_filename)
os.system('ffmpeg -i '+intro_filename_temp+' -i '+logo_filename+' -filter_complex "[1:v]scale='+logo_scaling+'[ovrl],[0:v][ovrl] overlay=10:10/2:enable=\'between(t,0,11)\'" -pix_fmt yuv420p -c:a copy '+intro_filename+">/dev/null 2>&1")
if (os.path.isfile(intro_filename_temp)):
	os.remove(intro_filename_temp)

# os.rename(intro_filename, intro_filename_temp)
# os.system('ffmpeg -i '+intro_filename_temp+' -i subscribe.mp4 -filter_complex "[1:v]scale=-1:480[ckout],[ckout]chromakey=0x5ffb02:0.05:1[ckout];[0:v][ckout]overlay=(0):(1080-480)[out]" -map "[out]" '+intro_filename+">/dev/null 2>&1")
# if (os.path.isfile(intro_filename_temp)):
# 	os.remove(intro_filename_temp)

doPrint("Generating credit video...")
# copyfile(credit_filename_temp, credit_filename)
os.system('ffmpeg -i '+credit_filename_temp+' -i '+logo_filename+' -filter_complex "[1:v]scale='+logo_scaling+'[ovrl],[0:v][ovrl] overlay=10:10/2:enable=\'between(t,0,11)\'" -pix_fmt yuv420p -c:a copy '+credit_filename+">/dev/null 2>&1")
if (os.path.isfile(credit_filename_temp)):
	os.remove(credit_filename_temp)

# os.rename(credit_filename, credit_filename_temp)
# os.system('ffmpeg -i '+credit_filename_temp+' -i subscribe.mp4 -filter_complex "[1:v]scale=-1:480[ckout],[ckout]chromakey=0x5ffb02:0.05:1[ckout];[0:v][ckout]overlay=(0):(1080-480)[out]" -map "[out]" '+credit_filename+">/dev/null 2>&1")
# if (os.path.isfile(credit_filename_temp)):
# 	os.remove(credit_filename_temp)

# Rename all of the files with a space by a _
video_files = getListFile(input_video_path)
if(len(video_files)>0):
	for video_file in video_files:
		file_path = input_video_path + video_file
		os.rename(file_path, file_path.replace(' ', '_').replace('\'', '-quote-'))
		
		video_file = video_file.replace(' ', '_').replace('\'', '-quote-')
		video_file = video_file.split(".")
		video_ext = video_file.pop()
		video_file = ".".join(video_file)
		if(video_ext != "mkv"):
			doPrint("[ERR] Non-mkv format file will be converted to correct video format (mkv)")
			os.system("ffmpeg -i '"+input_video_path+video_file+"."+video_ext+"' -codec copy '"+input_video_path+video_file+".mkv'>/dev/null 2>&1")
			os.unlink(input_video_path+video_file+"."+video_ext)

# Take all of the inputs videos in the input folder
# and parse their names to search for arguments and then
# load differents parts of the script
doPrint("Parsing arguments...")
if(folderExists(input_video_path)):
	# Check the list of files in the input folder
	video_files = getListFile(input_video_path)
	if(len(video_files)>0):
		for video_file in video_files:
			path_to_video_file = input_video_path + video_file
			
			video_file = video_file.split(".")
			video_ext = video_file.pop()
			video_file = ".".join(video_file)
			path_to_video_file_tmp = input_video_path + video_file + "2." + video_ext

			arguments = video_file.split(";")
			if(len(arguments)>0):
				for argument in arguments:
					value = argument.split("=")
					if(len(value)>1):
						argument = value[0]
						value = value[1]
						#If the video is sped
						if(argument=="speed"):
							doPrint("Changing speed of " + video_file + "...")
							value = float(value)
							os.rename(path_to_video_file, path_to_video_file_tmp)
							os.system('ffmpeg -i "'+path_to_video_file_tmp+'" -r '+str(4*value)+' -filter:v "setpts='+str(1/value)+'*PTS" -an -shortest "'+path_to_video_file+"\">/dev/null 2>&1")
							os.remove(path_to_video_file_tmp)

						if(argument=="cut_silence" and argument!="speed" and argument!="silence"):
							if(value=="true"):
								print('truc')

						#If video is silenced
						if(argument=="silence"):
							if(value=="true"):
								doPrint("Silencing " + video_file + "...")
								os.rename(path_to_video_file, path_to_video_file_tmp)
								os.system("ffmpeg -i '"+path_to_video_file_tmp+"' -c copy -an '"+path_to_video_file+"'>/dev/null 2>&1")
								os.remove(path_to_video_file_tmp)
	else:
		doPrint("No input files detected")
		terminate()
else:
	doPrint("No input folder detected")
	terminate()

# Once the speed up, slow down and silence process is complete
# We take all of the video inputs again and calculate to different points
# where the volume of the music need to be reduced
volumes = []
bandeau = []
titles = []
subtitles = []
skins = []

length = 0
video_files = getListFile(input_video_path)
if(len(video_files)>0):
	for video_file in video_files:
		path_to_video_file = input_video_path + video_file
		arguments = video_file.split(";")
		if(len(arguments)>0):
			sameTitleAsLast = False
			sameSubtitleAsLast = False
			sameSkinAsLast = False

			for argument in arguments:
				value = argument.split("=")
				if(len(value)>1):
					argument = value[0]
					value = value[1].replace("."+video_ext, '')
					from_point = length
					to_point = length+getLengthOfVideo(path_to_video_file)

					if(argument=="skin"):
						if(len(skins) > 0 and value.replace('_', ' ') == skins[len(skins)-1][2]):
							sameSkinAsLast = True

					if(argument=="title"):
						if(len(titles) > 0 and value.replace('_', ' ') == titles[len(titles)-1][2]):
							sameTitleAsLast = True

					if(argument=="subtitle"):
						if(len(subtitles) > 0 and value.replace('_', ' ') == subtitles[len(subtitles)-1][2]):
							sameSubtitleAsLast = True


			for argument in arguments:
				value = argument.split("=")
				if(len(value)>1):
					argument = value[0]
					value = value[1].replace("."+video_ext, '')
					from_point = length
					to_point = length+getLengthOfVideo(path_to_video_file)
					#If there is a bandeau
					if(argument=="bandeau"):
						bandeau.append([from_point, to_point, value.replace('_', ' ')])
					#If there is a skin
					if(argument=="skin"):
						if(sameSkinAsLast):
							skins[len(skins)-1][1] = to_point
						else:
							skins.append([from_point, to_point, value.replace('_', ' ')])
					#If there is a subtitle
					if(argument=="subtitle"):
						if(sameSubtitleAsLast and sameTitleAsLast):
							subtitles[len(subtitles)-1][1] = to_point
						else:
							subtitles.append([from_point, to_point, value.replace('_', ' ')])
					#If there is a title
					if(argument=="title"):
						if(sameTitleAsLast and sameSubtitleAsLast):
							titles[len(titles)-1][1] = to_point
						else:
							titles.append([from_point, to_point, value.replace('_', ' ')])
					#If there is a volume
					if(argument=="volume" and value!=""):
						#if(value == 0 or value == "0"):
						#	value = 0.01
						volumes.append([from_point, to_point, value])
		length += getLengthOfVideo(path_to_video_file)


description_to_display = ""
for title in titles:
	from_point = title[0]
	to_point = title[1]
	content = title[2]
	space = ""
	#if(content!="Proposition de loi" and content!="Déclaration" and content!="Intervention" and content!="Annonce" and content!="Introduction" and content!="Vote"):
	#	space = "	"

	description_to_display = description_to_display + "\n" + space + str(datetime.timedelta(seconds=int(from_point))) + " " + content
	for subtitle in subtitles:
		if(subtitle[0]==from_point):
			description_to_display = description_to_display + " : " + subtitle[2]
	
	for skin in skins:
		if(skin[0]==from_point):
			description_to_display = description_to_display + " (" + skin[2] + ")"

for skin in skins:
	isRegistered = False
	for nameWithRank in namesWithRanks:
		if skin[2] == nameWithRank[0]:
			isRegistered = True
	if not isRegistered:
		print("[WARN] NOT REGISTERED: " + skin[2])

f = open("description.txt", "w")
f.write(description_to_display.replace("-quote-", "\u2019"))
f.close()

total_video_length = 0
audio_from_video_lines = []
video_playlist_list = ""
# Extract the audio from the videos and put them in the audio_from_video temp folder
# And calculate the length of all of the videos in total
for video_file in video_files:
	video_length = getLengthOfVideo(input_video_path + video_file)
	total_video_length = total_video_length + video_length
	video_playlist_list += "file " + "'../input/" + video_file + "'\n"
	audio_from_video_lines.append(video_file + ".mp3")
	doPrint("[GET] Loading video file '" + video_file + "' (" + str(video_length) + "s)...")
	# Check if the audio has already been extracted and if not, extract it
	# Note : Silent audios are extract before hand
	path_to_video_file = "input/"+video_file
	if(containAudio(path_to_video_file)):
		max_volume = getMaxVolume(path_to_video_file)
		soundnorm = max_volume * -1
		os.system("ffmpeg -i \""+path_to_video_file+"\" -af \"volume="+str(soundnorm)+"dB\" -map \"0:a?\" \"temp/audio_from_video/"+video_file+".mp3\">/dev/null 2>&1")
	else:
		os.system('ffmpeg -f lavfi -i anullsrc=channel_layout=5.1:sample_rate=48000 -t '+str(getLengthOfVideo(path_to_video_file))+' "temp/audio_from_video/'+video_file + ".mp3\">/dev/null 2>&1")
appendTemp("video_playlist", video_playlist_list)

# Lists all of the audio files in the audio library folder
audio_files = getListFile(input_audio_path)
nearest_audio = ""
nearest_audio_between = total_video_length

# Gets the maximum audio length of the audio library
max_audio_duration = 0
for audio_file in audio_files:
	duration_audio_file = getLengthOfAudio(input_audio_path + audio_file)
	if(duration_audio_file > max_audio_duration):
		max_audio_duration = duration_audio_file
end_video_length = total_video_length


audio_playlist_array = []
audio_playlist_list = ""
from_point = 0
to_point = 0



# Lists in a temp file a list of all audio from video files
audio_from_video_list = ""
for audio_from_video_line in audio_from_video_lines:
	audio_from_video_list += "file 'audio_from_video/" + audio_from_video_line + "'\n"
appendTemp("audio_from_video_playlist", audio_from_video_list)


if(ADD_MUSIC):
	# Appends random musics to stick on the length of the video files
	# so that there is a background music all along
	# And then lists in a temp file a list of all audio files selected
	while(end_video_length > max_audio_duration):
		random_audio = random.choice(audio_files)
		f_random_audio = random_audio.replace(".mp3", "")
		is_in_music_array = False
		for music in audio_playlist_array:
			if(music[0] == random_audio):
				is_in_music_array = True
		if not(is_in_music_array):
			audio_length = getLengthOfAudio(input_audio_path + random_audio)
			audio_playlist_list += "file " + "'../audio_library/"+random_audio+"'\n"
			doPrint("[SET] Loading music file '" + f_random_audio + " (" + str(audio_length) + "s)...")
			# soup = getBeautifulSoup(f_random_audio)
			# doPrint("[INF] Author : "+getInfoFromYoutube(soup, "name_author") + " ("+getInfoFromYoutube(soup, "link_author")+")")
			# doPrint("[INF] Music : "+getInfoFromYoutube(soup, "name_video") + " ("+getInfoFromYoutube(soup, "link_video")+")\n")
			to_point = to_point + audio_length
			audio_playlist_array.append([random_audio, from_point, to_point])
			from_point = from_point + audio_length
			end_video_length = end_video_length - audio_length
	appendTemp("audio_playlist", audio_playlist_list)

	# Then, try to find a music to fill the last empty gap there is in the end
	# of the video without music.
	for audio_file in audio_files:
		duration_audio_file = getLengthOfAudio(input_audio_path + audio_file)
		difference_between = duration_audio_file - end_video_length
		if(difference_between < 0):
			difference_between = difference_between * -1
		if(difference_between < nearest_audio_between):
			nearest_audio = audio_file
			nearest_audio_between = difference_between

	# If it found one, it adds it to the audio temp file listing
	if(nearest_audio != ""):
		audio_length = getLengthOfAudio(input_audio_path + nearest_audio)
		to_point = to_point + audio_length
		audio_playlist_array.append([nearest_audio, from_point, to_point])
		from_point = from_point + audio_length
		doPrint("[SET] Loading music file '" + nearest_audio + " (" + str(audio_length) + "s)...")
		#soup = getBeautifulSoup(nearest_audio)
		#doPrint("[INF] Author : "+getInfoFromYoutube(soup, "name_author") + " ("+getInfoFromYoutube(soup, "link_author")+")")
		#doPrint("[INF] Music : "+getInfoFromYoutube(soup, "name_video") + " ("+getInfoFromYoutube(soup, "link_video")+")\n")
		appendTemp("audio_playlist", "file " + "'../audio_library/" + nearest_audio + "'\n")

# Download skins if any
import requests
skin_index = 1
for skin in skins:
	skin_filename = str(skin_index)
	
	if(fileExists("skin/" + str(skin[2]) + ".png")):
		copyfile("skin/" + str(skin[2]) + ".png", "temp/skins/" + skin_filename + '.png')
	else:
		doPrint("[GET] Skin " + str(skin_index) + " of " + skin[2])
		img_data = requests.get("https://minotar.net/bust/"+skin[2]+"/200.png").content
		if len(skin_filename) < 2:
			skin_filename = "0" + skin_filename;
		with open("temp/skins/" + skin_filename + '.png', 'wb') as handler:
			handler.write(img_data)
	skin_index = skin_index + 1

# We merge all the video inputs in one video file
doPrint("Compiling video playlist...")
os.system("ffmpeg -f concat -safe 0 -i temp/video_playlist.txt -c copy temp/video_playlist.mkv>/dev/null 2>&1")

# We merge all of the audio from videos inputs in one audio file
doPrint("Compiling audio from video playlist...")
os.system("ffmpeg -f concat -safe 0 -i temp/audio_from_video_playlist.txt temp/audio_from_video_playlist.mp3>/dev/null 2>&1")

# We merge all of the music audio in one audio file
if(ADD_MUSIC):
	doPrint("Compiling music playlist...")
	os.system('ffmpeg -f concat -safe 0 -i temp/audio_playlist.txt temp/audio_playlist.mp3>/dev/null 2>&1')

	if not fileExists("temp/audio_playlist.mp3"):
		doPrint("[FATAL ERROR] Music playlist could not be generated and caused a major system crash")
		doPrint("[FATAL ERROR] This is probably caused by an insufficient video length")
		doPrint("[FATAL ERROR] Please check that the length of all inputted videos is greather than")
		doPrint("[FATAL ERROR] the shortest music file in the audio library")
		terminate()

	doPrint("Applying volume settings...")
	# We change the volume according to the volumes set
	volume_string = ""
	for volume in volumes:
		from_point = volume[0]
		to_point = volume[1]
		value = volume[2]
		volume_string += 'volume=enable=\'between(t,'+str(from_point)+','+str(to_point)+')\':volume='+str(value)+','

	# We apply theses changes to the audio
	if(volume_string != ""):
		os.rename("temp/audio_playlist.mp3", "temp/audio_playlist2.mp3")
		os.system('ffmpeg -i temp/audio_playlist2.mp3 -af "'+volume_string[:-1]+'" temp/audio_playlist.mp3>/dev/null 2>&1')
		os.remove('temp/audio_playlist2.mp3')

# We merge the music audio with the audio from the videos together
if(ADD_MUSIC):
	doPrint("Merging audios playlists...")
	os.system("ffmpeg -i temp/audio_playlist.mp3 -i temp/audio_from_video_playlist.mp3 -filter_complex amix=inputs=2:duration=longest temp/merged_audio_playlists.mp3>/dev/null 2>&1")
else:
	os.rename("temp/audio_from_video_playlist.mp3", "temp/merged_audio_playlists.mp3")

# We merge the audio with the video all together
doPrint("Merging audio and video...")
os.system("ffmpeg -i temp/video_playlist.mkv -i temp/merged_audio_playlists.mp3 -map 0:v -map 1:a -shortest -c copy temp/final_load.mkv>/dev/null 2>&1")


output_name_file = "output/output_"+time.strftime("%H%M%S", time.localtime())+".mkv"

# We format the text on the video with the title
# the music titles
# and some messages
doPrint("Formatting text data...")

font_path = "Minecraft.otf"
font_path_black = "Minecraft-Bold.otf"
font_path_italic = "Minecraft-Italic.otf"
font_path_bold = "Minecraft-Bold.otf"
font_path_italic_bold = "Minecraft-BoldItalic.otf"

font_path = "ForcedSquare.ttf"
font_path_black = font_path
font_path_italic = font_path
font_path_bold = font_path
font_path_italic_bold = font_path

font_path = "Montserrat-Light.ttf"
font_path_black = "Montserrat-Black.ttf"
font_path_italic = "Montserrat-Italic.ttf"
font_path_bold = "Montserrat-Bold.ttf"
font_path_italic_bold = "Montserrat-BoldItalic.ttf"


draw_texts = []

# x='if(lt(t-t2+1\,0)\,x1+(x2-x1)*(t-t1)/(t2-t1-1)\,x)'
# y='if(lt(t-t2+1\,0)\,y1+(y2-y1)*(t-t1)/(t2-t1-1)\,y)'


coordinates_music_name = "boxborderw=5: x=(w-text_w)/2: y=(h-text_h-20)"
coordinates_music_title = "boxborderw=5: x=(w-text_w)/2: y=(h-text_h-70)"

coordinates = "boxborderw=5: x=(w-text_w)/2: y=(h-text_h-20)"
coordinates_intro_title = "boxborderw=50: x=(w-text_w)/2: y=(h-text_h)/2-text_h*2"
coordinates_intro_subtitle = "boxborderw=5: x=(w-text_w)/2: y=65+(h-text_h)/2-text_h*2"
coordinates_title = "boxborderw=5: x=(w-text_w)/2: y=(h-text_h-70)"
coordinates_text = "boxborderw=10: x=(w-text_w)/2: y=text_h+20"
for audio_playlist_array_element in audio_playlist_array:
	music_name_formatted = audio_playlist_array_element[0].split(".")
	music_name_formatted = music_name_formatted[:-1]
	for music_name_formatted_element in music_name_formatted:
		music_name_formatted = music_name_formatted_element+"."
	music_name_formatted = music_name_formatted[:-1]
	music_begin = audio_playlist_array_element[1]
	
	draw_texts = movingEffectText("", draw_texts, music_name_formatted, font_path_italic, "30", "(w-tw)/2", "(w-tw)/2", "h", "h-th-10", music_begin, music_begin+7, 2)
	draw_texts = movingEffectText("", draw_texts, music_name_formatted, font_path_italic, "30", "(w-tw)/2", "(w-tw)/2", "h-th-10", "h", music_begin+7, music_begin+9, 2)

#draw_texts.append("drawtext=fontfile="+font_path+": text='Prochaine séance le 29 avril 2020': fontcolor=white: fontsize=40: shadowcolor=black: shadowx=2: shadowy=2: enable='between(t,"+str(total_video_length-5)+","+str(total_video_length)+")': "+coordinates_intro_title)
#draw_texts.append("drawtext=fontfile="+font_path_bold+": text='Assemblée du 22 avril 2020': fontcolor=white: fontsize=60: shadowcolor=black: shadowx=2: shadowy=2: enable='between(t,5,11)': "+coordinates_intro_title)
#draw_texts.append("drawtext=fontfile="+font_path+": text='Marqueurs temporels en description': fontcolor=white: fontsize=30: shadowcolor=black: shadowx=2: shadowy=2: enable='between(t,5,11)': "+coordinates_intro_subtitle)
#draw_texts = typingEffectTitle(draw_texts, "Merci de votre visionnage", total_video_length-10, total_video_length, font_path, coordinates_intro_title, 40, False)
draw_texts = typingEffectTitle(draw_texts, "", 5, 11, font_path_bold, coordinates_intro_title, 60, False)
draw_texts = typingEffectTitle(draw_texts, "", 5, 11, font_path_bold, coordinates_intro_subtitle, 30, False)

# Getting list of usernames
usernames = []
for skin in skins:
		skin_name = skin[2]
		for nameWithRank in namesWithRanks:
			if skin[2] == nameWithRank[0]:
				if(len(nameWithRank) > 2):
					skin_name = nameWithRank[2]
		if not skin_name in usernames:
			usernames.append(skin_name)

credit_messages = [
	"Organisé par",
	"Leo BRUNET",
	"Alizee GOUGET",
	"Clement CANTERO",
	"Nicolas BOFI",
	"Sofia BOUAKLAYENE",
	"",
	"Vincent BARET",
	"Adnane EL ABBAS",
	"Souhaila KESBI",
	"Ouissem REDJEMI",
	"Joan Heimanu TERIIHOANIA",
	"",
	"Monté par [Automated video montage]",
	"par Joan TERIIHOANIA",
	"",
	"Pour POLYTECH MONTPELLIER",
	"Journée des métiers IG 2022"
]

sizeCreditTitles = 40
sizeCreditLines = 20
marginTopTitles = 20
marginBottomTitles = 5

creditLength = 9
creditFromPoint = total_video_length - creditLength
creditToPoint = total_video_length

creditHeight = marginTopTitles*5 + marginBottomTitles*3 +  sizeCreditTitles*5 + len(usernames)*sizeCreditLines + len(audio_playlist_array)*sizeCreditLines + len(credit_messages)*sizeCreditLines
# doPrint(str(creditHeight))
creditFromPointTop = 1000
creditToPointTop = 0 - creditHeight


creditFromPointTop = creditFromPointTop + marginTopTitles
creditToPointTop = creditToPointTop + marginTopTitles
draw_texts = movingEffectText("", draw_texts, "Crédit", font_path_bold, str(sizeCreditTitles), "(w-tw)/2", "(w-tw)/2", str(creditFromPointTop), str(creditToPointTop), creditFromPoint, creditToPoint, creditLength)
creditFromPointTop = creditFromPointTop + sizeCreditTitles + marginBottomTitles
creditToPointTop = creditToPointTop + sizeCreditTitles + marginBottomTitles

for credit_message in credit_messages:
	if credit_message != "":
		draw_texts = movingEffectText("", draw_texts, credit_message, font_path_bold, str(sizeCreditLines), "(w-tw)/2", "(w-tw)/2", str(creditFromPointTop), str(creditToPointTop), creditFromPoint, creditToPoint, creditLength)
	
	creditFromPointTop = creditFromPointTop + sizeCreditLines
	creditToPointTop = creditToPointTop + sizeCreditLines

# creditFromPointTop = creditFromPointTop + marginTopTitles
# creditToPointTop = creditToPointTop + marginTopTitles
# draw_texts = movingEffectText("", draw_texts, "Orateurs", font_path_bold, str(sizeCreditTitles), "(w-tw)/2", "(w-tw)/2", str(creditFromPointTop), str(creditToPointTop), creditFromPoint, creditToPoint, creditLength)
# creditFromPointTop = creditFromPointTop + sizeCreditTitles + marginBottomTitles
# creditToPointTop = creditToPointTop + sizeCreditTitles + marginBottomTitles

# for username in usernames:
# 	draw_texts = movingEffectText("", draw_texts, username, font_path_bold, str(sizeCreditLines), "(w-tw)/2", "(w-tw)/2", str(creditFromPointTop), str(creditToPointTop), creditFromPoint, creditToPoint, creditLength)
# 	creditFromPointTop = creditFromPointTop + sizeCreditLines
# 	creditToPointTop = creditToPointTop + sizeCreditLines


# creditFromPointTop = creditFromPointTop + marginTopTitles
# creditToPointTop = creditToPointTop + marginTopTitles
# draw_texts = movingEffectText("", draw_texts, "Musiques", font_path_bold, str(sizeCreditTitles), "(w-tw)/2", "(w-tw)/2", str(creditFromPointTop), str(creditToPointTop), creditFromPoint, creditToPoint, creditLength)
# creditFromPointTop = creditFromPointTop + sizeCreditTitles + marginBottomTitles
# creditToPointTop = creditToPointTop + sizeCreditTitles + marginBottomTitles

# for audio_playlist_array_element in audio_playlist_array:
# 	music_name_formatted = audio_playlist_array_element[0].split(".")
# 	music_name_formatted = music_name_formatted[:-1]
# 	for music_name_formatted_element in music_name_formatted:
# 		music_name_formatted = music_name_formatted_element+"."
# 	music_name_formatted = music_name_formatted[:-1]

# 	draw_texts = movingEffectText("", draw_texts, music_name_formatted, font_path_bold, str(sizeCreditLines), "(w-tw)/2", "(w-tw)/2", str(creditFromPointTop), str(creditToPointTop), creditFromPoint, creditToPoint, creditLength)
# 	creditFromPointTop = creditFromPointTop + sizeCreditLines
# 	creditToPointTop = creditToPointTop + sizeCreditLines

# creditFromPointTop = creditFromPointTop + marginTopTitles * 2
# creditToPointTop = creditToPointTop + marginTopTitles * 2
# draw_texts = movingEffectText("", draw_texts, "Merci de votre visionnage", font_path_bold, str(sizeCreditTitles), "(w-tw)/2", "(w-tw)/2", str(creditFromPointTop), str(creditToPointTop), creditFromPoint, creditToPoint, creditLength)


nbList = 3
listSubtitleSize = 20
listTitleSize = 25
subtitleSize = 30
titleSize = 40

marginBetweenMainAndList = 20
marginBetweenListItem = 10


for i in range(0, len(subtitles)):
	subtitle = subtitles[i]
	from_point = subtitle[0]
	to_point = subtitle[1]
	if(i < len(subtitles)-1):
		to_point = subtitles[i+1][0]

	content = subtitle[2]
	draw_texts = movingEffectText("subtitle", draw_texts, content, font_path_italic, "30", "0-tw", "50", "h-th-50", "h-th-50", from_point, to_point-2, 2)
	draw_texts = movingEffectText("subtitle", draw_texts, content, font_path_italic, "30", "50", "0-tw", "h-th-50", "h-th-50", to_point-2, to_point, 2)


for i in range(0, len(titles)):
	title = titles[i]
	from_point = title[0]
	to_point = title[1]
	if(i < len(titles)-1):
		to_point = titles[i+1][0]
	
	content = title[2]
	box_y = "h-10-" + str(subtitleSize + titleSize)
	
	draw_texts = movingEffectText("title", draw_texts, content, font_path_bold, str(titleSize), "0-tw", "150", "h-th-50-20-" + str(subtitleSize), "h-th-50-20-" + str(subtitleSize), from_point, to_point-2, 2)
	draw_texts = movingEffectText("title", draw_texts, content, font_path_bold, str(titleSize), "150", "0-tw", "h-th-50-20-" + str(subtitleSize), "h-th-50-20-" + str(subtitleSize), to_point-2, to_point, 2)

	for j in range(1,nbList):
		if(i+j < len(titles)):
			title = titles[i+j]
			content = title[2]

			#y_list = titleSize + subtitleSize + marginBetweenMainAndList
			y_list = 10

			x_New1 = "w"
			x_New2 = "w-tw-10"
			y_titleNew = str(y_list + ((nbList) * (listSubtitleSize + listTitleSize + marginBetweenListItem)))
			y_subtitleNew = str(y_list + ((nbList) * (listSubtitleSize + listTitleSize + marginBetweenListItem)) + listTitleSize)

			x_movingUp = "w-tw-10"
			y_titleMovingUp1 = str(y_list + ((j+1) * (listSubtitleSize + listTitleSize + marginBetweenListItem)))
			y_titleMovingUp2 = str(y_list + ((j) * (listSubtitleSize + listTitleSize + marginBetweenListItem)))
			y_subtitleMovingUp1 = str(y_list + ((j+1) * (listSubtitleSize + listTitleSize + marginBetweenListItem)) + listTitleSize)
			y_subtitleMovingUp2 = str(y_list + ((j) * (listSubtitleSize + listTitleSize + marginBetweenListItem)) + listTitleSize)

			x_leaving1 = "w-tw-10"
			x_leaving2 = "w"
			y_titleLeaving = str(y_list + ((j) * (listSubtitleSize + listTitleSize + marginBetweenListItem)))
			y_subtitleLeaving = str(y_list + ((j) * (listSubtitleSize + listTitleSize + marginBetweenListItem)) + listTitleSize)

			if j != 1:
				to_point_movingup = to_point
			else:
				to_point_movingup = to_point - 2

			draw_texts = movingEffectText("", draw_texts, content, font_path_bold, str(listTitleSize), x_movingUp, x_movingUp, y_titleMovingUp1, y_titleMovingUp2, from_point, to_point_movingup, 2)

			if j == 1 and i+j-1 > 0:
				draw_texts = movingEffectText("", draw_texts, titles[i+j-1][2], font_path_bold, str(listTitleSize), x_leaving1, x_leaving2, y_titleLeaving, y_titleLeaving, from_point-2, to_point-2, 2)

			if j == nbList-1 and i+j+1 < len(titles):
				draw_texts = movingEffectText("", draw_texts, titles[i+j+1][2], font_path_bold, str(listTitleSize), x_New1, x_New2, y_titleNew, y_titleNew, from_point+2, to_point, 2)

			for subtitle in subtitles:
				if(subtitle[0] == titles[i+j][0]):

					if j != 1:
						to_point_movingup = to_point
					else:
						to_point_movingup = to_point - 2

					subtitle_text = subtitle[2]
					if(len(subtitle[2].split(' ')) > 5):
						subtitle_text = ' '.join(subtitle[2].split(' ')[0:4]) + "..."
					
					draw_texts = movingEffectText("", draw_texts, subtitle_text, font_path, str(listSubtitleSize), x_movingUp, x_movingUp, y_subtitleMovingUp1, y_subtitleMovingUp2, from_point, to_point_movingup, 2)

					if j == 1:
						subtitle_text = subtitles[i][2]
						if(len(subtitles[i][2].split(' ')) > 5):
							subtitle_text = ' '.join(subtitles[i][2].split(' ')[0:4]) + "..."
						
						draw_texts = movingEffectText("", draw_texts, subtitle_text, font_path, str(listSubtitleSize),  x_leaving1, x_leaving2, y_subtitleLeaving, y_subtitleLeaving, from_point-2, to_point-2, 2)

					if j == nbList-1 and i+j+1 < len(subtitles):
						subtitle_text = subtitles[i+j+1][2]
						if(len(subtitles[i+j+1][2].split(' ')) > 5):
							subtitle_text = ' '.join(subtitles[i+j+1][2].split(' ')[0:4]) + "..."
						
						draw_texts = movingEffectText("", draw_texts, subtitle_text, font_path, str(listSubtitleSize), x_New1, x_New2, y_subtitleNew, y_subtitleNew, from_point+2, to_point, 2)


for bandeau_el in bandeau:
	if (bandeau_el[1] - bandeau_el[0]) >= 20:
		bandeau_duration = 20
	else:
		bandeau_duration = (bandeau_el[1] - bandeau_el[0])

	draw_texts = movingEffectText("", draw_texts, bandeau_el[2], font_path_bold, "20", "w+10", "0-tw-10", "h-th-10", "h-th-10", bandeau_el[0], bandeau_el[0], bandeau_duration)


skin_index = 1
for skin in skins:
	skin_height = 270
	skin_name = skin[2]

	for nameWithRank in namesWithRanks:
		if skin[2] == nameWithRank[0]:
			if(len(nameWithRank) > 2):
				skin_name = nameWithRank[2]
	
	draw_texts = movingEffectText("", draw_texts, skin_name, font_path_bold, "30", "0-tw-10", "10", "220", "220", skin[0], skin[1]-2, 1)
	draw_texts = movingEffectText("", draw_texts, skin_name, font_path_bold, "30", "10", "0-tw-10", "220", "220", skin[1]-2, skin[1], 1)
	
	coor_y = 260
	for nameWithRank in namesWithRanks:
		if skin[2] == nameWithRank[0]:
			isTitleType = True
			marginRank = 0
			temp_rank_white = []
			temp_rank_red = []
			for i in range(0, len(nameWithRank[1])):
				rank = nameWithRank[1][i]
				coor_y = coor_y + 20 + marginRank
				skin_height = skin_height + 20
				from_point1 = skin[0] + (i*0.25) 
				to_point1 = skin[1] -2 - (i*0.25)
				if i % 2 == 0:
					temp_rank_red = movingEffectText("rankred", temp_rank_red, rank, font_path_bold, "20", "0-tw-10", "10", str(coor_y), str(coor_y), from_point1, to_point1, 1)
					temp_rank_red = movingEffectText("rankred", temp_rank_red, rank, font_path_bold, "20", "10", "0-tw-10", str(coor_y), str(coor_y), to_point1, skin[1], 1)
					marginRank = 7
				else:
					temp_rank_white = movingEffectText("rankwhite", temp_rank_white, rank, font_path_bold, "20", "0-tw-10", "10+25", str(coor_y), str(coor_y), from_point1, to_point1, 1)
					temp_rank_white = movingEffectText("rankwhite", temp_rank_white, rank, font_path_bold, "20", "10+25", "0-tw-10", str(coor_y), str(coor_y), to_point1, skin[1], 1)
					marginRank = 7
			
			for temp_rank_white_el in temp_rank_white:
				draw_texts.append(temp_rank_white_el)

			for temp_rank_red_el in temp_rank_red:
				draw_texts.append(temp_rank_red_el)
			
	skin_index = skin_index + 1
	#draw_texts.append("drawbox=x=0:y=0:w=220:h="+str(skin_height)+":color=red@0.5:t=fill")

draw_overlays = []
skins_input = " "
skins_map = " "
skin_files = getListFile("temp/skins/")
overlay_animation_duration = 1
if(len(skin_files) > 0):
	skins_input = ""
	overlay_input_1 = "0"	
	skin_index = 1
	for skin_file in skin_files:
		skins_input = skins_input + " -i temp/skins/" + str(skin_index) + ".png"

		coor_animated = "overlay=enable='between(t,"+str(skins[skin_index-1][0])+","+str(skins[skin_index-1][0]+overlay_animation_duration)+")':x=0-210+(t-"+str(skins[skin_index-1][0])+")*210:y=10"
		draw_overlays.append("["+overlay_input_1+"]["+str(skin_index)+"]"+coor_animated+"[v"+str(skin_index)+"]")

		draw_overlays.append("[v"+str(skin_index)+"]["+str(skin_index)+"]overlay=x=10:y=10:enable='between(t,"+str(skins[skin_index-1][0]+overlay_animation_duration)+","+str(skins[skin_index-1][1]-2)+")'[v"+str(skin_index)+"]")

		coor_animated = "overlay=enable='between(t,"+str(skins[skin_index-1][1]-2)+","+str(skins[skin_index-1][1])+")':x=10-(t-"+str(skins[skin_index-1][1]-2)+")*210:y=10"
		draw_overlays.append("[v"+str(skin_index)+"]["+str(skin_index)+"]"+coor_animated+"[v"+str(skin_index)+"]")

		overlay_input_1 = "v" + str(skin_index)
		skin_index = skin_index + 1

	skins_map = "-map \"[" + overlay_input_1 + "]\" -map 0:a"
	doPrint("Compiling overlays data...")
	draw_overlays = ','.join(draw_overlays)
	f = open("script.txt", "w")
	f.write(
		draw_overlays
		.replace("ê", "e")
		.replace("é", "e")
		.replace("è", "e")
		.replace("à", "a")
		.replace("ù", "u")
		.replace("-quote-", "\u2019")
	)

	f.close()
	
	formatted_ffmpeg_command = "ffmpeg -i temp/final_load.mkv"+skins_input+" -filter_complex_script script.txt "+skins_map+" -c:a copy temp/temp_load.mkv"
	# doPrint(formatted_ffmpeg_command)
	os.system(formatted_ffmpeg_command)
	os.unlink("temp/final_load.mkv")
	os.rename("temp/temp_load.mkv", "temp/final_load.mkv")


#ffmpeg -i video -i image1 -i image2 -i image3 
#-filter_complex
#"[0][1]overlay=y=H-h:enable='between(t,2,4)'[v1];
# [v1][2]overlay=y=H-h:enable='between(t,6,8)'[v2];
# [v2][3]overlay=y=H-h:enable='between(t,8,10)'[v3]"
#-map "[v3]" outputVideo.mp4

# We encode them


draw_texts = screenAnimation(draw_texts, font_path_bold, 10)
draw_texts = screenAnimation(draw_texts, font_path_bold, (creditFromPoint - 3))


compile_parts = []
compile_part = []
index = 0

for i in range(0, len(draw_texts)):
	if(index > 500):
		compile_parts.append(compile_part)
		compile_part = []
		index = 0
	compile_part.append(draw_texts[i])
	index = index + 1

if(len(compile_part)>0):
	compile_parts.append(compile_part)

compile_part_number = 1
for compile_part in compile_parts:
	doPrint("Compiling formatted text data part " + str(compile_part_number) + "/"+str(len(compile_parts))+"...")
	compile_part_number += 1

	draw_texts = ','.join(compile_part)
	f = open("script.txt", "w")
	f.write(
		draw_texts
		.replace("ê", "e")
		.replace("é", "e")
		.replace("è", "e")
		.replace("à", "a")
		.replace("ù", "u")
		.replace("-quote-", "\u2019")
	)

	f.close()
	#formatted_ffmpeg_command = "ffmpeg -i temp/final_load.mkv -vf \"[in]"+draw_texts+"[out]\" -vcodec libx264 -crf 18 -acodec copy "+output_name_file+">/dev/null 2>&1"
	formatted_ffmpeg_command = "ffmpeg -i temp/final_load.mkv -filter_complex_script script.txt -c:a copy temp/temp_load.mkv"
	os.system(formatted_ffmpeg_command)

	if not fileExists("temp/temp_load.mkv"):
		doPrint("[FATAL ERROR] Text formatting failed during conversion for current dumped script.")
		doPrint("[FATAL ERROR] All temp files have also been dumped until next bootup for inspection.")
		doPrint("[FATAL ERROR] This error has been triggered by the temp_load file not being generated.")
		doPrint("[FATAL ERROR] -------------------------------------------------")
		doPrint("[FATAL ERROR] Current dumped script content :")
		print(draw_texts)																																																																																																																																																																																																																																																																																																																																																																																																																																																														  
		terminate()
	
	length_final_load = getLengthOfVideo("temp/final_load.mkv")
	length_temp_load = getLengthOfVideo("temp/temp_load.mkv")
	
	diff_length_temp_final_load = length_final_load - length_temp_load
	if diff_length_temp_final_load < 0:
		diff_length_temp_final_load = diff_length_temp_final_load * (-1)
	
	if diff_length_temp_final_load > 30 :
		doPrint("[FATAL ERROR] Text formatting failed during conversion for current dumped script.")
		doPrint("[FATAL ERROR] All temp files have also been dumped until next bootup for inspection.")
		doPrint("[FATAL ERROR] This error has been triggered by different input and output video lengths.")
		doPrint("[FATAL ERROR] -------------------------------------------------")
		doPrint("[FATAL ERROR] Input video file length  : " + str(length_final_load))
		doPrint("[FATAL ERROR] Output video file length : " + str(length_temp_load))
		doPrint("[FATAL ERROR] Current dumped script content :")
		print(draw_texts)
		terminate()

	os.unlink("temp/final_load.mkv")
	os.rename("temp/temp_load.mkv", "temp/final_load.mkv")

os.rename("temp/final_load.mkv", output_name_file)
doPrint("Operation completed")

#msgbox("Encoding complete", "Your videos have been edited and encoded !", 1)
#clearTemp()