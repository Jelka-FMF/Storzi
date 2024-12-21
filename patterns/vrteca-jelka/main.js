import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'
import { Relation } from 'jelka/types'

initializeJelka()

basic.setFrameRate(60)

basic.onFrame(function (frameNumber, timeSinceStart) {
  lights.setLights(lights.getLights(), colors.rgbColor(0, 103, 255))
  lights.setLights(
    shapes.planeRelation(0, 0, 0, 0, frameNumber % 360, Relation.Greater),
    colors.rgbColor(161, 0, 59),
  )
  lights.setLights(
    shapes.planeRelation(0, 0, 50, 0, frameNumber % 360, Relation.Greater),
    colors.cmykColor(0, 100, 48, 0),
  )
  lights.setLights(shapes.plane(0, 0, 50, 0, frameNumber % 360, 5), colors.rgbColor(0, 0, 255))
})
