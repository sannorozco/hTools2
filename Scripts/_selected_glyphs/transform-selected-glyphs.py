# [h] transform selected glyphs

from vanilla import *

from hTools2.modules.fileutils import getGlyphs
from hTools2.modules.color import randomColor

class transform_glyphs_dialog(object):

    _title = 'transform selected glyphs'
    _round = False
    _decompose = False
    _order = False
    _direction = False
    _overlaps = True
    _mark = True
    _gNames = []

    def __init__(self, font):
        self.font = font
        self.w = Window((220, 220), self._title, closable=False, miniaturizable=False)
        # checkboxes
        self.w.round_checkBox = CheckBox((15, 15, -15, 15), "round", callback=self.round_Callback, value=self._round)
        self.w.decompose_checkBox = CheckBox((15, 40, -15, 15), "decompose", callback=self.decompose_Callback, value=self._decompose)
        self.w.order_checkBox = CheckBox((15, 65, -15, 15), "auto contour order", callback=self.order_Callback, value=self._order)
        self.w.direction_checkBox = CheckBox((15, 90, -15, 15), "auto contour direction", callback=self.direction_Callback, value=self._direction)
        self.w.overlaps_checkBox = CheckBox((15, 115, -15, 15), "remove overlaps", callback=self.overlaps_Callback, value=self._overlaps)
        self.w.mark_checkBox = CheckBox((15, 140, -15, 15), "mark", callback=self.mark_Callback, value=self._mark)
        # buttons
        self.w.button_apply = Button((25, -55, 80, 0), "apply", callback=self.apply_Callback)
        self.w.button_close = Button((-105, -55, 80, 0), "close", callback=self.close_Callback)

        self.w.open()

    def round_Callback(self, sender):
        self._round = sender.get()

    def decompose_Callback(self, sender):
        self._decompose = sender.get()

    def order_Callback(self, sender):
        self._order = sender.get()

    def direction_Callback(self, sender):
        self._direction = sender.get()

    def overlaps_Callback(self, sender):
        self._overlaps = sender.get()

    def mark_Callback(self, sender):
        self._mark = sender.get()

    def apply_Callback(self, sender):
        c = randomColor()
        print 'transforming selected glyphs...\n'
        for gName in getGlyphs(self.font):
            print '\ttransforming %s...' % gName
            if self._round:
                print '\trounding %s' % gName
                f[gName].prepareUndo('round point positions')
                f[gName].round()
                f[gName].performUndo()
            if self._decompose:
                print '\t\tdecomposing...'
                f[gName].prepareUndo('decompose')
                f[gName].decompose()
                f[gName].performUndo()
            if self._order:
                print '\t\tauto contour order...'
                f[gName].prepareUndo('auto contour order')
                f[gName].autoContourOrder()
                f[gName].performUndo()    
            if self._direction:
                print '\t\tauto contour direction...'
                f[gName].prepareUndo('auto contour directions')
                f[gName].correctDirection()
                f[gName].performUndo()
            if self._overlaps:
                print '\t\tremoving overlaps...'
                f[gName].prepareUndo('remove overlaps')
                f[gName].removeOverlap()
                f[gName].performUndo()
            if self._mark:
                print '\t\tmark glyphs...'
                f[gName].prepareUndo('mark')
                f[gName].mark = c
                f[gName].performUndo()
            print
        print '...done.\n'

    def close_Callback(self, sender):
        print 'closed transform glyphs dialog.\n'
        self.w.close()

f = CurrentFont()

if f is not None:
    transform_glyphs_dialog(f)

else:
    print 'please open a font.\n'
    