import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'

initializeJelka()

basic.onFrame(function (frameNumber, timeSinceStart) {
  lights.resetLights(lights.getLights())
  lights.setLights(lights.getLights(), colors.hslColor(frameNumber % 0.5, 50, 57))
  lights.setLights(shapes.plane(0, 0, 50, 0, frameNumber, 10), colors.rgbColor(255, 153, 204))
  lights.setLights(shapes.plane(0, 0, 50, 0, 0 - frameNumber, 10), colors.rgbColor(255, 153, 204))
  lights.setLights(lights.getLights(), colors.rgbColor(121, 176, 238))
  lights.setLights(shapes.plane(0, 0, 50, 0, 0 - frameNumber, 10), colors.rgbColor(255, 153, 204))
  lights.setLights(shapes.plane(0, 0, 50, 0, frameNumber, 10), colors.rgbColor(255, 153, 204))
})
