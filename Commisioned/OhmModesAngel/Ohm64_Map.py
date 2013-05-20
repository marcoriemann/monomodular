#!/usr/bin/env python
# encoding: utf-8
"""
Ohm64_Map.py

Created by amounra on 2010-10-05.
Copyright (c) 2010 __artisia__. All rights reserved.

This file allows the reassignment of the controls from their default arrangement.  The order is from left to right; 
Buttons are Note #'s and Faders/Rotaries are Controller #'s

"""
CHANNEL = 0		#main channel (0 - 15)

OHM_BUTTONS = [65, 73, 66, 74, 67, 75, 68, 76]    #there are 8 of these

OHM_FADERS = [23, 22, 15, 14, 5, 7, 6, 4]		#there are 8 of these

OHM_DIALS = [17, 16, 9, 8, 19, 18, 11, 10, 21, 20, 13, 12, 3, 1, 0, 2]		#there are 16 of these

OHM_MENU = [69, 70, 71, 77, 78, 79]			#there are 6 of these

CROSSFADER = 24		#single

SHIFT_L = 64		#single

SHIFT_R = 72		#single

LIVID = 87			#single

PAGE1_USER_CHANNEL = 2

PAGE1_USER_MAP = [[0, 8, 16, 24, 32], 
					[1, 9, 17, 25, 33], 
					[2, 10, 18, 26, 34],
					[3, 11, 19, 27, 35],
					[4, 12, 20, 28, 36],
					[5, 13, 21, 29, 37],
					[6, 14, 22, 30, 38],
					[7, 15, 23, 31, 39]]

PAGE2_USER_CHANNEL = 3

PAGE1_DRUM_CHANNEL = 9			#this is the channel for the first (partial right) grid in Right Function Mode 2

PAGE1_DRUM_MAP = 	[[0, 1, 2, 3],			#these are the note numbers for the first (partial) grid in Right Function Mode 2
 					[4, 5, 6, 7],
					[8, 9, 10, 11],
					[12, 13, 14, 15]]
					
PAGE1_BASS_CHANNEL = 10			#this is the channel for the second (full right) grid in Right Function Modes 3 & 4

PAGE1_BASS_MAP = 	[[24, 28, 32, 36],		#these are the note numbers for the first (partial) grid in Right Function Mode 3 & 4
					[25, 29, 33, 37],
					[26, 30, 34, 38],
					[27, 31, 35, 39]]
					
PAGE1_KEYS_CHANNEL = 11

PAGE1_KEYS_MAP =   [[24, 12, 0], 
					[26, 14, 2], 
					[28, 16, 4],
					[29, 17, 5], 
					[31, 19, 7], 
					[33, 21, 9],
					[35, 23, 11],
					[36, 24, 12]]
					
PAGE1_MODES_MAP = [[0, 0, 0, 0, 0, 0, 0, 0], #major or ionian
					[0, 0, -1, 0, 0, 0, -1, 0], #dorian
					[0, -1, -1, 0, 0, -1, -1, 0], #phrygian
					[0, 0, 0, 1, 0, 0, 0, 0],  #lydian
					[0, 0, 0, 0, 0, 0, -1, 0], #mixolydian
					[0, 0, -1, 0, 0, -1, -1, 0], #minor or aeolian
					[0, -1, -1, 0, -1, -1, -1, 0], #locrian
					[0, 0, 0, 0, 0, 0, 0, 0]]
					

BACKLIGHT_TYPE = ['static', 'pulse', 'up', 'down']  #this assigns the backlight mode for left_shift_modes 1-4.  If 'static', the value below will be used

BACKLIGHT_VALUE = [127, 96, 64, 32]		#this assigns the led intensity for the backlight if it is in 'static' mode for left_shift_modes 1-4

OHM_TYPE = ['static', 'pulse', 'up', 'down']	#this assigns the ohm logo mode for right_shift_modes 1-4.  If 'static', the value below will be used

OHM_VALUE = [127, 96, 64, 32]	#this assigns the led intensity for the ohm logo if it is in 'static' mode for right_shift_modes 1-4

PAD_TRANSLATION = 	((0, 0, 0, 9), (0, 1, 1, 9), (0, 2, 2, 9), (0, 3, 3, 9),		#this is used by DrumRacks to translate input to one of the visible grid squares for triggering
					(1, 0, 4, 9), (1, 1, 5, 9), (1, 2, 6, 9), (1, 3, 7, 9),			#the format is (x position, y position, note-number, channel)
					(2, 0, 8, 9), (2, 1, 9, 9), (2, 2, 10, 9), (2, 3, 11, 9),
					(3, 0, 12, 9), (3, 1, 13, 9), (3, 2, 14, 9), (3, 3, 15, 9))
					


FOLLOW = True		#this sets whether or not the last selected device on a track is selected for editing when you select a new track


#	The default assignment of colors within the OhmRGB is:
#	Note 2 = white
#	Note 4 = cyan 
#	Note 8 = magenta 
#	Note 16 = red 
#	Note 32 = blue 
#	Note 64 = yellow
#	Note 127 = green
#	Because the colors are reassignable, and the default colors have changed from the initial prototype,
#		MonOhm script utilizes a color map to assign colors to the buttons.  This color map can be changed 
#		here in the script.  The color ordering is from 1 to 7.  

COLOR_MAP = [2, 64, 4, 8, 16, 32, 127]

#	In addition, there are two further color maps that are used depending on whether the RGB or Monochrome 
#		Ohm64 is detected.  The second number is the color used by the RGB (from the ordering in the COLOR_MAP array),
#		the first the Monochrome.  Obviously the Monochrome doesn't use the colors.  
#	However, the flashing status of a color is derived at by modulus.  Thus 1-6 are the raw colors, 7-12 are a fast
#		flashing color, 13-20 flash a little slower, etc.  127 is always solid.  You can assign your own color maps here:


STOP_CLIP_COLOR = [1, 127]
CLIP_TRIGD_TO_PLAY_COLOR = [1, 12]
CLIP_TRIGD_TO_RECORD_COLOR = [1, 11]
CLIP_STOPPED_COLOR = [1, 1]
CLIP_STARTED_COLOR = [13, 6]
CLIP_RECORDING_COLOR = [19, 5]
ZOOM_STOPPED_COLOR = [1, 1]
ZOOM_PLAYING_COLOR = [13, 6]
ZOOM_SELECTED_COLOR = [7, 8]


ARM_COLOR = [14, 5]
STOP_COLOR = [1, 5]
PLAY_COLOR = [1, 6]
MUTE_COLOR = [1, 2]
CROSSFADE_ASSIGN_COLOR = [1, 4]
SCENE_LAUNCH_COLOR = [7, 1]
NAV_BUTTON_COLOR = [1, 3]
DRUM_COLOR = [20, 6]
KEYS_COLOR = [1, 2]
BASS_COLOR = [32, 5]
DEVICE_NAV_COLOR = [1, 2]
SOLO_COLOR = [7, 3]
TAP_COLOR = [1, 1]
SELECT_COLOR = [127, 1]

## a



