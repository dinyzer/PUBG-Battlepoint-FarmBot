# -*- coding: utf-8 -*-
from datetime import datetime
import json
import webbrowser
from time import sleep , time
from random import randint
import psutil
from pyautogui import keyDown, keyUp, screenshot, press , click, moveTo
import coords

bps = 0
actual_time = str(datetime.now().strftime('%Y-%m-%d %H-%M-%S'))

class Bot:
	def __init__(self):
		self.pubg_open            = webbrowser.open('steam://rungameid/578080')
		self.game                 = 'TslGame.exe'
		self.crash_procname       = 'BroCrashReporter.exe'
		self.start_state          = 'Starting'
		self.play_state           = 'Playing'
		self.play_timer_max       = 60 * 3
		self.matching_state       = 'Matching'
		self.matching_timer_max   = 60 * 3
		self.loading_state        = 'Loading'
		self.loading_timer_max    = 60 * 3
		self.gameloading_state    = 'Game is loading'
		self.gameloading_timer_max= 60 * 3
		self.state                = 'Starting'
		self.TakeScreenshot       = True
		self.timer                = 0.0
		self.config               = None

	def setConfig(self, resolution_choice):
		with open('configRes.json', encoding='UTF-8') as data_file:
			global data
			data = json.load(data_file)
		if resolution_choice == '720':
			self.config = data[resolution_choice]
		elif resolution_choice == '1080':
			self.config = data[resolution_choice]
		elif resolution_choice == '1440':
			self.config = data[resolution_choice]
		elif resolution_choice == 'w1440':
			self.config = data[resolution_choice]

	def getpixel(self,x, y):
		return screenshot().getpixel((x, y))
	def pixelMatchesColor(self, x, y, expectedRGBColor, tolerance=0):
		pix = self.getpixel(x,y)
		if len(pix) == 3 and len(expectedRGBColor) == 3:
			r, g, b = pix[:3]
			exR, exG, exB = int(expectedRGBColor[0]), int(expectedRGBColor[1]), int(expectedRGBColor[2])
			return (abs(r - exR) <= tolerance) and (abs(g - exG) <= tolerance) and (abs(b - exB) <= tolerance)
		elif len(pix) == 4 and len(expectedRGBColor) == 4:  # RGBA mode
			r, g, b, a = pix
			exR, exG, exB, exA = expectedRGBColor
			return (abs(r - exR) <= tolerance) and (abs(g - exG) <= tolerance) and (abs(b - exB) <= tolerance) and (
			abs(a - exA) <= tolerance)
		else:
			assert False, 'Color mode was expected to be length 3 (RGB) or 4 (RGBA), but pixel is length %s and expectedRGBColor is length %s' % (
                len(pix), len(expectedRGBColor))

	def changeState(self, value):
		self.state = value
		self.timer = 0

	def isGameRunning(self): #True if the game is running false if not
		self.game in (p.name() for p in psutil.process_iter())

	def killgame(self):
		for proc in psutil.process_iter():
			if proc.name == self.game:
				proc.kill()


	def matchesButton(self, position):
		if self.pixelMatchesColor(position[0], position[1], self.getColor('white_button'),
						tolerance=self.config['color_tolerance']) or self.pixelMatchesColor(position[0],
																		position[1],
																		self.getColor('gray_button'),
                                                                        tolerance=self.config['color_tolerance']) \
		or self.pixelMatchesColor(position[0],
							position[1],
							self.getColor('super_white_button'),
							tolerance=self.config['color_tolerance']) or self.pixelMatchesColor(
			position[0], position[1], self.getColor('golden_button'), tolerance=self.config['color_tolerance']):
			return True
		return False

	def checkTimer(self): #Check for timeout
		if self.state == self.loading_state and self.timer > self.loading_timer_max:
			print('Timeout. Restarting the game')
			self.changeState(self.start_state)
		elif self.state == self.matching_state and self.timer > self.matching_timer_max:
			print('Timeout. Restarting the game')
			self.changeState(self.start_state)
		elif self.state == self.play_state and self.timer > self.play_timer_max:
			print('Timeout. Restarting the game')
			self.changeState(self.start_state)
		elif self.state == self.gameloading_state and self.timer > self.gameloading_timer_max:
			print('Timeout. Restarting the game')
			self.changeState(self.start_state)
	def getColor(self,name):
		return (self.config['colors'][name]['r'], self.config['colors'][name]['g'], self.config['colors'][name]['b'])

	def run(self):
		number = 1
		for server in self.config['servers']:
			number += 1
			inp = 0
			number = 1
		for server in self.config['modes']:
			number += 1
		inp = 1

		# Position init
		mode_tick_position       = (self.config['modes'][inp]['tick']['x'], self.config['modes'][inp]['tick']['y'])
		mode_position            = (self.config['modes'][inp]['x'], self.config['modes'][inp]['y'], self.config['modes'][inp]['title'])
		play_button_position     = (self.config['play_button']['x'], self.config['play_button']['y'])
		play_state_position      = (self.config['play_state']['x'], self.config['play_state']['y'])
		text_position            = (self.config['text']['x'], self.config['text']['y'])
		exit_position            = (self.config['exit_to_lobby']['x'], self.config['exit_to_lobby']['y'])
		error_position_check     = (self.config['error_position']['x'], self.config['error_position']['y'])
		error_ok_position        = (self.config['error_ok_position']['x'], self.config['error_ok_position']['y'])
		game_message_position    = (self.config['game_message_position']['x'], self.config['game_message_position']['y'])
		exit_button_position     = (self.config['exit_button_position']['x'], self.config['exit_button_position']['y'])
		reconnect_button_position= (self.config['reconnect_button_position']['x'], self.config['reconnect_button_position']['y'])
		#Reading Timing
		refresh_rate             = self.config['timers']['refresh_rate']
		wait_after_killing_a_game= self.config['timers']['wait_after_killing_a_game']
		start_delay              = self.config['timers']['start_delay']
		animation_delay          = self.config['timers']['animation_delay']
		wait_for_players         = self.config['timers']['wait_for_players']
		exit_animation_delay     = self.config['timers']['exit_animation_delay']
		loading_delay            = self.config['timers']['loading_delay']
		color_tolerance          = self.config['color_tolerance']
		dark_play_color          = self.getColor('dark_play_color')
		play_color               = self.getColor('play_color')
		matching_color           = self.getColor('matching_color')
		matching_tick_color      = self.getColor('matching_tick_color')
		text_start_color         = self.getColor('text_start_color')
		windows_background       = self.getColor('windows_background')
		exit_button_color        = self.getColor('exit_button_color')
		reconnect_button_color   = self.getColor('reconnect_button_color')

		try:
			for proc in psutil.process_iter():
				if proc.name() == self.crash_procname:
					self.killgame()
					sleep(wait_after_killing_a_game)
					self.changeState(self.start_state)
		except Exception as ex:
			print('Something went wrong while killing bug reporter... Error message: {}'.format(ex))
		while True:
			if self.state == self.start_state:
				if self.pixelMatchesColor(error_position_check[0], error_position_check[1], windows_background,
										tolerance=color_tolerance):
					press('enter')
					click(error_ok_position[0],error_ok_position[1])
				self.killgame()
				sleep(wait_after_killing_a_game)
				try:
					self.pubg_open
					self.changeState(self.loading_state)
					sleep(start_delay)
					sleep(10)
					print('Loading PUBG')
				except Exception as ex:
					print('Something went wrong while starating PUBG... Error message: {}'.format(ex))
			elif self.state == self.loading_state:
				if self.pixelMatchesColor(play_state_position[0], play_state_position[1], play_color,
					tolerance=color_tolerance) or self.pixelMatchesColor(play_state_position[0],
																			play_state_position[1],
																			dark_play_color,
																			tolerance=color_tolerance):
					moveTo(play_button_position[0],play_button_position[1])
					sleep(animation_delay)
					print('Selecting the game mode')
					sleep(animation_delay)
					click(mode_position[0],mode_position[1])
					sleep(animation_delay)
					if self.pixelMatchesColor(mode_tick_position[0], mode_tick_position[1], matching_tick_color,
												tolerance=color_tolerance):
						click(mode_tick_position[0],mode_tick_position[1])
						print('Clicking start')
					click(play_button_position[0], play_button_position[1])
					self.changeState(self.matching_state)
					sleep(loading_delay)
					print('Starting matchmaking')
				elif self.pixelMatchesColor(text_position[0], text_position[1], text_start_color, tolerance=color_tolerance):
					print('I see text, so the game is probably ready...')
					self.changeState(self.play_state)
				elif self.pixelMatchesColor(reconnect_button_position[0], reconnect_button_position[1], reconnect_button_color, tolerance=color_tolerance):
					print('Nice orange button? I\'ll press it!')
					click(reconnect_button_position[0], reconnect_button_position[1])
					sleep(animation_delay)
				elif self.matchesButton(game_message_position):
					print("Cant interact with game, control denied")
				elif not self.pixelMatchesColor(exit_button_position[0], exit_button_position[1], exit_button_color, tolerance=color_tolerance) \
					and not self.pixelMatchesColor(exit_button_position[0], exit_button_position[1], matching_tick_color, tolerance=color_tolerance)\
					and self.timer > 30 and self.isGameRunning():
					print('I can\'t see exit button, so the game is probably ready...')
					sleep(wait_for_players)
					self.changeState(self.play_state)
			elif self.state == self.matching_state:
				if self.pixelMatchesColor(play_state_position[0], play_state_position[1], play_color,
											tolerance=color_tolerance) or self.pixelMatchesColor(play_state_position[0],
																								play_state_position[1],
																								dark_play_color,
																								tolerance=color_tolerance):
					self.changeState(self.loading_state)
					print('debug- going back to loading state')
					sleep(loading_delay)
				if not self.pixelMatchesColor(play_state_position[0], play_state_position[1], matching_color,tolerance=color_tolerance):
					print('debug - play state postion and matching color')
					self.changeState(self.gameloading_state)
					sleep(loading_delay)
					print('Session is loading')
			elif self.state == self.gameloading_state:
				if not self.pixelMatchesColor(play_state_position[0], play_state_position[1], matching_tick_color,
												tolerance=color_tolerance):
					print('Loading is complete')
					sleep(wait_for_players)
					self.changeState(self.play_state)
			elif self.state == self.play_state:
				if not self.pixelMatchesColor(text_position[0], text_position[1], text_start_color, tolerance=color_tolerance):
					wait_for_plane = randint(40, 60)
					print('Time selected was {} seconds'.format(wait_for_plane))
					sleep(wait_for_plane)
					press('f')
					print('F was hit')
					timeout = time() + 315 - wait_for_plane
					keyDown('w')
					keyDown('space')
					print('Pressing space to let you alive if you fall in the water')
					runOnce = False
					stopRunning = False
					while True:
						if time() < timeout:
							if timeout - time() < 120 and stopRunning is not True:
								print("Stopped pressing w at {}".format(time()))
								keyUp('w')
								press('s')
								keyDown('space')
								sleep(3)
								press('capslock')
								stopRunning = True
							elif timeout - time() < 90 and runOnce is not True:
								press('s')
								keyDown('space')
								sleep(3)
								press('z')
								runOnce = True
						else:
							break
					keyUp('space')
					press('capslock')
					press('esc')
					sleep(animation_delay)
					click(exit_position[0], exit_position[1])
					sleep(exit_animation_delay)
					click(exit_position[0], exit_position[1])
					self.changeState(self.loading_state)
					coords.salir()
					global bps
					bps = bps + 60
					print ("You have earned " + str(bps) + "BPs")
					global actual_time
					coords.showbps(str(bps),actual_time)
					coords.coordenadas()
					coords.busy()
					sleep(5)
			sleep(refresh_rate)
			self.timer += refresh_rate
			self.checkTimer()
