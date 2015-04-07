'''
use it to rename srt files to the file names of avi files, or mp4, mkv ,etc. but you have to update it by yourself.

For example, there are some avi/art files in the folder

The.Wire.S02E01.720p.HDTV.x264-BATV.chs.srt
The Wire Season 2 Episode 01 - Ebb Tide.avi

I want to rename 'The.Wire.S02E01.720p.HDTV.x264-BATV.chs.srt' to  'The Wire Season 2 Episode 01 - Ebb Tide.srt'

'''

import os
import glob
import re

avi_files = glob.glob('*.avi')
srt_files = glob.glob('*.srt')

for avi in avi_files:
	m = re.match(r"The Wire Season\s*(\d+)\s*Episode\s*(\d+)\s*", avi)
	if m:
		season = int(m.group(1))
		episode = int(m.group(2))
		for srt in srt_files:
			m2 = re.match(r"The.Wire.S(\d+)E(\d+).", srt)
			if m2:
				if season == int(m2.group(1)) and episode == int(m2.group(2)):
					# print srt, '------>', avi[:-3]+'srt' 
					os.rename(srt, avi[:-3]+'srt')
