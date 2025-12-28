import { initializeJelka } from 'jelka'
import { basic, colors, lights } from 'jelka/interface'
import { Axis, Relation } from 'jelka/types'

initializeJelka()

function func(x) {
  return 1 - Math.pow(1 - x, 4)
}

basic.setFrameRate(60)

basic.onFrame((frameNumber, timeSinceStart) => {
  let frameProgress = (frameNumber % 100) / 60
  if (frameProgress > 1) return

  let vert = [0]
  for (let _ = 0; _ < 100; _++) {
    vert.push(0)
  }

  let vert2 = [0]
  for (let _ = 0; _ < 100; _++) {
    vert2.push(0)
  }

  let pos1 = 50 - func(frameProgress) * 70
  let pos2 = 50 + func(frameProgress) * 70

  for (let z = 0; z < 101; z++) {
    vert[z] = (50 - Math.min(Math.abs(z - pos1), Math.abs(z - pos2))) * 4
    if (pos1 < z && z < pos2) {
      vert2[z] = (1 - frameProgress) * 180
    }
  }

  for (let z = 0; z < 101; z++) {
    vert[z] = Math.max(vert[z], 0)
    vert2[z] = Math.max(vert2[z], 0)
    lights.setLights(
      lights.lightsWhere(Axis.Z, Relation.Greater, z),
      colors.rgbColor(vert2[z], vert[z], Math.min(150 + z + vert[z] + vert2[z], 255)),
    )
  }
})
