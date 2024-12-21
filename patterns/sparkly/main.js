import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'
import { Relation } from 'jelka/types'

initializeJelka()

basic.setFrameRate(20)

basic.onFrame(function (frameNumber, timeSinceStart) {
  if (Math.round(frameNumber / 10) % 5 === 1) {
    lights.setLights(
      shapes.planeRelation(0, 0, 50, 0, frameNumber, Relation.Greater),
      colors.rgbColor(200, 50, 20),
    )
  } else if (Math.round(frameNumber / 10) % 5 === 2) {
    lights.setLights(
      shapes.planeRelation(0, 0, 50, 0, frameNumber, Relation.Greater),
      colors.rgbColor(0, 100, 20),
    )
  } else if (Math.round(frameNumber / 10) % 5 === 3) {
    lights.setLights(
      shapes.planeRelation(0, 0, 50, 0, frameNumber, Relation.Greater),
      colors.rgbColor(0, 100, 20),
    )
  } else if (Math.round(frameNumber / 10) % 5 === 4) {
    lights.setLights(
      shapes.planeRelation(0, 0, 50, 0, frameNumber, Relation.Greater),
      colors.rgbColor(200, 0, 150),
    )
  } else {
    lights.setLights(
      shapes.planeRelation(0, 0, 50, 0, frameNumber, Relation.Greater),
      colors.rgbColor(0, 0, 237),
    )
  }
  lights.resetLights(shapes.planeRelation(0, 0, 50, 0, frameNumber, Relation.Less))
})
