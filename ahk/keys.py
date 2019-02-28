"""
The ahk.keys module contains some useful classes for working with 'special' keys.
It also
"""


class Key:
    is_modifier = False
    symbol = ''

    def __init__(self, key_name):
        self._key_name = key_name

    @property
    def name(self):
        return self._key_name

    @property
    def DOWN(self):
        return '{' + f'{self.name} down' + '}'

    @property
    def UP(self):
        return '{' + f'{self.name} up' + '}'

    def __str__(self):
        return '{' + self.name + '}'

    def __hash__(self):
        return hash(str(self))

    def __mul__(self, n):
        if not isinstance(n, int):
            raise TypeError(f"Unsupported operand type(s) for *: '{self.__class__.__name__}' and '{type(n)}'")
        return '{' + f'{self.name} {n}' + '}'

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __add__(self, s):
        return str(self) + s

    def __repr__(self):
        return f'{self.__class__.__name__}(key_name={self.name!r})'


SYMBOLS = {
    'Win': '#',
    'LWin': '<#',
    'RWin': '>#',
}


class KeyModifier(Key):
    is_modifier = True

    @property
    def symbol(self):
        return SYMBOLS.get(self.name, self.name)

    def __add__(self, other):
        return self.symbol + str(other)


class KEYS:
    """
    KEYS constants
    REF: https://autohotkey.com/docs/KeyList.htm
    """
    CAPS_LOCK = Key('CapsLock')
    CapsLock = CAPS_LOCK
    SCROLL_LOCK = Key('ScrollLock')
    ScrollLock = SCROLL_LOCK
    SPACE = Key('Space')

    TAB = Key('Tab')
    Tab = TAB
    ENTER = Key('Enter')
    Enter = ENTER
    ESCAPE = Key('Escape')
    BACKSPACE = Key('Backspace')
    Backspace = BACKSPACE
    UP = Key('Up')
    Up = UP
    DOWN = Key('Down')
    Down = DOWN
    LEFT = Key('Left')
    Left = LEFT
    RIGHT = Key('Right')
    Right = RIGHT

    WIN = KeyModifier('Win')
    Win = WIN
    LEFT_WIN = KeyModifier('LWin')
    LWin = LEFT_WIN
    RIGHT_WIN = KeyModifier('RWin')
    RWin = RIGHT_WIN
    CONTROL = KeyModifier('Control')
    Control = CONTROL
    CTRL = CONTROL
    Ctrl = CONTROL
    LEFT_CONTROL = KeyModifier('LControl')
    LCtrl = LEFT_CONTROL
    LControl = LEFT_CONTROL
    RIGHT_CONTROL = KeyModifier('RControl')
    RCtrl = RIGHT_CONTROL
    RControl = RIGHT_CONTROL
    ALT = KeyModifier('Alt')
    Alt = ALT
    LEFT_ALT = KeyModifier('LAlt')
    LAlt = LEFT_ALT
    RIGHT_ALT = KeyModifier('RAlt')
    RAlt = RIGHT_ALT
    SHIFT = KeyModifier('Shift')
    Shift = SHIFT
    LEFT_SHIFT = KeyModifier("LShift")
    LShift = LEFT_SHIFT
    RIGHT_SHIFT = KeyModifier('RShift')
    RShift = RIGHT_SHIFT
    NUMPAD_DOT = Key('NumpadDot')
    NumpadDot = NUMPAD_DOT
    NUMPAD_DEL = Key('NumpadDel')
    NumpadDel = NUMPAD_DEL
    NUM_LOCK = Key('NumLock')
    NumLock = NUM_LOCK
    NUMPAD_ADD = Key('NumpadAdd')
    NUMPAD_DIV = Key('NumpadDiv')
    NUMPAD_SUB = Key('NumpadSub')
    NUMPAD_MULT = Key('NumpadMult')
    NUMPAD_ENTER = Key('NumpadEnter')
    NumpadAdd = NUMPAD_ADD
    NumpadDiv = NUMPAD_DIV
    NumpadSub = NUMPAD_SUB
    NumpadMult = NUMPAD_MULT
    NumpadEnter = NUMPAD_ENTER


def _init_keys():
    '''put this in a function to avoid polluting global namespace'''
    for i in range(0, 10):
        #  set numpad keys
        key_name = f'Numpad{i}'
        key = Key(key_name)
        setattr(KEYS, key_name, key)
        setattr(KEYS, key_name.upper(), key)


    for i in range(1, 25):
        # set function keys
        key_name = f'F{i}'
        setattr(KEYS, key_name, Key(key_name))

    for i in range(1, 33):
        # set joystick keys
        key_name = f'Joy{i}'
        setattr(KEYS, key_name, Key(key_name))
        setattr(KEYS, key_name.upper(), Key(key_name))


_init_keys()

__all__ = [name for name in dir(KEYS) if not name.startswith('_')]


def __getattr__(name):
    return getattr(KEYS, name)
