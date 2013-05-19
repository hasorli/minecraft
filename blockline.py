
import minecraft
import block

mc = minecraft.Minecraft.create()

x = raw_input("Block required ?")
x = int(x)

#block.BLOCK = float(BLOCK)

for x in xrange(0, 10):
  mc.setBlock(x, 13, 0, block.Block(x))

