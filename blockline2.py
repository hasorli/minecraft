import minecraft
import block

mc = minecraft.Minecraft.create()

x = raw_input("Block required ?")
int (x)
#block.BLOCK = float(BLOCK)

for x in xrange(0, 10):
  mc.setBlock(x, 10, 0, block.x)
   