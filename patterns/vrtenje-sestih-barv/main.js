import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'

initializeJelka()

basic.onFrame(function (frameNumber, timeSinceStart) {
  lights.setLights(
    shapes.plane(0, 0, 50, (frameNumber % 360) + 30, 0, 1),
    colors.rgbColor(0, 255, 0),
  )
  lights.setLights(shapes.plane(0, 0, 50, frameNumber % 360, 0, 1), colors.rgbColor(255, 0, 0))
  lights.setLights(
    shapes.plane(0, 0, 50, (frameNumber % 360) + 60, 0, 1),
    colors.rgbColor(0, 0, 255),
  )
  lights.setLights(
    shapes.plane(0, 0, 50, (frameNumber % 360) + 90, 0, 1),
    colors.rgbColor(255, 255, 0),
  )
  lights.setLights(
    shapes.plane(0, 0, 50, (frameNumber % 360) + 120, 0, 1),
    colors.rgbColor(255, 80, 0),
  )
  lights.setLights(
    shapes.plane(0, 0, 50, (frameNumber % 360) + 150, 0, 1),
    colors.rgbColor(255, 0, 240),
  )
})
