import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'
import { Axis, Relation } from 'jelka/types'

initializeJelka()

basic.onFrame(function (frameNumber, timeSinceStart) {
  lights.resetLights(lights.getLights())
  lights.setLights(
    lights.lightsWhere(Axis.X, Relation.Less, 0, lights.getLights()),
    colors.rgbColor(frameNumber % 0.5, 70, 255),
  )
  lights.setLights(
    lights.lightsWhere(Axis.X, Relation.Greater, 0, lights.getLights()),
    colors.rgbColor(255, frameNumber % 0.5, 40),
  )
  lights.setLights(shapes.plane(0, 0, 50, 0, frameNumber, 10), colors.rgbColor(117, 249, 73))
  lights.setLights(shapes.plane(0, 0, 50, 0, frameNumber + 45, 10), colors.rgbColor(0, 255, 255))
  lights.setLights(shapes.plane(0, 0, 50, 0, frameNumber + 90, 10), colors.rgbColor(128, 0, 128))
  lights.setLights(shapes.plane(0, 0, 50, 0, frameNumber + 135, 10), colors.rgbColor(255, 165, 0))
})
