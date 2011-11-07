# [h] round point coordenates to integers

from hTools2.modules.fileutils import getGlyphs

f = CurrentFont()
gNames = getGlyphs(f)

print 'rounding point positions...'
for gName in gNames:
    print '\trounding %s' % gName
    f[gName].prepareUndo()
    f[gName].round()
print '...done.\n'
