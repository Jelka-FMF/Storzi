import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'

initializeJelka()

basic.setFrameRate(60)

basic.onFrame(function (frameNumber, timeSinceStart) {
  lights.setLights(lights.getLights(), colors.rgbColor(255, 44, 255))
  lights.setLights(
    shapes.plane(0, 0, frameNumber % 100, 0, 50, 20),
    colors.cmykColor(100, 28, 28, 0),
  )
  lights.setLights(
    shapes.plane(0, 0, frameNumber % 100, 0, 125, 20),
    colors.cmykColor(100, 68, 100, 0),
  )
})
