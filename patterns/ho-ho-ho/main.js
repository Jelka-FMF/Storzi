import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'

initializeJelka()

basic.setFrameRate(20)

basic.onFrame(function (frameNumber, timeSinceStart) {
  lights.setLights(lights.getLights(), colors.rgbColor(0, 0, 0))
  lights.setLights(shapes.plane(0, 0, frameNumber % 100, 0, 90, 20), colors.rgbColor(135, 0, 91))
  lights.setLights(
    shapes.plane(0, 0, (frameNumber - 20) % 100, 0, 90, 20),
    colors.rgbColor(0, 70, 10),
  )
  lights.setLights(
    shapes.plane(0, 0, (frameNumber - 40) % 100, 0, 90, 20),
    colors.rgbColor(0, 0, 185),
  )
  lights.setLights(
    shapes.plane(0, 0, (frameNumber - 60) % 100, 0, 90, 20),
    colors.cmykColor(0, 22, 84, 0),
  )
  lights.setLights(
    shapes.plane(0, 0, (frameNumber - 80) % 100, 0, 90, 20),
    colors.rgbColor(255, 0, 0),
  )
})
