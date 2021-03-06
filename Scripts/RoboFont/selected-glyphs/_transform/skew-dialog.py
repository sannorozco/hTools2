# [h] skew glyphs dialog

import math

from vanilla import *

class skewGlyphsDialog(object):

    _title = "skew glyphs"
    _button_w = 60
    _button_h = 30
    _padding = 10
    _offset_x = True

    def __init__(self):
        self.w = FloatingWindow(
                ((self._button_w * 3) + (self._padding * 2) - 2,
                (self._button_h * 2) + (self._padding * 2) + 20),
                self._title)
        # +1
        self.w._skew_x_plus_button_1 = SquareButton(
                (self._padding,
                self._padding,
                self._button_w,
                self._button_h),
                "+1",
                callback=self._skew_x_plus_1)
        # +5
        self.w._skew_x_plus_button_5 = SquareButton(
                (self._button_w + ((self._padding * 1) - 1),
                self._padding,
                self._button_w,
                self._button_h),
                "+5",
                callback=self._skew_x_plus_5)
        # +25
        self.w._skew_x_plus_button_25 = SquareButton(
                ((self._button_w * 2) + (self._padding * 1) - 2,
                self._padding,
                self._button_w,
                self._button_h),
                "+25",
                callback=self._skew_x_plus_25)
        # -1
        self.w._skew_x_minus_button_1 = SquareButton(
                (self._padding,
                self._button_h + (self._padding - 1),
                self._button_w,
                self._button_h),
                "-1",
                callback=self._skew_x_minus_1)
        # -5
        self.w._skew_x_minus_button_5 = SquareButton(
                (self._button_w + ((self._padding * 1) - 1),
                self._button_h + (self._padding - 1),
                self._button_w,
                self._button_h),
                "-5",
                callback=self._skew_x_minus_5)
        # -25
        self.w._skew_x_minus_button_25 = SquareButton(
                ((self._button_w * 2) + ((self._padding * 1) - 2),
                self._button_h + (self._padding - 1),
                self._button_w,
                self._button_h),
                "-25",
                callback=self._skew_x_minus_25)
        # checkbox
        self.w.offset_x_checkbox = CheckBox(
                (self._padding,
                self._button_h + (self._padding * 2) + 25,
                -self._padding,
                20),
                "skew half way from x-height",
                sizeStyle="small",
                value=self._offset_x)
        # open window
        self.w.open()

    def skew_glyphs(self, angle):
        font = CurrentFont()
        _offset_x = self.w.offset_x_checkbox.get()
        for gName in font.selection:
            try:
                font[gName].prepareUndo('skew')
                if _offset_x:
                    offset_x = math.tan(math.radians(angle)) * (font.info.xHeight / 2)
                else:
                    offset_x = 0
                font[gName].skew(angle, offset=(offset_x, 0))
                font[gName].performUndo()
            except:
                print '\tcannot transform %s' % gName                        

    def _skew_x_minus_1(self, sender):
        self.skew_glyphs(-1)

    def _skew_x_minus_5(self, sender):
        self.skew_glyphs(-5)

    def _skew_x_minus_25(self, sender):
        self.skew_glyphs(-25)

    def _skew_x_plus_1(self, sender):
        self.skew_glyphs(1)

    def _skew_x_plus_5(self, sender):
        self.skew_glyphs(5)

    def _skew_x_plus_25(self, sender):
        self.skew_glyphs(25)

    def close_callback(self, sender):
        self.w.close()

# run

skewGlyphsDialog()

