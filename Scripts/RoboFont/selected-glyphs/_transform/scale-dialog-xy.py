# [h] scale glyphs XY dialog

from vanilla import *

class scaleGlyphsXYDialog(object):

    _title = "scale glyphs xy"
    _button_w = 220
    _button_h = 30
    _padding = 10
    _x_metrics = True
    _y_metrics = False

    def __init__(self):
        self.w = FloatingWindow(
                ((self._button_w * 1) + (self._padding * 2),
                (self._button_h * 6) + (self._padding * 4) - 1 + 65),
                self._title)
        # + 1  
        self.w._scale_plus_x_button_1 = SquareButton(
                (self._padding,
                (self._button_h * 4) + (self._padding *3),
                (self._button_w / 2) + 1,
                self._button_h),
                "X +1%",
                sizeStyle='small',
                callback=self._scale_x_plus_1_callback)
        self.w._scale_plus_y_button_1 = SquareButton(
                (self._padding + (self._button_w / 2),
                (self._button_h * 4) + (self._padding * 3),
                (self._button_w / 2),
                self._button_h),
                "Y +1%",
                sizeStyle='small',
                callback=self._scale_y_plus_1_callback)            
        # + 10
        self.w._scale_plus_x_button_10 = SquareButton(
                ((self._padding * 1),
                (self._padding *2) + (self._button_h * 2),
                (self._button_w / 2) + 1,
                self._button_h),
                "X +10%",
                sizeStyle='small',
                callback=self._scale_x_plus_10_callback)
        self.w._scale_plus_y_button_10 = SquareButton(
                ((self._padding * 1) + (self._button_w / 2),
                (self._padding * 2) + (self._button_h * 2),
                (self._button_w / 2),
                self._button_h),
                "Y +10%",
                sizeStyle='small',
                callback=self._scale_y_plus_10_callback)
        # + 100
        self.w._scale_plus_x_button_100 = SquareButton(
                ((self._padding * 1),
                (self._padding * 1) + (self._button_h * 0),
                (self._button_w / 2) + 1,
                self._button_h),
                "X +100%",
                sizeStyle='small',
                callback=self._scale_x_plus_100_callback)            
        self.w._scale_plus_y_button_100 = SquareButton(
                ((self._padding * 1) + (self._button_w / 2),
                (self._padding * 1) + (self._button_h * 0),
                (self._button_w / 2),
                self._button_h),
                "Y +100%",
                sizeStyle='small',
                callback=self._scale_y_plus_100_callback)
        # - 1
        self.w._scale_minus_x_button_1 = SquareButton(
                (self._padding,
                (self._button_h * 5) + (self._padding * 3) - 1,
                (self._button_w / 2) + 1,
                self._button_h),
                "X -1%",
                sizeStyle='small',
                callback=self._scale_x_minus_1_callback)
        self.w._scale_minus_y_button_1 = SquareButton(
                (self._padding + (self._button_w / 2),
                (self._button_h * 5) + (self._padding * 3) - 1,
                (self._button_w / 2),
                self._button_h),
                "Y -1%",
                sizeStyle='small',
                callback=self._scale_y_minus_1_callback)            
        # - 10
        self.w._scale_minus_x_button_10 = SquareButton(
                (self._padding,
                (self._button_h * 3) + (self._padding * 2) - 1,
                (self._button_w / 2) + 1,
                self._button_h),
                "X -10%",
                sizeStyle='small',
                callback=self._scale_x_minus_10_callback)
        self.w._scale_minus_y_button_10 = SquareButton(
                (self._padding + (self._button_w / 2),
                (self._button_h * 3) + (self._padding * 2) - 1,
                (self._button_w / 2),
                self._button_h),
                "Y -10%",
                sizeStyle='small',
                callback=self._scale_y_minus_10_callback)            
        # - 100
        self.w._scale_minus_x_button_100 = SquareButton(
                ((self._padding * 1),
                (self._button_h * 1) + (self._padding * 1) - 1,
                (self._button_w / 2) + 1,
                self._button_h),
                "X -100%",
                sizeStyle='small',
                callback=self._scale_x_minus_100_callback)            
        self.w._scale_minus_y_button_100 = SquareButton(
                ((self._padding * 1) + (self._button_w / 2),
                (self._button_h * 1) + (self._padding * 1) - 1,
                (self._button_w / 2),
                self._button_h),
                "Y -100%",
                sizeStyle='small',
                callback=self._scale_y_minus_100_callback)
        # metrics
        self.w._metrics_X = CheckBox(
                (15, -60, -15, 20),
                "scale side-bearings (X)",
                value=self._x_metrics)
        self.w._metrics_Y = CheckBox(
                (15, -35, -15, 20),
                "scale vertical metrics (Y)",
                value=self._y_metrics)
        # open window
        self.w.open()

    # x callbacks

    def _scale_x_minus_1_callback(self, sender):
        self.scale_glyphs((0.99, 1))

    def _scale_x_minus_10_callback(self, sender):
        self.scale_glyphs((0.9, 1))

    def _scale_x_minus_100_callback(self, sender):
        self.scale_glyphs((0.5, 1))

    def _scale_x_plus_1_callback(self, sender):
        self.scale_glyphs((1.01, 1))

    def _scale_x_plus_10_callback(self, sender):
        self.scale_glyphs((1.1, 1))

    def _scale_x_plus_100_callback(self, sender):
        self.scale_glyphs((2.0, 1))

    # y callbacks

    def _scale_y_minus_1_callback(self, sender):
        self.scale_glyphs((1, 0.99))

    def _scale_y_minus_10_callback(self, sender):
        self.scale_glyphs((1, 0.9))

    def _scale_y_minus_100_callback(self, sender):
        self.scale_glyphs((1, 0.5))

    def _scale_y_plus_1_callback(self, sender):
        self.scale_glyphs((1, 1.01))

    def _scale_y_plus_10_callback(self, sender):
        self.scale_glyphs((1, 1.1))

    def _scale_y_plus_100_callback(self, sender):
        self.scale_glyphs((1, 2.0))

    # functions

    def scale_glyphs(self, (factor_x, factor_y)):
        boolstring = [False, True]
        _x_metrics = boolstring[self.w._metrics_X.get()]
        _y_metrics = boolstring[self.w._metrics_Y.get()]
        font = CurrentFont()
        print 'scaling selected glyphs...\n'
        print '\tX factor: %s (scale side-bearings: %s)' % ( factor_x, _x_metrics)
        print '\tY factor: %s (scale vertical metrics: %s)' % ( factor_y, _y_metrics)
        print
        for gName in font.selection:
            try:
                font[gName].prepareUndo('scale')
                _left = font[gName].leftMargin
                _right = font[gName].rightMargin
                # scale outlines
                print '\t%s' % gName,
                font[gName].scale((factor_x, factor_y))
                # scale horizontal metrics
                if _x_metrics:
                    font[gName].leftMargin = _left * factor_x
                    font[gName].rightMargin = _right * factor_x
                # done glyph
                font[gName].performUndo()
            except:
                print '\tcannot transform %s' % gName                        
        # scale vertical metrics
        if _y_metrics:
            font.info.xHeight = font.info.xHeight * factor_y
            font.info.capHeight = font.info.capHeight * factor_y
            font.info.ascender = font.info.ascender * factor_y
            font.info.descender = font.info.descender * factor_y
        # done
        print
        print '\n...done.\n'

    def close_callback(self, sender):
        self.w.close()

# run

scaleGlyphsXYDialog()
