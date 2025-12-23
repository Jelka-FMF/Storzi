import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'
import { Axis, Relation } from 'jelka/types'

initializeJelka()

basic.onFrame(function (frameNumber, timeSinceStart) {
  if (timeSinceStart < 1000) {
    // First 2 seconds → blue
    lights.setLights(lights.getLights(), colors.rgbColor(0, 0, 255))
  } else {
    // After 2 seconds → green
    lights.setLights(lights.getLights(), colors.rgbColor(0, 220, 0))
    lights.setLights(
      shapes.ball(0, 0, Math.sin(timeSinceStart / 300) * 20 + 50, 20),
      colors.rgbColor(255, 0, 0),
    )
    if (Math.sin(timeSinceStart / 40 - 0.5) > 0) {
      lights.setLights(
        lights.lightsWhere(Axis.Z, Relation.Less, 20, lights.getLights()),
        colors.rgbColor(0, 250, 0),
      )
      lights.setLights(lights.randomLight(), colors.rgbColor(0, 0, 255))
    } else {
      lights.setLights(
        lights.lightsWhere(Axis.Z, Relation.Less, 20, lights.getLights()),
        colors.rgbColor(0, 190, 0),
      )
    }
    if (Math.sin(timeSinceStart / 600 - 0.5) > 0) {
      lights.setLights(
        lights.lightsWhere(Axis.Z, Relation.Greater, 88, lights.getLights()),
        colors.rgbColor(255, 255, 0),
      )
    }
  }
})
