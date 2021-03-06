#!/usr/bin/python
#
# This program assembles the distribution file Gameduino.zip
# from the source .ino files, and the asset files in
# converted-assets.
#

inventory = {
    '1.Basics'          : "sprites256 palettes rotate collision scroll",
    '2.Audio'           : "toccata player sample instruments2",
    '3.Advanced'        : "interrupt splitscreen jkcollision bitmap wireframe snow assets",
    '4.Demo'            : "ball desert chessboard dna spectrum cp437 watterott",
    '5.Games'           : "asteroids frogger chopper manicminer",
    '6.Tools'           : "selftest screenshot memloader joytest",
    '7.Contrib'         : "singingPlant",
}

import zipfile

def clean(src):
    vis = 1
    dst = []
    for l in src:
        assert not chr(9) in l, "Tab found in source"
        if "//'" in l:
            l = l[:l.index("//'")]
        if vis and not "JCB" in l:
            dst.append(l.rstrip() + "\n")
        else:
            if "JCB{" in l:
                vis = 0
            if "}JCB" in l:
                vis = 1
    return "".join(dst)

z = zipfile.ZipFile("Gameduino.zip", "w", zipfile.ZIP_DEFLATED)

for f in "GD.cpp GD.h font8x8.h".split():
    z.write(f, "Gameduino/%s" % f)

legit = []
testset = open("testset", "w")
for d,projs in inventory.items():
    dir = "Gameduino" + "/" + d
    for p in projs.split():
        pd = dir + "/" + p
        z.writestr("%s/%s.ino" % (pd, p), clean(open("%s.ino" % p)))
        for l in open("%s.ino" % p):
            if '#include "' in l:
                hdr = l[10:l.rindex('"')]
                z.write("converted-assets/%s" % hdr, "%s/%s" % (pd, hdr))
                legit.append("converted-assets/%s" % hdr)
        testset.write(p + " ")
        legit.append(p + ".ino")

z.write("contrib/Guino_libray.ino", "Gameduino/7.Contrib/singingPlant/Guino_libray.ino")

testset.close()
z.close()

# print ["./mkino %s" % s for s in " ".join(inventory.values()).split()]
# print " ".join(legit)
