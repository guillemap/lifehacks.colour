'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from lifehacks.metaclasses import enum
from .. import Colour, hsla, rgba

################################################################
#######                   base palette                   #######
################################################################
class Palette(metaclass=enum[Colour]):
	BLACK  = rgba(  0,   0,   0)
	WHITE  = rgba(255, 255, 255)
	SHADOW = BLACK.clone(a=50)
	TRANSPARENT = BLACK.clone(a=0)

################################################################
#######                     palette                      #######
################################################################
class Mariana(Palette):
	'''	mariana theme from sublime
	'''
	#          real RGB color           HSL reference
	MARIANA  = rgba( 46, 56, 66)      # hsla(210, 15, 22)
	DARK_0   = rgba( 23, 28, 34)      # MARIANA.clone(l=11)
	DARK_1   = rgba( 28, 34, 40)      # MARIANA.clone(l=13)
	DARK_2   = rgba( 40, 48, 57)      # MARIANA.clone(l=19)
	MEDIUM_0 = MARIANA.clone()        # MARIANA.clone()
	MEDIUM_1 = rgba( 83, 99,113, 75)  # MARIANA.clone(l=40, a=75)
	MEDIUM_2 = rgba(179,183,187)      # MARIANA.clone(l=45)
	LIGHT_0  = rgba(165,172,186)      # hsla(220, 12, 69)
	LIGHT_1  = rgba(215,222,234)      # hsla(220, 28, 88)
	RED      = rgba(255, 82, 96)      # hsla(357, 79, 65)
	CORAL    = rgba(255,113, 76)      # hsla( 13, 93, 66)
	ORANGE   = rgba(255,170, 67)      # hsla( 32, 93, 66)
	YELLOW   = rgba(255,195, 74)      # hsla( 40, 94, 68)
	MINT     = rgba(140,201,143)      # hsla(114, 31, 68)
	TEAL     = rgba( 54,183,181)      # hsla(180, 36, 54)
	BLUE     = rgba( 85,155,209)      # hsla(210, 50, 60)
	PURPLE   = rgba(207,146,201)      # hsla(300, 30, 68)
